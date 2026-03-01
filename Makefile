# ──────────────────────────────────────────────────────────────────────────────
# Makefile — graduation_score_2025
# Yêu cầu: Python venv tại .venv/ và đã cài requirements.txt
# ──────────────────────────────────────────────────────────────────────────────

PYTHON   := .venv/bin/python
NB_DIR   := notebooks
NB_FLAGS := --to notebook --execute --inplace --ExecutePreprocessor.timeout=600

.PHONY: help install etl analysis build all clean

help:
	@echo ""
	@echo "  make install    — Cài toàn bộ dependencies vào .venv/"
	@echo "  make etl        — Chạy ETL: Excel → Parquet + thêm cột tỉnh"
	@echo "  make analysis   — Chạy EDA + Clustering + Hypothesis"
	@echo "  make build      — Chạy toàn bộ analysis (không ETL)"
	@echo "  make all        — ETL + build"
	@echo "  make clean      — Xoá chart đã xuất"
	@echo ""

install:
	python3 -m venv .venv
	$(PYTHON) -m pip install --upgrade pip -q
	$(PYTHON) -m pip install -r requirements.txt -q
	@echo "✅ Dependencies installed."

etl:
	$(PYTHON) -m nbconvert $(NB_FLAGS) $(NB_DIR)/01_etl.ipynb
	@echo "✅ ETL complete."

analysis:
	$(PYTHON) -m nbconvert $(NB_FLAGS) $(NB_DIR)/02_eda.ipynb
	$(PYTHON) -m nbconvert $(NB_FLAGS) $(NB_DIR)/03_clustering.ipynb
	$(PYTHON) -m nbconvert $(NB_FLAGS) $(NB_DIR)/04_hypothesis.ipynb
	@echo "✅ Analysis complete."

build: analysis
	@echo "✅ Build complete — charts saved to dist/charts/"

all: etl build

clean:
	rm -f dist/charts/*.png
	@echo "🗑  Charts cleared."
