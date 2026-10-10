#!/usr/bin/env python3
"""
LEVEL 100 ADVERSARIAL STREAM PROCESSING BENCHMARK GENERATOR (v3 - Optimized Spacing)
Authentic Apache Flink Distributed Stream Architecture:
- Two-Input Channel Watermark Alignment: min(WM_P0, WM_P1)
- Non-Planar Bridge Jump Routing
- Half-Open Sliding Windows [Size=6s, Slide=3s]
- Precision Event-Time Coordinates:
  P0: A1(2s, K1, V=22), A4(7s, K1, V=28), A2(9s, K2, V=35), A3(12s, K1, V=14)
  P1: B1(3s, K2, V=25), B3(5.5s, K1, V=20), B2(10s, K1, V=32), B4(13s, K2, V=40)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

def render_level100_diagram(output_path=None):
    if output_path is None:
        output_path = os.path.normpath(os.path.abspath("assets/level100_stream_dag.png"))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    ax.set_xlim(0, 160)
    ax.set_ylim(0, 90)
    ax.axis("off")
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")

    # Header
    ax.text(80, 86.8, "DISTRIBUTED STREAM PROCESSING TOPOLOGY: INGESTION WAVEFORMS & SLIDING WINDOWS", 
            fontsize=12.5, weight="bold", ha="center", va="center", color="#0f172a", fontfamily="sans-serif")
    ax.text(80, 84.1, "Apache Flink Distributed Streaming Execution Graph | Two-Channel Watermark Alignment", 
            fontsize=9.0, style="italic", ha="center", va="center", color="#475569")
    ax.plot([8, 152], [82.5, 82.5], color="#cbd5e1", lw=1.2)

    # -------------------------------------------------------------
    # STAGE 1: INGESTION TIMELINE WAVEFORMS (Left: x=6 to x=64)
    # -------------------------------------------------------------
    stage1_rect = FancyBboxPatch((6, 12), 58, 67, boxstyle="round,pad=0.8,rounding_size=2.0",
                                 facecolor="#f8fafc", edgecolor="#94a3b8", lw=1.5, linestyle="--")
    ax.add_patch(stage1_rect)
    ax.text(35, 76.2, "STAGE 1: PARTITIONED INGESTION WAVEFORMS", fontsize=9.2, weight="bold", color="#1e293b", ha="center")
    ax.text(35, 73.8, "Event-Time Waveforms (Arrival Cycles: T1 -> T4)", fontsize=7.5, color="#64748b", ha="center")

    # Time Axis Parameters: t from 0 to 14 mapped to x from 12 to 60
    t_min, t_max = 0, 14
    x_t0, x_t14 = 12, 60
    def t_to_x(t):
        return x_t0 + (t - t_min) / (t_max - t_min) * (x_t14 - x_t0)

    # Partition P0 Container (Top)
    p0_box = FancyBboxPatch((8, 45.5), 54, 25, boxstyle="round,pad=0.5,rounding_size=1.2",
                            facecolor="#eff6ff", edgecolor="#3b82f6", lw=1.5)
    ax.add_patch(p0_box)
    ax.text(10, 68.2, "Partition P0 (Stream A)", fontsize=8.8, weight="bold", color="#1d4ed8")

    # Partition P1 Container (Bottom)
    p1_box = FancyBboxPatch((8, 15), 54, 25, boxstyle="round,pad=0.5,rounding_size=1.2",
                            facecolor="#f0fdf4", edgecolor="#22c55e", lw=1.5)
    ax.add_patch(p1_box)
    ax.text(10, 37.7, "Partition P1 (Stream B)", fontsize=8.8, weight="bold", color="#15803d")

    # Draw Time Grids and Axes for P0 and P1
    for y_axis in [48.5, 18.0]:
        ax.plot([x_t0, x_t14], [y_axis, y_axis], color="#64748b", lw=1.2)
        for t in range(0, 15):
            xt = t_to_x(t)
            is_major = (t % 2 == 0)
            tick_h = 1.3 if is_major else 0.7
            ax.plot([xt, xt], [y_axis - tick_h, y_axis], color="#64748b", lw=1.0 if is_major else 0.6)
            if is_major:
                ax.text(xt, y_axis - 2.5, f"{t}s", fontsize=6.2, ha="center", va="top", color="#475569", fontfamily="monospace")
            ax.plot([xt, xt], [y_axis, y_axis + 16.5], color="#e2e8f0", lw=0.45, linestyle=":")

    # Partition 0 packets: t = 2, 7, 9, 12
    p0_packets = [
        (2.0, "A1", "K1", 22, "T1", "#dbeafe", "#1e40af"),
        (7.0, "A4", "K1", 28, "T4", "#dbeafe", "#1e40af"),
        (9.0, "A2", "K2", 35, "T2", "#fee2e2", "#991b1b"),
        (12.0, "A3", "K1", 14, "T3", "#dbeafe", "#1e40af")
    ]
    for t, pid, key, val, cycle, bg_c, fg_c in p0_packets:
        xt = t_to_x(t)
        ax.plot([xt, xt], [48.5, 52.5], color=fg_c, lw=1.5)
        pkt = FancyBboxPatch((xt - 2.2, 52.5), 4.4, 11.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                             facecolor=bg_c, edgecolor=fg_c, lw=1.2)
        ax.add_patch(pkt)
        ax.text(xt, 61.8, f"[{cycle}] {pid}", fontsize=5.6, weight="bold", color="#475569", ha="center")
        ax.text(xt, 58.6, f"Key: {key}", fontsize=6.6, weight="bold", color=fg_c, ha="center")
        ax.text(xt, 55.6, f"V = {val}", fontsize=7.0, weight="bold", color="#0f172a", ha="center")
        ax.text(xt, 53.3, f"t = {t:g}s", fontsize=5.8, color="#475569", ha="center", fontfamily="monospace")

    # Partition 1 packets: t = 3, 5.5, 10, 13
    p1_packets = [
        (3.0, "B1", "K2", 25, "T1", "#fee2e2", "#991b1b"),
        (5.5, "B3", "K1", 16, "T3", "#dbeafe", "#1e40af"),
        (10.0, "B2", "K1", 32, "T2", "#dbeafe", "#1e40af"),
        (13.0, "B4", "K2", 40, "T4", "#fee2e2", "#991b1b")
    ]
    for t, pid, key, val, cycle, bg_c, fg_c in p1_packets:
        xt = t_to_x(t)
        # Minor tick indicator for 5.5s
        if t == 5.5:
            ax.plot([xt, xt], [18.0 - 0.9, 18.0], color="#22c55e", lw=0.9)
            ax.text(xt, 18.0 - 2.5, "5.5s", fontsize=5.2, ha="center", va="top", color="#15803d", fontfamily="monospace")
        ax.plot([xt, xt], [18.0, 22.0], color=fg_c, lw=1.5)
        pkt = FancyBboxPatch((xt - 2.2, 22.0), 4.4, 11.5, boxstyle="round,pad=0.2,rounding_size=0.6",
                             facecolor=bg_c, edgecolor=fg_c, lw=1.2)
        ax.add_patch(pkt)
        ax.text(xt, 31.3, f"[{cycle}] {pid}", fontsize=5.6, weight="bold", color="#475569", ha="center")
        ax.text(xt, 28.1, f"Key: {key}", fontsize=6.6, weight="bold", color=fg_c, ha="center")
        ax.text(xt, 25.1, f"V = {val}", fontsize=7.0, weight="bold", color="#0f172a", ha="center")
        ax.text(xt, 22.8, f"t = {t:g}s", fontsize=5.8, color="#475569", ha="center", fontfamily="monospace")

    # -------------------------------------------------------------
    # STAGE 2: WATERMARK OPERATOR (Center-Left: x=68 to x=90)
    # -------------------------------------------------------------
    wm_rect = FancyBboxPatch((68, 12), 22, 67, boxstyle="round,pad=0.8,rounding_size=2.0",
                             facecolor="#fefce8", edgecolor="#eab308", lw=1.5, linestyle="--")
    ax.add_patch(wm_rect)
    ax.text(79, 76.2, "STAGE 2: WATERMARK", fontsize=9.0, weight="bold", color="#854d0e", ha="center")
    ax.text(79, 73.8, "Watermark Generator", fontsize=7.5, style="italic", color="#a16207", ha="center")

    wm_card = FancyBboxPatch((69.5, 30), 19.0, 39, boxstyle="round,pad=0.4,rounding_size=1.0",
                            facecolor="#ffffff", edgecolor="#facc15", lw=1.2)
    ax.add_patch(wm_card)
    ax.text(79, 66.0, "WatermarkStrategy", fontsize=7.8, weight="bold", color="#854d0e", ha="center")
    ax.plot([71, 87], [64.5, 64.5], color="#fde047", lw=0.8)

    ax.text(71.0, 61.2, "Type:", fontsize=6.8, weight="bold", color="#475569")
    ax.text(71.0, 58.8, "BoundedOutOfOrderness", fontsize=6.4, color="#0f172a", fontfamily="monospace")
    
    ax.text(71.0, 54.8, "Bounded Lag (delta_t):", fontsize=6.8, weight="bold", color="#475569")
    ax.text(71.0, 52.4, "4.000 s", fontsize=7.8, weight="bold", color="#b45309", fontfamily="monospace")
    
    ax.text(71.0, 48.4, "Allowed Lateness:", fontsize=6.8, weight="bold", color="#475569")
    ax.text(71.0, 46.0, "0.000 s (Strict)", fontsize=7.2, weight="bold", color="#dc2626", fontfamily="monospace")
    
    ax.text(71.0, 42.0, "Multi-Input Alignment:", fontsize=6.8, weight="bold", color="#475569")
    ax.text(71.0, 39.4, "Two-Channel Minimum", fontsize=6.6, weight="bold", color="#1e293b", fontfamily="monospace")
    ax.text(71.0, 37.0, "WM = min(WM_P0, WM_P1)", fontsize=6.3, style="italic", color="#2563eb", fontfamily="monospace")
    
    ax.text(71.0, 33.2, "Channel Watermark:", fontsize=6.6, weight="bold", color="#475569")
    ax.text(71.0, 31.0, "WM_p = max(t_p) - delta_t", fontsize=6.1, color="#334155", fontfamily="monospace")

    # Connect Stage 1 to Stage 2
    ax.annotate("", xy=(68, 58), xytext=(62, 58), arrowprops=dict(arrowstyle="->", lw=1.5, color="#64748b"))
    ax.annotate("", xy=(68, 27), xytext=(62, 27), arrowprops=dict(arrowstyle="->", lw=1.5, color="#64748b"))

    # -------------------------------------------------------------
    # STAGE 3: NON-PLANAR CROSSBAR ROUTING (Center: x=90 to x=118)
    # -------------------------------------------------------------
    filter_box = FancyBboxPatch((98, 54), 14, 8, boxstyle="round,pad=0.4,rounding_size=1.0",
                                facecolor="#f3e8ff", edgecolor="#9333ea", lw=1.5)
    ax.add_patch(filter_box)
    ax.text(105, 59.5, "PREDICATE FILTER", fontsize=7.0, weight="bold", color="#6b21a8", ha="center")
    ax.text(105, 56.5, "Condition: Value >= 20", fontsize=6.6, weight="bold", color="#581c87", ha="center")

    # Exit coordinates from Stage 2: P0 at (90, 58), P1 at (90, 27)
    # P0[K1] (Blue) -> Filter -> Worker 1 (118, 58)
    ax.plot([90, 98], [58, 58], color="#2563eb", lw=2.0)
    ax.plot([112, 118], [58, 58], color="#2563eb", lw=2.0)
    ax.scatter([92], [58], color="#2563eb", s=30, zorder=5)
    ax.text(92.8, 60.0, "K1", fontsize=7.0, weight="bold", color="#1d4ed8")

    # P0[K2] (Red) -> Crosses down to Worker 2 (118, 27)
    ax.plot([92, 95, 112, 118], [58, 58, 27, 27], color="#dc2626", lw=1.8)
    ax.text(93.0, 53.0, "K2", fontsize=7.0, weight="bold", color="#b91c1c")

    # P1[K2] (Red) -> Straight to Worker 2
    ax.plot([90, 118], [27, 27], color="#dc2626", lw=2.0)
    ax.scatter([92], [27], color="#dc2626", s=30, zorder=5)
    ax.text(92.8, 24.5, "K2", fontsize=7.0, weight="bold", color="#b91c1c")

    # P1[K1] (Blue) -> Crosses up to Worker 1 via Bridge Jump
    ax.scatter([94], [27], color="#2563eb", s=30, zorder=5)
    ax.text(94.5, 30.2, "K1", fontsize=7.0, weight="bold", color="#1d4ed8")

    ax.plot([94, 101.5], [27, 41.0], color="#2563eb", lw=2.0)
    arc = patches.Arc((102.8, 42.6), 3.2, 3.2, angle=50, theta1=0, theta2=180, color="#2563eb", lw=2.0)
    ax.add_patch(arc)
    ax.plot([104.1, 114], [44.2, 58], color="#2563eb", lw=2.0)
    ax.scatter([114], [58], color="#2563eb", s=35, zorder=5)

    # -------------------------------------------------------------
    # STAGE 4: WORKER 1 SLIDING WINDOW STATE STORES (Right: x=118 to 154)
    # -------------------------------------------------------------
    w1_box = FancyBboxPatch((118, 45.5), 36, 33.5, boxstyle="round,pad=0.8,rounding_size=2.0",
                            facecolor="#eff6ff", edgecolor="#2563eb", lw=2.0)
    ax.add_patch(w1_box)
    ax.text(136, 75.2, "WORKER 1 (KEY K1 AGGREGATOR)", fontsize=9.0, weight="bold", color="#1e40af", ha="center")
    ax.text(136, 72.8, "Sliding Windows (Size = 6 s, Slide = 3 s)", fontsize=7.5, color="#2563eb", ha="center")

    # Sliding Window Cards
    win_cards = [
        ("WA", "[00s, 06s)", 121.5, "#ffffff", "#93c5fd"),
        ("WB", "[03s, 09s)", 131.0, "#fef3c7", "#f59e0b"),
        ("WC", "[06s, 12s)", 140.5, "#ffffff", "#93c5fd"),
        ("WD", "[09s, 15s)", 150.0, "#ffffff", "#93c5fd"),
    ]
    for w_name, w_iv, wx, c_bg, c_border in win_cards:
        w_card = FancyBboxPatch((wx - 4.0, 48.5), 8.0, 21.0, boxstyle="round,pad=0.3,rounding_size=0.8",
                                facecolor=c_bg, edgecolor=c_border, lw=1.5 if w_name == "WB" else 1.1)
        ax.add_patch(w_card)
        ax.text(wx, 66.0, w_name, fontsize=8.0, weight="bold", color="#1e40af" if w_name != "WB" else "#b45309", ha="center")
        ax.text(wx, 63.3, w_iv, fontsize=6.2, weight="bold" if w_name == "WB" else "normal", 
                color="#0f172a" if w_name == "WB" else "#64748b", ha="center", fontfamily="monospace")
        ax.plot([wx - 3.2, wx + 3.2], [61.8, 61.8], color="#e2e8f0" if w_name != "WB" else "#fde68a", lw=0.8)
        ax.text(wx, 55.0, "State Store:\nSigma(V)", fontsize=6.5, color="#475569", ha="center")
        if w_name == "WB":
            ax.text(wx, 50.2, "TARGET", fontsize=5.8, weight="bold", color="#b45309", ha="center")

    # Worker 2 Box
    w2_box = FancyBboxPatch((118, 12), 36, 28, boxstyle="round,pad=0.8,rounding_size=2.0",
                            facecolor="#fef2f2", edgecolor="#dc2626", lw=1.5)
    ax.add_patch(w2_box)
    ax.text(136, 36.5, "WORKER 2 (KEY K2 AGGREGATOR)", fontsize=8.5, weight="bold", color="#991b1b", ha="center")
    ax.text(136, 25.0, "Key K2 Auxiliary Pipelines\n& Storage", fontsize=7.5, color="#64748b", ha="center")

    # Footer
    footer_box = FancyBboxPatch((6, 2.5), 148, 6.0, boxstyle="round,pad=0.4,rounding_size=1.0",
                                facecolor="#f8fafc", edgecolor="#cbd5e1", lw=1.0)
    ax.add_patch(footer_box)
    footer_text = (
        "PIPELINE SPECIFICATION:   Job ID: flink-sliding-stream-v4   |   Alignment: min(WM_P0, WM_P1) (Lag = 4.000 s)\n"
        "Windows: Half-Open EventTime Sliding Windows [t_start, t_end)   |   Allowed Lateness: 0.000 s (Strict)"
    )
    ax.text(80, 5.5, footer_text, fontsize=7.2, color="#475569", ha="center", va="center", fontfamily="sans-serif")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"[SUCCESS] Level 100 diagram rendered to: {output_path}")

if __name__ == "__main__":
    render_level100_diagram()
