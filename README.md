

# Phân tích & Báo cáo Điểm thi Tốt nghiệp THPT 2025

## Giới thiệu

Dự án cung cấp hệ thống báo cáo số hóa, trực quan hóa và phân tích chuyên sâu về điểm thi tốt nghiệp THPT năm 2025 tại Việt Nam. Báo cáo tập trung vào từng môn học, nhóm môn, khai thác các kỹ thuật phân tích dữ liệu hiện đại như trực quan hóa, phân cụm (clustering), kiểm định giả thuyết thống kê, nhằm hỗ trợ nhà quản lý giáo dục, giáo viên, học sinh và phụ huynh hiểu rõ hơn về xu hướng, đặc điểm và mối liên hệ giữa các môn thi.

## Động lực & Mục tiêu

- Cung cấp góc nhìn tổng quan và chi tiết về kết quả thi tốt nghiệp THPT 2025.
- Phát hiện các xu hướng, bất thường, mối tương quan giữa các môn học.
- Hỗ trợ xây dựng chính sách giáo dục, định hướng ôn tập, lựa chọn tổ hợp môn phù hợp.
- Thực hành, trình bày kỹ năng phân tích dữ liệu, trực quan hóa và xây dựng báo cáo số.

## 🚀 Xem báo cáo trực tuyến

👉 **[Xem bản báo cáo tại GitHub Pages](https://minhtriet-le.github.io/graduation_score_2025/)**

---

## 📂 Cấu trúc dự án

```
graduation_score_2025/
│
├── src/                        ← Python modules (tái sử dụng)
│   ├── config.py               ← Hằng số: nhãn môn, màu sắc, bảng mã tỉnh...
│   ├── etl.py                  ← export_to_parquet(), add_province_columns()
│   ├── plotting.py             ← Hàm vẽ biểu đồ histogram, bar, heatmap, K-Means
│   └── stats.py                ← compare_two_groups() – kiểm định thống kê
│
├── notebooks/
│   ├── 01_etl.ipynb            ← ETL: Excel → Parquet + thêm cột tỉnh
│   ├── 02_eda.ipynb            ← EDA: thống kê mô tả, histogram, heatmap
│   ├── 03_clustering.ipynb     ← K-Means đơn môn & đa môn (Tự Nhiên, Xã Hội)
│   ├── 04_hypothesis.ipynb     ← Kiểm định giả thuyết thống kê
│   └── 05_build.ipynb          ← Chạy toàn bộ pipeline tự động
│
├── dist/                       ← Website báo cáo (HTML/CSS/JS)
│   ├── index.html
│   ├── sections/               ← Từng section báo cáo
│   ├── charts/                 ← Biểu đồ xuất ra (PNG)
│   ├── css/
│   └── js/
│
├── raw_data/                   ← Dữ liệu gốc Excel (không chia sẻ công khai)
├── combined_data.parquet       ← Dữ liệu đã xử lý
├── Makefile                    ← make etl / analysis / build / all / clean
├── requirements.txt
└── README.md
```

---

## 📊 Nội dung phân tích

| Notebook | Nội dung |
|---|---|
| `01_etl` | Đọc nhiều file Excel, chuẩn hoá cột, thêm mã tỉnh, xuất Parquet |
| `02_eda` | Thống kê mô tả (mean/std/skewness), histogram từng môn, bar chart Ngoại ngữ, heatmap tương quan |
| `03_clustering` | K-Means theo tỉnh: đơn môn (Toán, Văn, Lý, Hóa) + đa môn (khối Tự Nhiên, Xã Hội); Elbow + Silhouette để chọn K |
| `04_hypothesis` | Levene's test + Welch's t-test + Cohen's d + Mann-Whitney U; dễ mở rộng thêm cặp so sánh |

**Môn thi được phân tích:** Toán, Ngữ văn, Vật lí, Hóa học, Sinh học, Lịch sử, Địa lí, Tin học, Công nghệ (CN/NN), Giáo dục KT&PL, Giáo dục Công dân, Ngoại ngữ (Anh, Nga, Pháp, Trung, Đức, Nhật, Hàn).

---

## 🛠️ Công nghệ & công cụ

| Thư viện | Mục đích |
|---|---|
| `pandas`, `numpy` | Xử lý, tổng hợp dữ liệu |
| `pyarrow` | Đọc/ghi Parquet hiệu quả |
| `matplotlib`, `seaborn` | Trực quan hoá |
| `scikit-learn` | K-Means clustering, StandardScaler, Silhouette Score |
| `scipy` | Kiểm định thống kê (t-test, Levene, Mann-Whitney) |
| `unidecode` | Chuẩn hoá tên cột tiếng Việt |
| `nbconvert` | Chạy notebook tự động qua Makefile |

---

## 📦 Hướng dẫn sử dụng

### Xem báo cáo

1. **Trực tuyến (khuyên dùng):** [GitHub Pages](https://minhtriet-le.github.io/graduation_score_2025/)
2. **Offline:** Clone repo → mở `dist/index.html` bằng trình duyệt.

### Cài đặt môi trường

```bash
git clone https://github.com/minhtriet-le/graduation_score_2025.git
cd graduation_score_2025
make install          # tạo .venv và cài requirements.txt
```

Hoặc cài thủ công:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Tái tạo toàn bộ phân tích & biểu đồ

```bash
# Khi có dữ liệu Excel mới trong raw_data/
make etl

# Tái sinh toàn bộ chart (không cần chạy lại ETL)
make build

# ETL + build cùng lúc
make all

# Xoá chart cũ
make clean
```

Hoặc chạy từng notebook thủ công trong `notebooks/`.

### Mở rộng phân tích

- **Thêm cặp kiểm định mới:** Mở `04_hypothesis.ipynb`, gọi `compare_two_groups()` với tham số tuỳ chỉnh.
- **Thêm môn clustering:** Trong `03_clustering.ipynb`, gọi `kmeans_subject_2d()` hoặc `kmeans_multi_subject_2d()`.
- **Thay dữ liệu năm khác:** Đặt file `.xlsx` mới vào `raw_data/`, chạy `make etl`.
- **Sửa hằng số chung:** Chỉnh sửa tập trung tại `src/config.py`.

---

## Đóng góp & phát triển

Mọi đóng góp về code, dữ liệu, ý tưởng phân tích hoặc phản hồi về báo cáo đều được hoan nghênh!

- Gửi issue hoặc pull request trực tiếp trên GitHub.
- Đề xuất thêm các phân tích, biểu đồ, hoặc cải tiến giao diện website.

## Liên hệ

- **Tác giả:** Lê Minh Triết
- **GitHub:** [minhtriet-le](https://github.com/minhtriet-le)

## 📄 Bản quyền & sử dụng dữ liệu

Dữ liệu và mã nguồn chỉ sử dụng cho mục đích học tập, nghiên cứu, phi thương mại. Khi sử dụng lại vui lòng ghi nguồn dự án. Nếu có thắc mắc về bản quyền dữ liệu gốc, vui lòng liên hệ tác giả.
