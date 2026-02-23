# 🎨 Minimalist Modern Theme - Quick Reference

## 🚀 Bắt đầu nhanh

### Các tệp chính:
```
✅ css/minimalist.css        ← Main theme (load đầu tiên)
✅ css/charts-minimalist.css ← Chart compatibility
✅ js/minimalist.js          ← All interactions
✅ index.html                ← Updated references
```

### Để xem demo:
```bash
cd /Users/trietle/mcv_project/mini_project/graduation_score_2025/dist
# Mở index.html trong browser
```

---

## 🎨 Hệ thống Màu (CSS Variables)

```css
/* Primary Colors */
--primary: #1f2937;            /* Dark slate */
--primary-light: #374151;      /* Medium */
--primary-lighter: #4b5563;    /* Light */

/* Accent Colors (Main) */
--accent: #06b6d4;             /* Cyan */
--accent-hover: #0891b2;       /* Darker cyan */
--accent-light: #cffafe;       /* Very light cyan */

/* Surface Colors */
--surface: #ffffff;            /* White */
--surface-secondary: #f9fafb;  /* Very light gray */
--surface-tertiary: #f3f4f6;   /* Light gray */

/* Text Colors */
--text-primary: #111827;       /* Near black */
--text-secondary: #6b7280;     /* Medium gray */
--text-light: #9ca3af;         /* Light gray */

/* Borders & Utilities */
--border: #e5e7eb;             /* Light border */
--border-dark: #d1d5db;        /* Darker border */
--success: #10b981;
--warning: #f59e0b;
--danger: #ef4444;
--info: #3b82f6;
```

---

## 📐 Spacing & Sizing

```css
/* Border Radius */
--radius-sm: 6px;
--radius-md: 8px;
--radius-lg: 12px;

/* Shadows */
--shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px rgba(0, 0, 0, 0.07);
--shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
--shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.15);

/* Transitions */
--transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
```

---

## 🎯 Component Cheat Sheet

### **Stat Card**
```html
<div class="stat-card">
  <div class="stat-icon blue">👥</div>
  <div class="stat-body">
    <div class="stat-value">363,000+</div>
    <div class="stat-label">Tổng số thí sinh</div>
  </div>
</div>
```
Icon colors: `blue`, `green`, `amber`, `purple`, `red`

### **Panel**
```html
<div class="panel">
  <span class="panel-badge blue">Badge Text</span>
  <div class="panel-title">Title</div>
  <p class="panel-lead">Lead paragraph</p>
  <!-- Content -->
</div>
```
Badge colors: `blue`, `green`, `yellow`, `purple`

### **Highlight Box**
```html
<div class="highlight-box">
  <p>Important text here</p>
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
  </ul>
</div>
```

### **Callout**
```html
<div class="callout">
  "Interesting insight or quote"
</div>
```

### **Chart Card**
```html
<div class="chart-card">
  <div class="chart-card-header">
    <span class="chart-card-title">📊 Title</span>
    <span class="chart-card-tag">Tag</span>
  </div>
  <div class="chart-card-body">
    <img src="path/to/chart.png" alt="Description">
    <div class="comment-box" contenteditable="true" 
         data-placeholder="Your comment..."></div>
  </div>
</div>
```

### **Tabs**
```html
<div class="tab-bar" data-target="tab-group-1">
  <button class="tab-btn" data-pane="tab-1">Tab 1</button>
  <button class="tab-btn" data-pane="tab-2">Tab 2</button>
</div>

<div id="tab-group-1">
  <div class="tab-pane" id="tab-1">Content 1</div>
  <div class="tab-pane" id="tab-2">Content 2</div>
</div>
```

### **Cluster Card**
```html
<div class="cluster-card c1">
  <div class="cc-title">🟢 Cụm 1 – Xuất sắc</div>
  <div class="cc-provinces">Description</div>
</div>
```
Classes: `c1` (green), `c2` (blue), `c3` (amber), `c4` (red)

---

## 🛠️ Tùy chỉnh

### **Đổi Accent Color:**

1. Mở `css/minimalist.css`
2. Tìm `:root { }` ở dòng ~1
3. Đổi 3 dòng này:

```css
:root {
  /* ... */
  --accent: #06b6d4;       /* Đổi từ cyan sang color khác */
  --accent-hover: #0891b2; /* Đổi hover state */
  --accent-light: #cffafe; /* Đổi light variant */
}
```

**Color Palettes để copy:**

```css
/* Xanh lá */
--accent: #10b981;
--accent-hover: #059669;
--accent-light: #d1fae5;

/* Tím */
--accent: #8b5cf6;
--accent-hover: #7c3aed;
--accent-light: #ede9fe;

/* Cam */
--accent: #f97316;
--accent-hover: #ea580c;
--accent-light: #ffedd5;

/* Hồng */
--accent: #ec4899;
--accent-hover: #db2777;
--accent-light: #fce7f3;

/* Đỏ */
--accent: #ef4444;
--accent-hover: #dc2626;
--accent-light: #fee2e2;
```

---

## 📱 Responsive Classes

```html
<!-- Hide on mobile (< 768px) -->
<div class="hide-mobile">Content</div>

<!-- Hide on desktop (> 768px) -->
<div class="hide-desktop">Content</div>

<!-- Show only on mobile -->
<div class="mobile-only">Content</div>

<!-- Show only on desktop -->
<div class="desktop-only">Content</div>
```

---

## ⚡ JavaScript API

```javascript
// Scroll to section
scrollToSection('sec-overview');

// Copy to clipboard
copyToClipboard('text to copy');

// Toggle sidebar (mobile)
document.getElementById('sidebar').classList.toggle('active');

// Manually show lightbox
document.getElementById('lightbox').classList.add('active');
```

---

## 🔍 CSS Selectors Chính

```css
#top-navbar           /* Top navigation bar */
#sidebar              /* Left sidebar */
#main-content         /* Main content area */
#back-to-top          /* Back to top button */
#lightbox             /* Image lightbox */
#read-progress        /* Reading progress bar */

.panel                /* Content panel */
.chart-card           /* Chart container */
.stat-card            /* Stat box */
.section-header       /* Section heading */
.tab-bar              /* Tab navigation */
.comment-box          /* Editable comment area */
```

---

## 🎬 Built-in Animations

```css
/* Fade in when scrolling into view */
.slide-in {
  animation: slideIn 0.4s ease-out;
}

/* Lightbox image */
@keyframes lbIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}

/* Tab pane fade */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(5px); }
  to { opacity: 1; transform: translateY(0); }
}
```

---

## 📋 Font Stack

```css
/* Sans-serif (Main) */
-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto',
'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans',
'Helvetica Neue', sans-serif;

/* Monospace (Code) */
'Fira Code', 'Courier New', monospace;
```

---

## 🌐 Browser Compatibility

```
✅ Chrome 90+
✅ Firefox 88+
✅ Safari 14+
✅ Edge 90+
❌ Internet Explorer 11 (not supported)
```

**Features used:**
- CSS Grid & Flexbox
- CSS Custom Properties
- Backdrop Filter
- Intersection Observer API
- IntersectionObserver API

---

## 📊 Responsive Grid

```css
/* Auto-fit columns (min 220px) */
display: grid;
grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
gap: 16px;
```

**Result:**
- Desktop (1400px): 6 columns
- Tablet (768px): 3 columns
- Mobile (480px): 1 column

---

## 🔧 Debugging Tips

```javascript
// Check computed CSS variables
getComputedStyle(document.documentElement)
  .getPropertyValue('--accent');

// Check active nav
document.querySelector('#nav-menu a.active');

// Test animations
document.querySelector('.chart-card').classList.add('slide-in');
```

---

## 📞 Support

- 📖 Full guide: `MINIMALIST_THEME_GUIDE.md`
- 🔄 Summary: `THEME_UPDATE_SUMMARY.md`
- 💡 Check: Browser DevTools (F12) → Console

---

**Quick Start: Open `dist/index.html` in browser! 🚀**
