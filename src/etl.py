"""
etl.py — ETL pipeline: Excel → Parquet, thêm cột tỉnh/tỉnh_mới.
"""

import pandas as pd
from pathlib import Path
from unidecode import unidecode

from src.config import PROVINCE_NEW_PROVINCE, CODE_PROVINCE, SCORE_COLS


def export_to_parquet(
    folder_name: str,
    output_filename: str = "combined_data.parquet",
) -> None:
    """
    Đọc tất cả file .xlsx trong thư mục, chuẩn hoá, gộp thành một DataFrame
    và xuất ra file Parquet.

    Args:
        folder_name:     Đường dẫn thư mục chứa file .xlsx.
        output_filename: Tên file Parquet đầu ra.
    """
    data_dir = Path(folder_name)
    all_dfs = []

    # 1. Đọc tất cả sheet từ tất cả file Excel
    for file_path in data_dir.glob("*.xlsx"):
        print(f"Reading: {file_path.name}")
        excel_data = pd.read_excel(file_path, sheet_name=None)

        for sheet_name, df in excel_data.items():
            df["origin_file"]  = file_path.name
            df["origin_sheet"] = str(sheet_name)
            df.columns         = df.columns.astype(str)
            all_dfs.append(df)

    if not all_dfs:
        print("No data found to export.")
        return

    # 2. Gộp tất cả DataFrame
    final_df = pd.concat(all_dfs, ignore_index=True)

    # Chuẩn hoá tên cột: bỏ dấu, viết thường, thay space → _
    final_df.columns = [
        unidecode(col).lower().replace(" ", "_") for col in final_df.columns
    ]

    # Lọc dòng có SBD, chuẩn hoá 8 chữ số
    final_df = final_df[final_df["sobaodanh"].notna()]
    final_df["sobaodanh"] = (
        final_df["sobaodanh"].astype(int).astype(str).str.zfill(8)
    )

    # Chọn và sắp xếp cột
    keep_cols = [
        "sobaodanh", "toan", "van", "li", "hoa", "sinh", "tin_hoc",
        "cong_nghe_cong_nghiep", "cong_nghe_nong_nghiep", "su", "dia",
        "giao_duc_kinh_te_va_phap_luat", "ngoai_ngu", "giao_duc_cong_dan",
        "ma_mon_ngoai_ngu", "origin_file", "origin_sheet",
    ]
    final_df = final_df[keep_cols]

    # Kiểu string
    string_cols = ["sobaodanh", "ma_mon_ngoai_ngu", "origin_file", "origin_sheet"]
    for col in string_cols:
        if col in final_df.columns:
            final_df[col] = final_df[col].astype("string")

    # Kiểu float32 cho điểm số
    for col in SCORE_COLS:
        if col in final_df.columns:
            final_df[col] = pd.to_numeric(final_df[col], errors="coerce").astype("float32")

    final_df = final_df.sort_values("sobaodanh").reset_index(drop=True)

    # 3. Xuất Parquet
    final_df.to_parquet(output_filename, engine="pyarrow", index=False)
    print("-" * 40)
    print(f"✅ Exported to: {output_filename}")
    print(f"   Rows:    {len(final_df):,}")
    print(f"   Columns: {len(final_df.columns)}")


def add_province_columns(
    parquet_file: str = "combined_data.parquet",
) -> None:
    """
    Thêm cột 'ma_tinh', 'tinh' (tỉnh gốc) và 'tinh_moi' (sau sáp nhập)
    vào file Parquet đã có.

    Args:
        parquet_file: Đường dẫn file Parquet cần cập nhật.
    """
    df = pd.read_parquet(parquet_file)

    if "ma_tinh" not in df.columns:
        df["ma_tinh"] = df["sobaodanh"].str[:2]

    df["tinh"]     = df["ma_tinh"].map(CODE_PROVINCE).astype("string")
    df["tinh_moi"] = df["tinh"].map(PROVINCE_NEW_PROVINCE).astype("string")

    df.to_parquet(parquet_file, engine="pyarrow", index=False)
    print(f'✅ Đã thêm cột "ma_tinh", "tinh", "tinh_moi" → {parquet_file}')
    print(f'   Null trong "tinh":     {df["tinh"].isna().sum()}')
    print(f'   Null trong "tinh_moi": {df["tinh_moi"].isna().sum()}')
