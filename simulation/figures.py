"""Figures for *M from Mystery*. Each reads the results dict and writes
one PNG.

Palette (CVD-checked in a prior validation; line styles and direct labels as
secondary encoding): amber, green, blue, warm gray; red reserved for harm.
"""
from __future__ import annotations

from fractions import Fraction as F

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK = "#1a1a1a"
GRID = "#d9d9d9"
AMBER = "#b45309"
GREEN = "#15803d"
BLUE = "#2563eb"
GRAY = "#57534e"
RED = "#b3202c"


def _style(ax) -> None:
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(INK)
    ax.tick_params(colors=INK, labelsize=9)
    ax.grid(True, color=GRID, linewidth=0.6, alpha=0.7)
    ax.set_axisbelow(True)


LABEL = {"qL": "q_L (3,2)", "dbarR": "dbar (3,1)", "ubarR": "ubar (3,1)",
         "lL": "l_L (1,2)", "ebarR": "ebar (1,1)", "nbarR": "nubar (1,1)"}


def plot_generation(res: dict, path: str) -> None:
    gen = res["generation"]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.2, 3.9))
    # left: the ledger: hypercharge by multiplet, marker area = states
    ms = gen["multiplets"]
    xs = np.arange(len(ms))
    ys = [float(F(m["hypercharge"])) for m in ms]
    sizes = [70 * m["states"] for m in ms]
    colors = [BLUE if m["su3"] == 3 else GREEN for m in ms]
    ax1.scatter(xs, ys, s=sizes, c=colors, alpha=0.85, edgecolors=INK,
                linewidths=0.6, zorder=3)
    for x, m in zip(xs, ms):
        ax1.annotate(f"Y = {m['hypercharge']}",
                     (x, float(F(m["hypercharge"]))), fontsize=7.5,
                     color=INK, xytext=(0, 12), textcoords="offset points",
                     ha="center")
    ax1.axhline(0, color=INK, lw=0.8)
    ax1.set_xticks(xs)
    ax1.set_xticklabels([LABEL[m["name"]] for m in ms], fontsize=8)
    ax1.set_ylabel("hypercharge", fontsize=9)
    ax1.set_ylim(-1.0, 1.35)
    ax1.set_title("one generation: 16 Weyl states in six multiplets, "
                  "with hypercharges", fontsize=9.5, color=INK)
    ax1.annotate("blue: color triplets\ngreen: color singlets\narea: states",
                 (0.02, 0.03), xycoords="axes fraction", fontsize=7.5,
                 color=GRAY)
    _style(ax1)
    # right: deletion rigidity
    names = [m["name"] for m in ms]
    broken = [len(gen["deletion_breaks"][n]) for n in names]
    cols = [RED if b else GREEN for b in broken]
    ax2.bar(range(len(names)), broken, color=cols, width=0.6)
    for i, b in enumerate(broken):
        ax2.annotate(str(b), (i, b), fontsize=9, ha="center", va="bottom",
                     color=INK, xytext=(0, 2), textcoords="offset points")
    ax2.set_xticks(range(len(names)))
    ax2.set_xticklabels([LABEL[n] for n in names], fontsize=8)
    ax2.set_ylabel("consistency conditions broken if deleted", fontsize=9)
    ax2.set_title("conditions broken by deleting each multiplet",
                  fontsize=9.5, color=INK)
    ax2.annotate("right-handed neutrino:\nno condition broken", (5.4, 2.7), fontsize=7.5,
                 color=GREEN, ha="right")
    _style(ax2)
    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def plot_forms(res: dict, path: str) -> None:
    glob = res["global_forms"]
    fig, axes = plt.subplots(1, 4, figsize=(11.6, 3.2))
    titles = {"1": "Gamma = 1", "Z2": "Gamma = Z2", "Z3": "Gamma = Z3",
              "Z6": "Gamma = Z6"}
    for ax, name in zip(axes, ["1", "Z2", "Z3", "Z6"]):
        lat = glob["lattices"][name]
        E, M = set(lat["electric"]), set(lat["magnetic"])
        for e in range(6):
            for m in range(6):
                ok = e in E and m in M
                ax.scatter([e], [m], s=52 if ok else 14,
                           c=BLUE if ok else GRID,
                           edgecolors=INK if ok else "none",
                           linewidths=0.5, zorder=3)
        ax.set_xticks(range(6))
        ax.set_yticks(range(6))
        ax.set_xlabel("electric class", fontsize=8.5)
        if name == "1":
            ax.set_ylabel("magnetic class", fontsize=8.5)
        f = glob["forms"][name]
        ax.set_title(f"{titles[name]}\n{f['electric_one_form_order']} electric x "
                     f"{f['magnetic_one_form_order']} magnetic", fontsize=9,
                     color=INK)
        _style(ax)
    fig.suptitle("line lattices of the four global forms "
                 "of the Standard Model gauge group", fontsize=10,
                 color=INK, y=1.03)
    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def plot_atomos(res: dict, path: str) -> None:
    sl2 = res["sl2z"]
    fus = res["fusion"]
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(11.6, 3.6),
                                        gridspec_kw={"width_ratios": [1.15, 0.9, 1]})
    # left: the SL(2,Z) orbit of (1,0) in a small window
    import math
    N = 12
    for p in range(-N, N + 1):
        for q in range(-N, N + 1):
            if (p, q) == (0, 0):
                continue
            prim = math.gcd(p, q) == 1
            ax1.scatter([p], [q], s=13 if prim else 5,
                        c=GREEN if prim else GRID, zorder=3)
    ax1.scatter([1], [0], s=60, c=RED, edgecolors=INK, linewidths=0.6,
                zorder=4)
    ax1.annotate("(1, 0)", (1, 0), fontsize=8, color=RED, xytext=(6, 6),
                 textcoords="offset points")
    ax1.set_xlabel("electric charge p", fontsize=9)
    ax1.set_ylabel("magnetic charge q", fontsize=9)
    ax1.set_title(f"SL(2,Z) orbit of the unit electric charge:\n"
                  f"primitive vectors, density {sl2['primitive_density']:.3f} "
                  f"(6/pi^2 = {sl2['six_over_pi_squared']:.4f})",
                  fontsize=9, color=INK)
    _style(ax1)
    # middle: the proton toy
    labels = ["1", "8", "8'", "10"]
    dims = [1, 8, 8, 10]
    cols = [RED, GRAY, GRAY, GRAY]
    ax2.bar(range(4), dims, color=cols, width=0.6)
    for i, d in enumerate(dims):
        ax2.annotate(str(d), (i, d), fontsize=8.5, ha="center", va="bottom",
                     color=INK, xytext=(0, 2), textcoords="offset points")
    ax2.set_xticks(range(4))
    ax2.set_xticklabels(labels, fontsize=9)
    ax2.set_ylabel("dimension", fontsize=9)
    ax2.set_title("SU(3): 3 x 3 x 3 = 1 + 8 + 8 + 10", fontsize=9, color=INK)
    ax2.annotate("the proton\nchannel", (0, 1.6), fontsize=8, color=RED,
                 ha="center")
    _style(ax2)
    # right: SU(2) fusion: prime and composite at once
    ns = list(range(2, fus["su2_max_dim"] + 1))
    ax3.scatter(ns, [1] * len(ns), s=60, c=GREEN, marker="o",
                edgecolors=INK, linewidths=0.5, zorder=3,
                label="tensor-prime (no factorization)")
    ax3.scatter(ns, [0] * len(ns), s=60, c=RED, marker="s",
                edgecolors=INK, linewidths=0.5, zorder=3,
                label="summand of a product of smaller spins")
    ax3.set_yticks([0, 1])
    ax3.set_yticklabels(["composite\nas summand", "prime\nas factor"],
                        fontsize=8)
    ax3.set_xticks(ns)
    ax3.set_xlabel("SU(2) irreducible, by dimension", fontsize=9)
    ax3.set_ylim(-0.7, 1.7)
    ax3.set_title("SU(2) fusion: tensor factorizations\n"
                  "and summand occurrences by spin", fontsize=9,
                  color=INK)
    _style(ax3)
    fig.tight_layout()
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
