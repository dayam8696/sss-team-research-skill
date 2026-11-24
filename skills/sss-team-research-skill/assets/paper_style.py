"""Publication style and SSS house chart helpers for matplotlib.

Usage:
    import sys; sys.path.insert(0, "<path to this assets folder>")
    from paper_style import apply, save, faceted_bars, trend_dual_axis, lollipop, COL_W, PAGE_W
    apply()
    fig = trend_dual_axis(years, articles, mean_tc_article, mean_tc_year, partial_last=True)
    save(fig, "fig2_trend")   # writes fig2_trend.pdf and fig2_trend.png (300 dpi)

Every helper takes the user's real numbers. Never pass invented values.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

# Okabe-Ito: colour-blind safe
OKABE_ITO = ["#0072B2", "#E69F00", "#009E73", "#D55E00", "#CC79A7", "#56B4E9", "#F0E442", "#000000"]
# Sequential house blues/greens used for model series in SSS results figures
SERIES = ["#3B4CC0", "#2A9D8F", "#7AC74F", "#E9C46A", "#E76F51", "#8E44AD"]
COL_W = 3.5   # single-column width, inches
PAGE_W = 7.0  # full-page width, inches


def apply(font_size=9):
    mpl.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": font_size,
        "axes.titlesize": font_size,
        "axes.titleweight": "bold",
        "axes.labelsize": font_size,
        "xtick.labelsize": font_size - 1,
        "ytick.labelsize": font_size - 1,
        "legend.fontsize": font_size - 1,
        "legend.frameon": True,
        "legend.framealpha": 0.9,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.prop_cycle": mpl.cycler(color=SERIES),
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.alpha": 0.3,
        "grid.linewidth": 0.5,
        "lines.linewidth": 1.5,
        "pdf.fonttype": 42,  # embed TrueType so journals accept the PDF
        "ps.fonttype": 42,
        "savefig.bbox": "tight",
        "savefig.dpi": 300,
    })


def save(fig, stem):
    for ext in ("pdf", "png"):
        fig.savefig(f"{stem}.{ext}")
    plt.close(fig)
    return [f"{stem}.pdf", f"{stem}.png"]


def faceted_bars(data, facets, groups, series, ylabel, errors=None, ylim=None, width=PAGE_W, height=2.6):
    """One panel per facet (e.g. dataset), x = groups (e.g. pipelines), one bar per series (e.g. LLM).

    data[facet][series] -> list of values aligned with `groups`; errors has the same shape (SD/CI) or None.
    """
    fig, axes = plt.subplots(1, len(facets), figsize=(width, height), sharey=True, squeeze=False)
    n = len(series)
    bw = 0.8 / n
    for ax, f in zip(axes[0], facets):
        for i, s in enumerate(series):
            xs = [g + (i - (n - 1) / 2) * bw for g in range(len(groups))]
            err = errors[f][s] if errors else None
            ax.bar(xs, data[f][s], bw, yerr=err, capsize=2 if err else 0, label=s, color=SERIES[i % len(SERIES)])
        ax.set_title(f"Dataset: {f}" if not str(f).lower().startswith("dataset") else str(f))
        ax.set_xticks(range(len(groups)))
        ax.set_xticklabels(groups, rotation=30, ha="right")
        if ylim:
            ax.set_ylim(*ylim)
    axes[0][0].set_ylabel(ylabel)
    axes[0][0].legend(title="Model", loc="upper right")
    fig.tight_layout()
    return fig


def trend_dual_axis(years, articles, mean_tc_article=None, mean_tc_year=None, partial_last=False, width=PAGE_W, height=3.0):
    """Bibliometric publication & citation trend: bars (articles, left) + citation lines (right), value labels."""
    fig, ax = plt.subplots(figsize=(width, height))
    colors = ["#5DADE2"] * len(years)
    for i, v in enumerate(articles):  # darker bars for the high-output years
        if v >= 0.5 * max(articles):
            colors[i] = "#1F618D"
    bars = ax.bar([str(y) for y in years], articles, color=colors, label="Articles (N), left axis", zorder=2)
    if partial_last:
        bars[-1].set_alpha(0.55)
        bars[-1].set_hatch("//")
        ax.annotate("partial year", (len(years) - 1, articles[-1]), textcoords="offset points", xytext=(0, 14), ha="center", fontsize=7, style="italic")
    for b, v in zip(bars, articles):
        ax.annotate(f"{v}", (b.get_x() + b.get_width() / 2, v), textcoords="offset points", xytext=(0, 2), ha="center", fontsize=7, fontweight="bold")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of articles", color="#1F618D")
    handles, labels = ax.get_legend_handles_labels()
    if mean_tc_article is not None or mean_tc_year is not None:
        ax2 = ax.twinx()
        ax2.grid(False)
        ax2.spines["right"].set_visible(True)
        for vals, lab, col, ls in ((mean_tc_article, "Mean TC/article, right axis", "#C0392B", "-"),
                                   (mean_tc_year, "Mean TC/year, right axis", "#D68910", "--")):
            if vals is None:
                continue
            (ln,) = ax2.plot([str(y) for y in years], vals, ls, marker="o", mfc="white", color=col, label=lab, zorder=3)
            for x, v in zip([str(y) for y in years], vals):
                ax2.annotate(f"{v:.2f}", (x, v), textcoords="offset points", xytext=(0, 5), ha="center", fontsize=6, color=col)
            handles.append(ln)
            labels.append(lab)
        ax2.set_ylabel("Citations (mean)", color="#C0392B")
    ax.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 1.12), ncol=3, frameon=False)
    fig.tight_layout()
    return fig


def lollipop(labels, values, xlabel="Number of articles", width=COL_W, height=None, max_label=40):
    """Top-N lollipop chart (sources, countries), largest at the top, value printed at the dot."""
    order = sorted(zip(values, labels))
    vals, labs = [v for v, _ in order], [lab if len(lab) <= max_label else lab[: max_label - 1] + "…" for _, lab in order]
    fig, ax = plt.subplots(figsize=(width, height or 0.22 * len(vals) + 0.6))
    ax.hlines(range(len(vals)), 0, vals, color="#85C1E9", linewidth=1.5)
    ax.plot(vals, range(len(vals)), "o", color="#1F618D", markersize=6)
    for i, v in enumerate(vals):
        ax.annotate(f"{v}", (v, i), textcoords="offset points", xytext=(6, -3), fontsize=7)
    ax.set_yticks(range(len(vals)))
    ax.set_yticklabels([s.upper() for s in labs], fontsize=6)
    ax.set_xlabel(xlabel)
    ax.grid(axis="y", visible=False)
    fig.tight_layout()
    return fig
