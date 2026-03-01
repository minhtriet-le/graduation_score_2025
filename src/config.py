"""
config.py — Hằng số dùng chung cho toàn bộ dự án phân tích điểm thi THPT 2025.
"""

# ──────────────────────────────────────────────────────────────────────────────
# Thư mục xuất biểu đồ
# ──────────────────────────────────────────────────────────────────────────────
OUTPUT_DIR = "dist/charts"

# ──────────────────────────────────────────────────────────────────────────────
# Cột điểm số
# ──────────────────────────────────────────────────────────────────────────────
SCORE_COLS = [
    "toan", "van", "li", "hoa", "sinh", "tin_hoc",
    "cong_nghe_cong_nghiep", "cong_nghe_nong_nghiep",
    "su", "dia", "giao_duc_kinh_te_va_phap_luat",
    "ngoai_ngu", "giao_duc_cong_dan",
]

# ──────────────────────────────────────────────────────────────────────────────
# Nhãn hiển thị tiếng Việt cho từng môn thi
# ──────────────────────────────────────────────────────────────────────────────
SUBJECT_LABELS = {
    "toan":                          "Toán",
    "van":                           "Ngữ văn",
    "li":                            "Vật lí",
    "hoa":                           "Hóa học",
    "sinh":                          "Sinh học",
    "tin_hoc":                       "Tin học",
    "cong_nghe_cong_nghiep":         "Công nghệ Công nghiệp",
    "cong_nghe_nong_nghiep":         "Công nghệ Nông nghiệp",
    "su":                            "Lịch sử",
    "dia":                           "Địa lí",
    "giao_duc_kinh_te_va_phap_luat": "Giáo dục Kinh tế và Pháp luật",
    "ngoai_ngu":                     "Ngoại ngữ",
    "giao_duc_cong_dan":             "Giáo dục Công dân",
}

# ──────────────────────────────────────────────────────────────────────────────
# Nhãn tiếng Việt cho từng mã môn ngoại ngữ
# ──────────────────────────────────────────────────────────────────────────────
FOREIGN_LANG_LABELS = {
    "N1": "Tiếng Anh",
    "N2": "Tiếng Nga",
    "N3": "Tiếng Pháp",
    "N4": "Tiếng Trung",
    "N5": "Tiếng Đức",
    "N6": "Tiếng Nhật",
    "N7": "Tiếng Hàn",
}

# ──────────────────────────────────────────────────────────────────────────────
# Màu sắc & nhãn cho K-Means (k=4)
# ──────────────────────────────────────────────────────────────────────────────
CLUSTER_COLORS = ["#2ecc71", "#3498db", "#e67e22", "#e74c3c"]

CLUSTER_LABELS = {
    0: "Cụm 1 – Xuất sắc",
    1: "Cụm 2 – Khá",
    2: "Cụm 3 – Trung bình",
    3: "Cụm 4 – Yếu",
}

# ──────────────────────────────────────────────────────────────────────────────
# Bảng mã tỉnh (SBD 2 chữ số đầu → tên tỉnh)
# ──────────────────────────────────────────────────────────────────────────────
PROVINCE_CODE = {
    "Hà Nội":               "01",
    "TP. Hồ Chí Minh":      "02",
    "Hải Phòng":            "03",
    "Đà Nẵng":              "04",
    "Hà Giang":             "05",
    "Cao Bằng":             "06",
    "Lai Châu":             "07",
    "Lào Cai":              "08",
    "Tuyên Quang":          "09",
    "Lạng Sơn":             "10",
    "Bắc Kạn":              "11",
    "Thái Nguyên":          "12",
    "Yên Bái":              "13",
    "Sơn La":               "14",
    "Phú Thọ":              "15",
    "Vĩnh Phúc":            "16",
    "Quảng Ninh":           "17",
    "Bắc Giang":            "18",
    "Bắc Ninh":             "19",
    "Hải Dương":            "21",
    "Hưng Yên":             "22",
    "Hòa Bình":             "23",
    "Hà Nam":               "24",
    "Nam Định":             "25",
    "Thái Bình":            "26",
    "Ninh Bình":            "27",
    "Thanh Hóa":            "28",
    "Nghệ An":              "29",
    "Hà Tĩnh":              "30",
    "Quảng Bình":           "31",
    "Quảng Trị":            "32",
    "Thừa Thiên Huế":       "33",
    "Quảng Nam":            "34",
    "Quảng Ngãi":           "35",
    "Kon Tum":              "36",
    "Bình Định":            "37",
    "Gia Lai":              "38",
    "Phú Yên":              "39",
    "Đắk Lắk":              "40",
    "Khánh Hòa":            "41",
    "Lâm Đồng":             "42",
    "Bình Phước":           "43",
    "Bình Dương":           "44",
    "Ninh Thuận":           "45",
    "Tây Ninh":             "46",
    "Bình Thuận":           "47",
    "Đồng Nai":             "48",
    "Long An":              "49",
    "Đồng Tháp":            "50",
    "An Giang":             "51",
    "Bà Rịa - Vũng Tàu":   "52",
    "Tiền Giang":           "53",
    "Kiên Giang":           "54",
    "Cần Thơ":              "55",
    "Bến Tre":              "56",
    "Vĩnh Long":            "57",
    "Trà Vinh":             "58",
    "Sóc Trăng":            "59",
    "Bạc Liêu":             "60",
    "Cà Mau":               "61",
    "Điện Biên":            "62",
    "Đắk Nông":             "63",
    "Hậu Giang":            "64",
}

# Đảo ngược: mã → tên tỉnh
CODE_PROVINCE = {v: k for k, v in PROVINCE_CODE.items()}

# ──────────────────────────────────────────────────────────────────────────────
# Bảng sáp nhập tỉnh (tỉnh cũ → tỉnh mới sau sáp nhập)
# ──────────────────────────────────────────────────────────────────────────────
PROVINCE_NEW_PROVINCE = {
    # Tuyên Quang + Hà Giang → Tuyên Quang
    "Tuyên Quang": "Tuyên Quang",
    "Hà Giang":    "Tuyên Quang",

    # Yên Bái + Lào Cai → Lào Cai
    "Yên Bái": "Lào Cai",
    "Lào Cai": "Lào Cai",

    # Bắc Kạn + Thái Nguyên → Thái Nguyên
    "Bắc Kạn":     "Thái Nguyên",
    "Thái Nguyên": "Thái Nguyên",

    # Vĩnh Phúc + Hòa Bình + Phú Thọ → Phú Thọ
    "Vĩnh Phúc": "Phú Thọ",
    "Hòa Bình":  "Phú Thọ",
    "Phú Thọ":   "Phú Thọ",

    # Bắc Giang + Bắc Ninh → Bắc Ninh
    "Bắc Giang": "Bắc Ninh",
    "Bắc Ninh":  "Bắc Ninh",

    # Thái Bình + Hưng Yên → Hưng Yên
    "Thái Bình": "Hưng Yên",
    "Hưng Yên":  "Hưng Yên",

    # Hải Phòng + Hải Dương → Hải Phòng
    "Hải Phòng": "Hải Phòng",
    "Hải Dương": "Hải Phòng",

    # Hà Nam + Nam Định + Ninh Bình → Ninh Bình
    "Hà Nam":    "Ninh Bình",
    "Nam Định":  "Ninh Bình",
    "Ninh Bình": "Ninh Bình",

    # Quảng Bình + Quảng Trị → Quảng Trị
    "Quảng Bình": "Quảng Trị",
    "Quảng Trị":  "Quảng Trị",

    # Đà Nẵng + Quảng Nam → Đà Nẵng
    "Đà Nẵng":   "Đà Nẵng",
    "Quảng Nam": "Đà Nẵng",

    # Kon Tum + Quảng Ngãi → Quảng Ngãi
    "Kon Tum":    "Quảng Ngãi",
    "Quảng Ngãi": "Quảng Ngãi",

    # Bình Định + Gia Lai → Gia Lai
    "Bình Định": "Gia Lai",
    "Gia Lai":   "Gia Lai",

    # Ninh Thuận + Khánh Hòa → Khánh Hòa
    "Ninh Thuận": "Khánh Hòa",
    "Khánh Hòa":  "Khánh Hòa",

    # Đắk Nông + Bình Thuận + Lâm Đồng → Lâm Đồng
    "Đắk Nông":   "Lâm Đồng",
    "Bình Thuận": "Lâm Đồng",
    "Lâm Đồng":   "Lâm Đồng",

    # Phú Yên + Đắk Lắk → Đắk Lắk
    "Phú Yên": "Đắk Lắk",
    "Đắk Lắk": "Đắk Lắk",

    # TP.HCM + Bà Rịa - Vũng Tàu + Bình Dương → TP.HCM
    "TP. Hồ Chí Minh":    "TP. Hồ Chí Minh",
    "Bà Rịa - Vũng Tàu":  "TP. Hồ Chí Minh",
    "Bình Dương":          "TP. Hồ Chí Minh",

    # Bình Phước + Đồng Nai → Đồng Nai
    "Bình Phước": "Đồng Nai",
    "Đồng Nai":   "Đồng Nai",

    # Long An + Tây Ninh → Tây Ninh
    "Long An":  "Tây Ninh",
    "Tây Ninh": "Tây Ninh",

    # Cần Thơ + Sóc Trăng + Hậu Giang → Cần Thơ
    "Cần Thơ":   "Cần Thơ",
    "Sóc Trăng": "Cần Thơ",
    "Hậu Giang": "Cần Thơ",

    # Bến Tre + Trà Vinh + Vĩnh Long → Vĩnh Long
    "Bến Tre":  "Vĩnh Long",
    "Trà Vinh": "Vĩnh Long",
    "Vĩnh Long": "Vĩnh Long",

    # Tiền Giang + Đồng Tháp → Đồng Tháp
    "Tiền Giang": "Đồng Tháp",
    "Đồng Tháp":  "Đồng Tháp",

    # Bạc Liêu + Cà Mau → Cà Mau
    "Bạc Liêu": "Cà Mau",
    "Cà Mau":   "Cà Mau",

    # Kiên Giang + An Giang → An Giang
    "Kiên Giang": "An Giang",
    "An Giang":   "An Giang",

    # 11 tỉnh/thành giữ nguyên
    "Cao Bằng":       "Cao Bằng",
    "Điện Biên":      "Điện Biên",
    "Hà Tĩnh":        "Hà Tĩnh",
    "Lai Châu":       "Lai Châu",
    "Lạng Sơn":       "Lạng Sơn",
    "Nghệ An":        "Nghệ An",
    "Quảng Ninh":     "Quảng Ninh",
    "Thanh Hóa":      "Thanh Hóa",
    "Sơn La":         "Sơn La",
    "Hà Nội":         "Hà Nội",
    "Thừa Thiên Huế": "Thừa Thiên Huế",
}
