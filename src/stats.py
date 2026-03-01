"""
stats.py — Hàm kiểm định thống kê dùng chung.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats as scipy_stats
import os

from src.config import OUTPUT_DIR


def compare_two_groups(
    df,
    subject_col: str,
    subject_label: str,
    group_a: str,
    group_b: str,
    group_col: str = "tinh",
    alpha: float = 0.05,
    output_dir: str = OUTPUT_DIR,
) -> dict:
    """
    So sánh điểm hai nhóm (tỉnh) bằng:
      - Levene's test (kiểm tra phương sai)
      - Welch's / Student's t-test (two-sided)
      - Cohen's d (effect size)
      - Mann-Whitney U test (phi tham số)
    Vẽ histogram + box plot so sánh và lưu PNG.

    Args:
        df:            DataFrame đã load từ Parquet.
        subject_col:   Tên cột điểm (vd: 'toan').
        subject_label: Tên hiển thị (vd: 'Toán').
        group_a:       Giá trị nhóm A trong group_col (vd: 'Quảng Nam').
        group_b:       Giá trị nhóm B trong group_col (vd: 'Đà Nẵng').
        group_col:     Cột phân nhóm (mặc định 'tinh').
        alpha:         Mức ý nghĩa (mặc định 0.05).
        output_dir:    Thư mục lưu ảnh.

    Returns:
        dict chứa các giá trị thống kê chính.
    """
    os.makedirs(output_dir, exist_ok=True)

    scores_a = df[df[group_col] == group_a][subject_col].dropna().values
    scores_b = df[df[group_col] == group_b][subject_col].dropna().values

    n_a, n_b     = len(scores_a), len(scores_b)
    mean_a, mean_b = scores_a.mean(), scores_b.mean()
    std_a,  std_b  = scores_a.std(ddof=1), scores_b.std(ddof=1)

    print("=" * 60)
    print(f"  So sánh điểm {subject_label}: {group_a} vs {group_b}")
    print("=" * 60)
    print(f"  {'Nhóm':<22} {'n':>8} {'Mean':>9} {'Std':>9}")
    print(f"  {'-'*48}")
    print(f"  {group_a:<22} {n_a:>8,} {mean_a:>9.4f} {std_a:>9.4f}")
    print(f"  {group_b:<22} {n_b:>8,} {mean_b:>9.4f} {std_b:>9.4f}")
    print(f"  {'Chênh lệch ĐTB':<22} {'':>8} {abs(mean_a - mean_b):>9.4f}")

    # Levene's test
    lev_stat, lev_p = scipy_stats.levene(scores_a, scores_b)
    equal_var        = lev_p > alpha
    print(f"\n── Levene's test (phương sai đồng nhất)")
    print(f"   Statistic = {lev_stat:.4f},  p-value = {lev_p:.4e}")
    print(f"   → {'Phương sai BẰNG NHAU (p > 0.05)' if equal_var else 'Phương sai KHÁC NHAU (p ≤ 0.05)'}")

    # Welch's / Student's t-test
    t_stat, t_p = scipy_stats.ttest_ind(scores_a, scores_b, equal_var=equal_var)
    test_name   = "Student" if equal_var else "Welch"
    print(f"\n── {test_name}'s t-test (H₀: μ₁ = μ₂, hai phía)")
    print(f"   t-statistic = {t_stat:.4f},  p-value = {t_p:.4e}")
    reject = t_p < alpha
    print(f"   → {'BÁC BỎ H₀' if reject else 'KHÔNG đủ bằng chứng bác bỏ H₀'} (α = {alpha})")
    if reject:
        winner = group_a if mean_a > mean_b else group_b
        print(f"   → {winner} có ĐTB {subject_label} cao hơn (có ý nghĩa thống kê).")

    # Cohen's d
    pooled_std = np.sqrt(
        ((n_a - 1) * std_a**2 + (n_b - 1) * std_b**2) / (n_a + n_b - 2)
    )
    cohens_d  = (mean_a - mean_b) / pooled_std
    magnitude = (
        "nhỏ (small)"   if abs(cohens_d) < 0.2 else
        "nhỏ-vừa"       if abs(cohens_d) < 0.5 else
        "vừa (medium)"  if abs(cohens_d) < 0.8 else
        "lớn (large)"
    )
    print(f"\n── Effect size: Cohen's d = {cohens_d:.4f}  →  {magnitude}")

    # Mann-Whitney U
    u_stat, u_p = scipy_stats.mannwhitneyu(scores_a, scores_b, alternative="two-sided")
    print(f"\n── Mann-Whitney U test (phi tham số)")
    print(f"   U = {u_stat:.0f},  p-value = {u_p:.4e}")
    print(f"   → {'BÁC BỎ H₀' if u_p < alpha else 'KHÔNG đủ bằng chứng bác bỏ H₀'} (α = {alpha})")

    # ── Biểu đồ so sánh ──────────────────────────────────────────────────────
    bins    = np.arange(0, 10.5, 0.5)
    color_a = "#3498db"
    color_b = "#e74c3c"

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Histogram
    axes[0].hist(scores_a, bins=bins, alpha=0.6, color=color_a, density=True,
                 label=f"{group_a} (n={n_a:,}, μ={mean_a:.3f})")
    axes[0].hist(scores_b, bins=bins, alpha=0.6, color=color_b, density=True,
                 label=f"{group_b} (n={n_b:,}, μ={mean_b:.3f})")
    axes[0].axvline(mean_a, color=color_a, linestyle="--", linewidth=1.8)
    axes[0].axvline(mean_b, color=color_b, linestyle="--", linewidth=1.8)
    axes[0].set_title(f"Phân bố điểm {subject_label} (normalized)",
                      fontsize=13, fontweight="bold")
    axes[0].set_xlabel(f"Điểm {subject_label}")
    axes[0].set_ylabel("Mật độ")
    axes[0].legend(fontsize=11)
    sns.despine(ax=axes[0])

    # Box plot
    data_box   = [scores_a, scores_b]
    labels_box = [group_a, group_b]
    bp = axes[1].boxplot(
        data_box, labels=labels_box, patch_artist=True,
        medianprops=dict(color="black", linewidth=2), widths=0.5,
    )
    for patch, color in zip(bp["boxes"], [color_a, color_b]):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    for i, (sc, color) in enumerate(zip(data_box, [color_a, color_b]), start=1):
        axes[1].scatter(i, sc.mean(), marker="D", color=color, s=60, zorder=5,
                        label=f"Mean {labels_box[i-1]}: {sc.mean():.3f}")

    sig_label = "***" if t_p < 0.001 else "**" if t_p < 0.01 else "*" if t_p < alpha else "ns"
    sig_text  = f"{test_name}'s t-test\np = {t_p:.2e}\n{sig_label}"
    axes[1].text(0.97, 0.97, sig_text, transform=axes[1].transAxes,
                 ha="right", va="top", fontsize=11,
                 bbox=dict(facecolor="white", edgecolor="gray", alpha=0.85))
    axes[1].set_title(f"Box plot điểm {subject_label}", fontsize=13, fontweight="bold")
    axes[1].set_ylabel(f"Điểm {subject_label}")
    axes[1].legend(fontsize=10, loc="lower right")
    sns.despine(ax=axes[1])

    plt.suptitle(f"So sánh điểm {subject_label}: {group_a} vs {group_b}",
                 fontsize=14, fontweight="bold", y=1.02)
    plt.tight_layout()

    safe_a    = group_a.replace(" ", "_").replace(".", "")
    safe_b    = group_b.replace(" ", "_").replace(".", "")
    save_path = os.path.join(output_dir, f"hypothesis_{subject_col}_{safe_a}_{safe_b}.png")
    plt.savefig(save_path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"\nSaved: {os.path.basename(save_path)}")

    return {
        "group_a": group_a, "group_b": group_b,
        "n_a": n_a, "n_b": n_b,
        "mean_a": mean_a, "mean_b": mean_b,
        "std_a": std_a, "std_b": std_b,
        "levene_p": lev_p, "equal_var": equal_var,
        "t_stat": t_stat, "t_p": t_p,
        "cohens_d": cohens_d,
        "u_stat": u_stat, "u_p": u_p,
        "reject_h0": reject,
    }
