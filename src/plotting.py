"""
plotting.py — Hàm vẽ biểu đồ dùng chung.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import seaborn as sns
from scipy.spatial import ConvexHull
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

from src.config import (
    OUTPUT_DIR,
    SUBJECT_LABELS,
    CLUSTER_COLORS,
    CLUSTER_LABELS,
)


def setup_style() -> None:
    """Thiết lập style matplotlib/seaborn nhất quán."""
    sns.set_theme(style="whitegrid")
    plt.rcParams["figure.dpi"] = 120


def plot_score_histogram(data, title: str, filename: str) -> None:
    """
    Vẽ histogram phân phối điểm và lưu ra file PNG.

    Args:
        data:     Series/array điểm số (đã dropna).
        title:    Tiêu đề biểu đồ.
        filename: Đường dẫn file PNG đầu ra.
    """
    bins = np.arange(0, 10.5, 0.5)

    n       = len(data)
    mean    = data.mean()
    median  = data.median()
    std     = data.std()
    count_10 = (data == 10).sum()
    count_0  = (data == 0).sum()

    fig, ax = plt.subplots(figsize=(9, 6))
    sns.histplot(data, bins=bins, binrange=(0, 10), kde=False, ax=ax)

    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel("Điểm số")
    ax.set_ylabel("Số lượng thí sinh")
    ax.set_xlim(0, 10)
    ax.set_xticks(bins)

    summary_text = (
        f"Số thí sinh: {n:,}\n"
        f"ĐTB: {mean:.2f}\n"
        f"Trung vị: {median:.2f}\n"
        f"Độ lệch chuẩn: {std:.2f}\n"
        f"Số điểm 10: {count_10:,}\n"
        f"Số điểm 0: {count_0:,}"
    )
    plt.gcf().text(
        0.15, 0.7, summary_text, fontsize=12,
        bbox=dict(facecolor="white", alpha=0.8, edgecolor="gray"),
    )

    plt.tight_layout()
    plt.savefig(filename, dpi=120, bbox_inches="tight")
    plt.close(fig)


def plot_all_subject_histograms(df, output_dir: str = OUTPUT_DIR) -> None:
    """
    Vẽ histogram cho tất cả các môn thi (trừ ngoại ngữ xử lý riêng).

    Args:
        df:         DataFrame đã load từ Parquet.
        output_dir: Thư mục lưu ảnh.
    """
    os.makedirs(output_dir, exist_ok=True)
    score_columns = df.select_dtypes(include=["float32", "float64"]).columns
    score_columns = score_columns.drop("ngoai_ngu", errors="ignore")

    for col in score_columns:
        data = df[col].dropna()
        if not data.empty:
            file_path = os.path.join(output_dir, f"{col}.png")
            label = SUBJECT_LABELS.get(col, col)
            plot_score_histogram(data, f"Phân bố điểm - {label}", file_path)
            print(f"Saved: {col}.png")


def plot_foreign_language_histograms(df, output_dir: str = OUTPUT_DIR) -> None:
    """
    Vẽ histogram điểm Ngoại ngữ, tách theo từng mã ngôn ngữ (N1–N7).

    Args:
        df:         DataFrame đã load từ Parquet.
        output_dir: Thư mục lưu ảnh.
    """
    from src.config import FOREIGN_LANG_LABELS

    os.makedirs(output_dir, exist_ok=True)
    if "ngoai_ngu" not in df.columns or "ma_mon_ngoai_ngu" not in df.columns:
        return

    langs = df[["ngoai_ngu", "ma_mon_ngoai_ngu"]].dropna(
        subset=["ngoai_ngu", "ma_mon_ngoai_ngu"]
    )
    for code, group in langs.groupby("ma_mon_ngoai_ngu"):
        filename  = os.path.join(output_dir, f"ngoai_ngu_{code}.png")
        lang_name = FOREIGN_LANG_LABELS.get(code, code)
        title     = f"Phân bố điểm Ngoại ngữ - {lang_name} ({code})"
        plot_score_histogram(group["ngoai_ngu"], title, filename)
        print(f"Saved: ngoai_ngu_{code}.png")


def plot_foreign_language_bar(df, output_dir: str = OUTPUT_DIR) -> None:
    """
    Vẽ bar chart ngang – tỷ lệ đăng ký thi các môn Ngoại ngữ.

    Args:
        df:         DataFrame đã load từ Parquet.
        output_dir: Thư mục lưu ảnh.
    """
    from src.config import FOREIGN_LANG_LABELS

    os.makedirs(output_dir, exist_ok=True)
    lang_counts = (
        df[df["ma_mon_ngoai_ngu"].notna() & df["ngoai_ngu"].notna()]
        ["ma_mon_ngoai_ngu"]
        .value_counts()
        .sort_values(ascending=True)
    )

    total    = lang_counts.sum()
    y_labels = [f"{FOREIGN_LANG_LABELS.get(c, c)} ({c})" for c in lang_counts.index]
    counts   = lang_counts.values

    base_color = "#2176AE"
    n = len(counts)
    bar_colors = [
        (*[c + (1 - c) * (1 - (i + 1) / n * 0.75)
           for c in plt.matplotlib.colors.to_rgb(base_color)],)
        for i in range(n)
    ]

    with plt.style.context("seaborn-v0_8-whitegrid"):
        fig, ax = plt.subplots(figsize=(11, 6))
        fig.patch.set_facecolor("white")
        ax.set_facecolor("white")

        bars = ax.barh(y_labels, counts, color=bar_colors, edgecolor="none", height=0.55)

        for bar, count in zip(bars, counts):
            pct   = count / total * 100
            lbl   = f"{count:,}  ({pct:.2f}%)"
            x_end = bar.get_width()
            y_mid = bar.get_y() + bar.get_height() / 2
            if count / total > 0.08:
                ax.text(x_end - total * 0.004, y_mid, lbl,
                        ha="right", va="center", fontsize=12,
                        fontweight="bold", color="white")
            else:
                ax.text(x_end + total * 0.003, y_mid, lbl,
                        ha="left", va="center", fontsize=12,
                        fontweight="bold", color="#333333")

        ax.set_axisbelow(True)
        ax.xaxis.grid(True, color="#BBBBBB", linestyle="--", linewidth=0.8, alpha=0.7)
        ax.yaxis.grid(False)
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x/1000:.0f}K"))
        ax.tick_params(axis="x", labelsize=11, length=0, pad=6)
        ax.tick_params(axis="y", labelsize=12, length=0, pad=6)
        ax.set_xlim(right=max(counts) * 1.22)
        ax.set_title("Tỷ lệ đăng ký thi các môn Ngoại ngữ",
                     fontsize=16, fontweight="bold", pad=16, color="#111111")
        ax.set_xlabel("Số thí sinh", fontsize=12, labelpad=8, color="#444444")
        ax.set_ylabel("Môn Ngoại ngữ", fontsize=12, labelpad=8, color="#444444")
        for side in ["top", "right", "left"]:
            ax.spines[side].set_visible(False)
        ax.spines["bottom"].set_color("#CCCCCC")

        plt.tight_layout()
        save_path = os.path.join(output_dir, "ngoai_ngu_bar.png")
        plt.savefig(save_path, dpi=120, bbox_inches="tight")
        plt.close(fig)
    print(f"Saved: ngoai_ngu_bar.png")


def plot_num_subjects_bar(df, output_dir: str = OUTPUT_DIR) -> None:
    """
    Vẽ bar chart phân bố số môn thi của mỗi thí sinh.

    Args:
        df:         DataFrame đã load từ Parquet (phải có cột num_subjects).
        output_dir: Thư mục lưu ảnh.
    """
    from src.config import SCORE_COLS

    os.makedirs(output_dir, exist_ok=True)
    df = df.copy()
    df["num_subjects"]  = df[SCORE_COLS].notna().sum(axis=1)
    num_subj_counts     = df["num_subjects"].value_counts().sort_index()
    total_students      = num_subj_counts.sum()
    BAR_COLOR           = "#2176AE"

    with plt.style.context("seaborn-v0_8-whitegrid"):
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor("white")
        ax.set_facecolor("white")

        bars = ax.bar(
            num_subj_counts.index.astype(str),
            num_subj_counts.values,
            color=BAR_COLOR, edgecolor="none", width=0.6,
        )

        for bar, val in zip(bars, num_subj_counts.values):
            pct = val / total_students * 100
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + total_students * 0.003,
                f"{val:,}\n({pct:.1f}%)",
                ha="center", va="bottom", fontsize=11,
                fontweight="bold", color="#333333",
            )

        ax.set_axisbelow(True)
        ax.yaxis.grid(True, color="#BBBBBB", linestyle="--", linewidth=0.8, alpha=0.7)
        ax.xaxis.grid(False)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x/1000:.0f}K"))
        ax.tick_params(axis="x", labelsize=12, length=0, pad=6)
        ax.tick_params(axis="y", labelsize=11, length=0, pad=6)
        ax.set_ylim(top=max(num_subj_counts.values) * 1.18)
        ax.set_title("Phân bố số môn thi của mỗi thí sinh",
                     fontsize=16, fontweight="bold", pad=16, color="#111111")
        ax.set_xlabel("Số môn thi", fontsize=12, labelpad=8, color="#444444")
        ax.set_ylabel("Số thí sinh",  fontsize=12, labelpad=8, color="#444444")
        for side in ["top", "right", "left"]:
            ax.spines[side].set_visible(False)
        ax.spines["bottom"].set_color("#CCCCCC")

        plt.tight_layout()
        save_path = os.path.join(output_dir, "num_subjects_bar.png")
        plt.savefig(save_path, dpi=120, bbox_inches="tight")
        plt.close(fig)
    print(f"Saved: num_subjects_bar.png")


def plot_correlation_heatmap(df, output_dir: str = OUTPUT_DIR) -> None:
    """
    Vẽ heatmap tương quan giữa các môn thi chính.

    Args:
        df:         DataFrame đã load từ Parquet.
        output_dir: Thư mục lưu ảnh.
    """
    os.makedirs(output_dir, exist_ok=True)
    corr_cols = ["toan", "van", "li", "hoa", "sinh", "su", "dia", "ngoai_ngu"]
    corr_labels = {
        "toan": "Toán", "van": "Ngữ văn", "li": "Vật lí",
        "hoa": "Hóa học", "sinh": "Sinh học", "su": "Lịch sử",
        "dia": "Địa lí", "ngoai_ngu": "Ngoại ngữ",
    }
    corr_matrix = df[corr_cols].corr().round(2)
    corr_matrix.index   = [corr_labels[c] for c in corr_matrix.index]
    corr_matrix.columns = [corr_labels[c] for c in corr_matrix.columns]

    mask = np.zeros_like(corr_matrix, dtype=bool)
    mask[np.triu_indices_from(mask, k=1)] = True

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(
        corr_matrix, mask=mask, annot=True, fmt=".2f",
        cmap="RdYlGn", vmin=-1, vmax=1,
        linewidths=0.5, linecolor="white",
        annot_kws={"size": 12}, ax=ax, square=True,
        cbar_kws={"shrink": 0.8, "label": "Hệ số tương quan"},
    )
    ax.set_title("Tương quan điểm thi giữa các môn",
                 fontsize=16, fontweight="bold", pad=16)
    ax.tick_params(axis="x", labelsize=12, rotation=30)
    ax.tick_params(axis="y", labelsize=12, rotation=0)
    plt.tight_layout()
    save_path = os.path.join(output_dir, "corr_heatmap.png")
    plt.savefig(save_path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: corr_heatmap.png")


def kmeans_subject_2d(
    df,
    subject_col: str,
    subject_label: str,
    k: int = 4,
    group_col: str = "tinh",
    output_dir: str = OUTPUT_DIR,
):
    """
    Phân cụm K-Means (Elbow + Silhouette + scatter 2D) theo mean & std
    của một môn thi đơn lẻ, theo nhóm tỉnh.

    Args:
        df:            DataFrame đã load từ Parquet.
        subject_col:   Tên cột điểm (vd: 'toan').
        subject_label: Tên hiển thị (vd: 'Toán').
        k:             Số cụm K-Means.
        group_col:     Cột nhóm (mặc định 'tinh').
        output_dir:    Thư mục lưu ảnh.

    Returns:
        DataFrame thống kê theo tỉnh với cột cluster_rank.
    """
    os.makedirs(output_dir, exist_ok=True)

    # --- Tính mean & std ---
    mean_col = f"mean_{subject_col}"
    std_col  = f"std_{subject_col}"
    stats = (
        df.dropna(subset=[group_col, subject_col])
        .groupby(group_col)[subject_col]
        .agg(**{mean_col: "mean", std_col: "std"})
        .reset_index()
        .dropna()
    )
    print(f"Số tỉnh có dữ liệu {subject_label}: {len(stats)}")

    X        = stats[[mean_col, std_col]].values
    scaler   = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # --- Elbow + Silhouette ---
    K_range    = range(2, 10)
    inertias   = []
    sil_scores = []
    for kk in K_range:
        km_    = KMeans(n_clusters=kk, random_state=42, n_init=10)
        lbl_   = km_.fit_predict(X_scaled)
        inertias.append(km_.inertia_)
        sil_scores.append(silhouette_score(X_scaled, lbl_))

    best_k_sil = list(K_range)[np.argmax(sil_scores)]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].plot(list(K_range), inertias, "o-", color="steelblue", linewidth=2, markersize=7)
    axes[0].set_title(f"Elbow – Inertia vs K ({subject_label})", fontsize=13, fontweight="bold")
    axes[0].set_xlabel("Số cụm K")
    axes[0].set_ylabel("Inertia (WCSS)")
    axes[0].xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    axes[1].plot(list(K_range), sil_scores, "o-", color="coral", linewidth=2, markersize=7)
    axes[1].axvline(best_k_sil, linestyle="--", color="gray", alpha=0.7,
                    label=f"Best k = {best_k_sil}")
    axes[1].set_title(f"Silhouette Score vs K ({subject_label})", fontsize=13, fontweight="bold")
    axes[1].set_xlabel("Số cụm K")
    axes[1].set_ylabel("Silhouette Score")
    axes[1].xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    axes[1].legend(fontsize=12)

    plt.suptitle(f"Chọn K tối ưu – K-Means (mean & std {subject_label} theo tỉnh)",
                 fontsize=14, fontweight="bold", y=1.02)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, f"kmeans_{subject_col}_optimal_k.png"),
        dpi=120, bbox_inches="tight",
    )
    plt.close(fig)
    print(f"K tối ưu theo Silhouette ({subject_label}): {best_k_sil}")

    # --- Fit K=k ---
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    stats["cluster"] = km.fit_predict(X_scaled)

    cluster_order = (
        stats.groupby("cluster")[mean_col].mean()
        .sort_values(ascending=False).index.tolist()
    )
    rank_map             = {c: i for i, c in enumerate(cluster_order)}
    stats["cluster_rank"] = stats["cluster"].map(rank_map)

    # --- Scatter 2D ---
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_facecolor("#f9f9f9")

    for rank in range(k):
        sub   = stats[stats["cluster_rank"] == rank]
        pts   = sub[[mean_col, std_col]].values
        color = CLUSTER_COLORS[rank]
        if len(pts) >= 3:
            hull      = ConvexHull(pts)
            hull_pts  = np.append(hull.vertices, hull.vertices[0])
            ax.fill(pts[hull_pts, 0], pts[hull_pts, 1], alpha=0.10, color=color, zorder=1)
            ax.plot(pts[hull_pts, 0], pts[hull_pts, 1],
                    linestyle="--", linewidth=1.2, color=color, alpha=0.5, zorder=2)

    for rank in range(k):
        sub = stats[stats["cluster_rank"] == rank]
        ax.scatter(
            sub[mean_col], sub[std_col],
            label=f"{CLUSTER_LABELS[rank]}  (n={len(sub)})",
            color=CLUSTER_COLORS[rank],
            s=90, edgecolors="white", linewidths=0.8, zorder=4,
        )

    for _, row in stats.iterrows():
        ax.annotate(
            row[group_col],
            xy=(row[mean_col], row[std_col]),
            xytext=(4, 4), textcoords="offset points",
            fontsize=7.2, color="#222222",
            path_effects=[pe.withStroke(linewidth=2, foreground="white")],
            zorder=5,
        )

    centers = scaler.inverse_transform(km.cluster_centers_)
    for i, center in enumerate(centers):
        cr = rank_map[i]
        ax.scatter(center[0], center[1],
                   marker="*", s=350, color=CLUSTER_COLORS[cr],
                   edgecolors="black", linewidths=0.9, zorder=6)

    grand_mean = stats[mean_col].mean()
    grand_std  = stats[std_col].mean()
    ax.axvline(grand_mean, color="gray", linestyle=":", linewidth=1.0, alpha=0.6)
    ax.axhline(grand_std,  color="gray", linestyle=":", linewidth=1.0, alpha=0.6)
    ax.text(
        grand_mean + (stats[mean_col].max() - stats[mean_col].min()) * 0.01,
        ax.get_ylim()[1] * 0.995,
        f"ĐTB tổng: {grand_mean:.2f}", fontsize=9, color="gray", va="top",
    )

    ax.set_title(
        f"Phân cụm tỉnh theo Điểm {subject_label} – K-Means (k = {k})\n"
        "Features: Điểm trung bình & Độ lệch chuẩn",
        fontsize=15, fontweight="bold", pad=14,
    )
    ax.set_xlabel(f"Điểm trung bình {subject_label}", fontsize=13)
    ax.set_ylabel(f"Độ lệch chuẩn {subject_label}", fontsize=13)
    ax.tick_params(labelsize=11)
    ax.legend(fontsize=11, title="Cụm (★ = centroid)", title_fontsize=11,
              framealpha=0.9, loc="upper left")
    sns.despine()
    plt.tight_layout()
    save_path = os.path.join(output_dir, f"kmeans_{subject_col}_k{k}_2d.png")
    plt.savefig(save_path, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: kmeans_{subject_col}_k{k}_2d.png")

    # --- Bảng tổng hợp ---
    print(f"\n=== THÀNH PHẦN CÁC CỤM ({subject_label.upper()}) ===")
    for rank in range(k):
        sub = stats[stats["cluster_rank"] == rank].sort_values(mean_col, ascending=False)
        print(f"\n[Cụm {rank+1}] {CLUSTER_LABELS[rank]} — {len(sub)} tỉnh")
        print(f"  ĐTB {subject_label}: {sub[mean_col].mean():.3f}  |  Std TB: {sub[std_col].mean():.3f}")
        print(f"  Tỉnh: {', '.join(sub[group_col].tolist())}")

    return stats


def kmeans_multi_subject_2d(
    df,
    subject_cols: list,
    group_label: str,
    k: int = 4,
    group_col: str = "tinh",
    output_dir: str = OUTPUT_DIR,
):
    """
    Phân cụm K-Means đa môn (multi-feature) theo tỉnh.
    Features: mean + std của mỗi môn trong subject_cols.
    Scatter 2D dùng trục = mean tổng hợp & std tổng hợp.

    Args:
        df:           DataFrame đã load từ Parquet.
        subject_cols: Danh sách cột điểm (vd: ['toan', 'li', 'hoa']).
        group_label:  Tên nhóm môn (vd: 'Tự Nhiên').
        k:            Số cụm K-Means.
        group_col:    Cột nhóm (mặc định 'tinh').
        output_dir:   Thư mục lưu ảnh.

    Returns:
        DataFrame thống kê theo tỉnh với cột cluster_rank.
    """
    import warnings
    warnings.filterwarnings("ignore")
    os.makedirs(output_dir, exist_ok=True)

    slug = "_".join(subject_cols)

    # 1. Lọc thí sinh thi đủ các môn
    df_filtered = df.dropna(subset=subject_cols + [group_col])
    df_filtered = df_filtered[df_filtered[subject_cols].notna().all(axis=1)]
    print(f"Số thí sinh thi đủ {', '.join(subject_cols)}: {len(df_filtered):,}")

    # 2. Tính mean & std theo tỉnh
    agg_dict = {}
    for col in subject_cols:
        agg_dict[f"mean_{col}"] = (col, "mean")
        agg_dict[f"std_{col}"]  = (col, "std")

    stats = df_filtered.groupby(group_col).agg(**agg_dict).reset_index().dropna()
    mean_cols = [f"mean_{c}" for c in subject_cols]
    std_cols  = [f"std_{c}"  for c in subject_cols]
    stats["mean_all"] = stats[mean_cols].mean(axis=1)
    stats["std_all"]  = stats[std_cols].mean(axis=1)

    # 3. Chuẩn hoá 2×n features
    feat_cols = [col for pair in zip(mean_cols, std_cols) for col in pair]
    X        = stats[feat_cols].values
    scaler   = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 4. Elbow + Silhouette
    K_range    = range(2, min(len(stats), 10))
    inertias   = []
    sil_scores = []
    for kk in K_range:
        km_  = KMeans(n_clusters=kk, random_state=42, n_init=10)
        lbl_ = km_.fit_predict(X_scaled)
        inertias.append(km_.inertia_)
        sil_scores.append(silhouette_score(X_scaled, lbl_))

    best_k_sil = list(K_range)[np.argmax(sil_scores)]
    fig, axes  = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].plot(list(K_range), inertias, "o-", color="steelblue", linewidth=2, markersize=7)
    axes[0].set_title(f"Elbow – Inertia vs K ({group_label})", fontsize=13, fontweight="bold")
    axes[0].set_xlabel("Số cụm K"); axes[0].set_ylabel("Inertia (WCSS)")
    axes[0].xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    axes[1].plot(list(K_range), sil_scores, "o-", color="coral", linewidth=2, markersize=7)
    axes[1].axvline(best_k_sil, linestyle="--", color="gray", alpha=0.7,
                    label=f"Best k = {best_k_sil}")
    axes[1].set_title(f"Silhouette Score vs K ({group_label})", fontsize=13, fontweight="bold")
    axes[1].set_xlabel("Số cụm K"); axes[1].set_ylabel("Silhouette Score")
    axes[1].xaxis.set_major_locator(plt.MaxNLocator(integer=True))
    axes[1].legend(fontsize=12)
    plt.suptitle(f"Chọn K tối ưu – K-Means khối {group_label}",
                 fontsize=14, fontweight="bold", y=1.02)
    plt.tight_layout()
    plt.savefig(
        os.path.join(output_dir, f"kmeans_{slug}_optimal_k.png"),
        dpi=120, bbox_inches="tight",
    )
    plt.close(fig)
    print(f"K tối ưu theo Silhouette: {best_k_sil}")

    # 5. Fit K=k
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    stats["cluster"] = km.fit_predict(X_scaled)
    cluster_order    = (
        stats.groupby("cluster")["mean_all"].mean()
        .sort_values(ascending=False).index.tolist()
    )
    rank_map              = {c: i for i, c in enumerate(cluster_order)}
    stats["cluster_rank"] = stats["cluster"].map(rank_map)

    # 6. Scatter 2D
    fig, ax = plt.subplots(figsize=(14, 9))
    ax.set_facecolor("#f9f9f9")

    for rank in range(k):
        sub   = stats[stats["cluster_rank"] == rank]
        pts   = sub[["mean_all", "std_all"]].values
        color = CLUSTER_COLORS[rank]
        if len(pts) >= 3:
            hull      = ConvexHull(pts)
            hull_pts  = np.append(hull.vertices, hull.vertices[0])
            ax.fill(pts[hull_pts, 0], pts[hull_pts, 1], alpha=0.10, color=color, zorder=1)
            ax.plot(pts[hull_pts, 0], pts[hull_pts, 1],
                    linestyle="--", linewidth=1.2, color=color, alpha=0.5, zorder=2)

    for rank in range(k):
        sub = stats[stats["cluster_rank"] == rank]
        ax.scatter(sub["mean_all"], sub["std_all"],
                   label=f"{CLUSTER_LABELS[rank]}  (n={len(sub)})",
                   color=CLUSTER_COLORS[rank],
                   s=90, edgecolors="white", linewidths=0.8, zorder=4)

    for _, row in stats.iterrows():
        ax.annotate(
            row[group_col],
            xy=(row["mean_all"], row["std_all"]),
            xytext=(4, 4), textcoords="offset points",
            fontsize=7.2, color="#222222",
            path_effects=[pe.withStroke(linewidth=2, foreground="white")],
            zorder=5,
        )

    centers_orig = scaler.inverse_transform(km.cluster_centers_)
    for i, center in enumerate(centers_orig):
        cr         = rank_map[i]
        c_mean_all = np.mean([center[feat_cols.index(f"mean_{c}")] for c in subject_cols])
        c_std_all  = np.mean([center[feat_cols.index(f"std_{c}")]  for c in subject_cols])
        ax.scatter(c_mean_all, c_std_all,
                   marker="*", s=350, color=CLUSTER_COLORS[cr],
                   edgecolors="black", linewidths=0.9, zorder=6)

    grand_mean = stats["mean_all"].mean()
    grand_std  = stats["std_all"].mean()
    ax.axvline(grand_mean, color="gray", linestyle=":", linewidth=1.0, alpha=0.6)
    ax.axhline(grand_std,  color="gray", linestyle=":", linewidth=1.0, alpha=0.6)
    ax.text(
        grand_mean + (stats["mean_all"].max() - stats["mean_all"].min()) * 0.01,
        ax.get_ylim()[1] * 0.995,
        f"ĐTB tổng: {grand_mean:.2f}", fontsize=9, color="gray", va="top",
    )

    subject_names = " + ".join(
        SUBJECT_LABELS.get(c, c) for c in subject_cols
    )
    ax.set_title(
        f"Phân cụm tỉnh – Khối {group_label} ({subject_names}) – K-Means (k = {k})\n"
        f"Trục: ĐTB tổng hợp & Độ lệch chuẩn TB ({len(subject_cols)*2} features)",
        fontsize=14, fontweight="bold", pad=14,
    )
    ax.set_xlabel(f"ĐTB tổng hợp ({subject_names})", fontsize=13)
    ax.set_ylabel("Độ lệch chuẩn trung bình", fontsize=13)
    ax.tick_params(labelsize=11)
    ax.legend(fontsize=11, title="Cụm (★ = centroid)", title_fontsize=11,
              framealpha=0.9, loc="upper left")
    sns.despine()
    plt.tight_layout()
    save_path = os.path.join(output_dir, f"kmeans_{slug}_k{k}_2d.png")
    plt.savefig(save_path, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: kmeans_{slug}_k{k}_2d.png")

    # 7. Bảng tổng hợp
    print(f"\n=== THÀNH PHẦN CÁC CỤM (KHỐI {group_label.upper()}) ===")
    for rank in range(k):
        sub = stats[stats["cluster_rank"] == rank].sort_values("mean_all", ascending=False)
        print(f"\n[Cụm {rank+1}] {CLUSTER_LABELS[rank]} — {len(sub)} tỉnh")
        for mc in mean_cols:
            lbl = SUBJECT_LABELS.get(mc.replace("mean_", ""), mc)
            print(f"  ĐTB {lbl}: {sub[mc].mean():.3f}", end="  |  ")
        print(f"\n  ĐTB tổng hợp: {sub['mean_all'].mean():.3f}  |  Std TB: {sub['std_all'].mean():.3f}")
        print(f"  Tỉnh: {', '.join(sub[group_col].tolist())}")

    return stats
