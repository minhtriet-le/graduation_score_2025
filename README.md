

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

## 📂 Cấu trúc dự án

- `charts/` — Chứa toàn bộ biểu đồ, heatmap, scatter plot, kết quả clustering, v.v.
- `dist/` — Website đã build sẵn (HTML, CSS, JS) để xem báo cáo offline hoặc deploy.
- `process.ipynb` — Notebook xử lý dữ liệu, phân tích thống kê, sinh biểu đồ.
- `combined_data.parquet` — Dữ liệu đã tổng hợp, dùng cho phân tích (không bắt buộc phải có khi sử dụng website).
- `raw_data/` — Dữ liệu gốc (Excel, có thể chứa dữ liệu nhạy cảm, không chia sẻ công khai).

## Quy trình phân tích & kỹ thuật sử dụng

1. **Tiền xử lý dữ liệu**: Tổng hợp, làm sạch dữ liệu điểm từ nhiều nguồn, chuẩn hóa định dạng, loại bỏ giá trị ngoại lai.
2. **Phân tích thống kê mô tả**: Tính toán các chỉ số trung bình, phương sai, phân phối điểm từng môn, từng nhóm đối tượng.
3. **Trực quan hóa dữ liệu**: Sinh các biểu đồ histogram, bar chart, scatter plot, heatmap tương quan, giúp nhận diện xu hướng và mối liên hệ giữa các môn.
4. **Phân tích nâng cao**:
   - Phân cụm học sinh theo điểm số (KMeans clustering)
   - Kiểm định giả thuyết thống kê giữa các nhóm, các vùng miền
   - So sánh phân phối điểm giữa các năm, các tổ hợp môn
5. **Xây dựng báo cáo số**: Tổng hợp kết quả, xuất biểu đồ, xây dựng website báo cáo tương tác.

## 📊 Nội dung báo cáo

Báo cáo gồm:

- Phân phối điểm các môn: Toán, Ngữ văn, Vật lí, Hóa học, Sinh học, Lịch sử, Địa lí, Tin học, Công nghệ, Giáo dục Kinh tế & Pháp luật, Giáo dục Công dân, Ngoại ngữ (Anh, Nga, Pháp, Trung, Đức, Nhật, Hàn)
- Biểu đồ so sánh, heatmap tương quan giữa các môn
- Phân tích số lượng môn thi, phân cụm học sinh theo điểm số (KMeans)
- Một số kiểm định giả thuyết thống kê (so sánh trung bình, kiểm định phân phối, v.v.)
- Các biểu đồ chuyên sâu: phân tích theo vùng miền, tổ hợp môn, nhóm đối tượng

## 🛠️ Công nghệ & công cụ

- **Python 3.x** — Ngôn ngữ chính cho xử lý và phân tích dữ liệu
- **Pandas, Numpy** — Xử lý, tổng hợp dữ liệu
- **Matplotlib, Seaborn** — Trực quan hóa dữ liệu
- **Scikit-learn** — Phân cụm, phân tích nâng cao
- **Jupyter Notebook** (`process.ipynb`) — Quy trình phân tích, sinh biểu đồ, tài liệu hóa từng bước
- **HTML/CSS/JS** (thư mục `dist/`) — Hiển thị báo cáo, tương tác biểu đồ

## 📦 Hướng dẫn sử dụng

### Xem báo cáo

1. **Khuyên dùng:** Truy cập GitHub Pages để xem báo cáo trực tuyến.
2. **Xem offline:** Clone repo, mở file `dist/index.html` bằng trình duyệt.

### Tái tạo phân tích & biểu đồ

1. Cài Python 3.x và các thư viện cần thiết:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```
2. Mở và chạy toàn bộ notebook `process.ipynb` để sinh lại các biểu đồ, bảng phân tích.
3. Kết quả sẽ được lưu vào thư mục `charts/` và có thể cập nhật vào website (`dist/`).

### Cấu hình & mở rộng

- Có thể thay thế dữ liệu gốc trong `raw_data/` để phân tích các năm khác.
- Tùy chỉnh, mở rộng các phân tích trong notebook theo nhu cầu.

## Đóng góp & phát triển

Mọi đóng góp về code, dữ liệu, ý tưởng phân tích hoặc phản hồi về báo cáo đều được hoan nghênh!

- Gửi issue hoặc pull request trực tiếp trên GitHub.
- Đề xuất thêm các phân tích, biểu đồ, hoặc cải tiến giao diện website.

## Liên hệ

- **Tác giả:** Lê Minh Triết
- **GitHub:** [minhtriet-le](https://github.com/minhtriet-le)

## 📄 Bản quyền & sử dụng dữ liệu

Dữ liệu và mã nguồn chỉ sử dụng cho mục đích học tập, nghiên cứu, phi thương mại. Khi sử dụng lại vui lòng ghi nguồn dự án. Nếu có thắc mắc về bản quyền dữ liệu gốc, vui lòng liên hệ tác giả.
