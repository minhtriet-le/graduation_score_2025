# 🎨 Minimalist Modern Theme – Hướng dẫn sử dụng

## 📋 Mục lục

1. [Giới thiệu](#giới-thiệu)
2. [Đặc điểm chính](#đặc-điểm-chính)
3. [Kiến trúc](#kiến-trúc-css)
4. [Tùy chỉnh](#tùy-chỉnh)
5. [Hỗ trợ trình duyệt](#hỗ-trợ-trình-duyệt)

---

## Giới thiệu

**Minimalist Modern Theme** là một thiết kế tối giản, hiện đại được xây dựng với các tiêu chuẩn web mới nhất. Theme này tập trung vào:

- ✨ **Sạch sẽ & Tối giản**: Giao diện không quá tải, tập trung vào nội dung
- 🎯 **Hiệu suất cao**: CSS tối ưu, chuyển động mượt mà
- 📱 **Responsive**: Hoạt động hoàn hảo trên mọi kích thước màn hình
- ♿ **Accessibility**: Tuân theo tiêu chuẩn WCAG 2.1

---

## Đặc điểm chính

### 1. **Hệ thống Màu Minimalist**

```css
--primary: #1f2937;        /* Dark slate */
--accent: #06b6d4;         /* Cyan accent */
--surface: #ffffff;        /* White background */
--text-primary: #111827;   /* Near black */
--text-secondary: #6b7280; /* Medium gray */
```

Palette sử dụng **cyan (#06b6d4)** làm accent color chính, tạo điểm nhấn hiện đại mà không quá sáng.

### 2. **Navbar Sticky & Responsive**

- Navbar dính phía trên với backdrop blur effect
- Logo mini với biểu tượng emoji
- Menu responsive (hamburger trên mobile)
- Badge thông tin kỳ thi

### 3. **Sidebar Tương tác**

- Tìm kiếm mục nhanh
- Các nhóm mục có thể mở/đóng
- Active state tự động khi scroll
- Đóng tự động trên mobile

### 4. **Thanh tiến trình Reading**

- Gradual progress bar ở đầu trang
- Hiển thị mức độ đọc page
- Cập nhật mượt mà khi scroll

### 5. **Chart Cards Tương tác**

- Lightbox khi click ảnh
- Comment box có thể chỉnh sửa
- Lazy animation khi scroll vào view
- Tooltip & hover effects

### 6. **Tab System Hiện đại**

- Smooth transition giữa các tab
- Active state rõ ràng
- Responsive overflow trên mobile

### 7. **Back to Top Button**

- Xuất hiện tự động khi scroll > 300px
- Smooth scroll animation
- Hover effects

---

## Kiến trúc CSS

### Cấu trúc tệp:

```
dist/
├── css/
│   ├── minimalist.css           ← Main theme file
│   ├── charts-minimalist.css    ← Charts specific styles
│   └── charts.css               ← Legacy compatibility
├── js/
│   ├── minimalist.js            ← Theme interactions
│   └── charts.js                ← Chart utilities
└── index.html
```

### CSS Variables (Custom Properties):

Theme sử dụng CSS variables để dễ tùy chỉnh:

```css
:root {
  --primary: #1f2937;
  --accent: #06b6d4;
  --accent-hover: #0891b2;
  --surface: #ffffff;
  --text-primary: #111827;
  --text-secondary: #6b7280;
  /* ... và nhiều cái khác */
}
```

---

## Tùy chỉnh

### 1. **Thay đổi Màu Accent**

Mở `css/minimalist.css` và thay đổi:

```css
:root {
  --accent: #06b6d4;       /* Đổi từ cyan */
  --accent-hover: #0891b2;
  --accent-light: #cffafe;
}
```

**Gợi ý:**
- Xanh lá: `#10b981`, `#047857`, `#d1fae5`
- Tím: `#8b5cf6`, `#7c3aed`, `#ede9fe`
- Cam: `#f97316`, `#ea580c`, `#ffedd5`

### 2. **Tùy chỉnh Font Size**

```css
body {
  font-size: 15px; /* Default size */
}

.section-title {
  font-size: 28px; /* Heading size */
}
```

### 3. **Điều chỉnh Spacing**

Các giá trị padding/margin chính:

```css
/* Chỉnh trong CSS */
#main-content { padding: 40px; }
.panel { padding: 28px; }
.chart-card { padding: 24px; }
```

### 4. **Dark Mode (Tùy chọn)**

Thêm CSS prefers-color-scheme:

```css
@media (prefers-color-scheme: dark) {
  :root {
    --surface: #1f2937;
    --surface-secondary: #111827;
    --text-primary: #f9fafb;
    --text-secondary: #d1d5db;
    --border: #374151;
  }
}
```

### 5. **Tùy chỉnh Radius (Border Radius)**

```css
:root {
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
}
```

---

## Hỗ trợ Trình duyệt

| Trình duyệt | Phiên bản | Hỗ trợ |
|-----------|---------|---------|
| Chrome | 90+ | ✅ Đầy đủ |
| Firefox | 88+ | ✅ Đầy đủ |
| Safari | 14+ | ✅ Đầy đủ |
| Edge | 90+ | ✅ Đầy đủ |
| IE 11 | N/A | ❌ Không hỗ trợ |

**Lưu ý:** Theme sử dụng:
- CSS Grid & Flexbox
- CSS Custom Properties
- Backdrop Filter
- IntersectionObserver API

---

## JavaScript Features

### Được bật mặc định:

1. **Sidebar Search** - Tìm kiếm nhanh các mục
2. **Active Navigation** - Cập nhật nav/sidebar khi scroll
3. **Tab System** - Chuyển đổi tab mượt mà
4. **Lightbox** - Xem ảnh phóng to
5. **Back to Top** - Nút quay lên đầu trang
6. **Comment Boxes** - Có thể chỉnh sửa nội dung
7. **Animations** - Scroll animations
8. **Responsive Menu** - Hamburger menu trên mobile

### API Functions:

```javascript
// Scroll to section
scrollToSection('sec-overview');

// Copy to clipboard
copyToClipboard('text');
```

---

## Best Practices

### 1. **Hiệu suất**
- Tải CSS minimalist.css trước (blocking)
- Load charts.css sau (non-critical)
- Images được lazy-load qua intersection observer

### 2. **Accessibility**
- Tất cả interactive elements có `aria-label`
- Keyboard navigation được hỗ trợ
- Contrast ratio ≥ 4.5:1 cho text

### 3. **Responsive Design**
- Mobile-first approach
- Breakpoints: 480px, 768px, 1024px
- Sidebar tự động đóng trên desktop

### 4. **Customization**
- Đừng thay đổi trực tiếp styles inline
- Sử dụng CSS variables để tùy chỉnh
- Tạo file override.css nếu cần bổ sung

---

## Troubleshooting

### Chart không hiển thị
- Đảm bảo `charts.css` được load
- Kiểm tra browser console cho lỗi
- Xác nhận đường dẫn file ảnh

### Sidebar không hoạt động
- Kiểm tra `minimalist.js` được load
- Xác nhận JavaScript không bị disable
- Kiểm tra browser console

### Responsive layout bị lỗi
- Clear browser cache (Ctrl+Shift+R)
- Kiểm tra viewport meta tag
- Test trên device thật hoặc DevTools

---

## Liên hệ & Support

Để báo cáo lỗi hoặc yêu cầu tính năng, vui lòng tạo issue trong repository.

---

**Last Updated:** February 2026  
**Theme Version:** 2.0 (Minimalist Modern)
