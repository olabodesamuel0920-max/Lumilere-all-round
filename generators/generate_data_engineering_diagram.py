#!/usr/bin/env python3
"""
Publication-Quality Diagram Generator for Data Engineering Benchmark [AG-TASK-011]
Topic: Distributed Stream Processing DAG (Watermark, Shuffle Routing & Windowed State)
Resolution: 2600 x 1500 px @ 300 DPI
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, PathPatch, ConnectionPatch
from matplotlib.path import Path
import numpy as np
import os

def build_data_engineering_diagram(output_path=None):
    if output_path is None:
        output_path = os.path.normpath(os.path.abspath("assets/data_engineering_stream_dag.png"))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    ax.set_xlim(0, 160)
    ax.set_ylim(0, 90)
    ax.axis("off")
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")

    # Title & Metadata Header
    ax.text(80, 86, "DISTRIBUTED STREAM PROCESSING DAG: KEY-ROUTED WATERMARK & STATEFUL WINDOWING", 
            fontsize=13, weight="bold", ha="center", va="center", color="#0f172a", fontfamily="sans-serif")
    ax.text(80, 83.2, "Enterprise Telemetry Ingestion Pipeline (Apache Flink / Google Cloud Dataflow Architecture)", 
            fontsize=9.5, style="italic", ha="center", va="center", color="#475569")
    
    # Dividing header line
    ax.plot([8, 152], [81.5, 81.5], color="#cbd5e1", lw=1.2)

    # -------------------------------------------------------------
    # STAGE 1: INGESTION PARTITIONS & EVENT QUEUES (Left Region)
    # -------------------------------------------------------------
    # Container box
    stage1_rect = FancyBboxPatch((6, 12), 46, 66, boxstyle="round,pad=0.8,rounding_size=2.0",
                                 facecolor="#f8fafc", edgecolor="#94a3b8", lw=1.5, linestyle="--")
    ax.add_patch(stage1_rect)
    ax.text(29, 75.5, "STAGE 1: PARTITIONED INGESTION BUFFERS", fontsize=10, weight="bold", color="#1e293b", ha="center")
    ax.text(29, 73.2, "Sequential Ingestion Arrival Cycles (T1 -> T4)", fontsize=8, color="#64748b", ha="center")

    # Partition 0 Box (Top)
    p0_box = FancyBboxPatch((8, 46), 42, 24, boxstyle="round,pad=0.5,rounding_size=1.5",
                            facecolor="#eff6ff", edgecolor="#3b82f6", lw=1.8)
    ax.add_patch(p0_box)
    ax.text(10, 67.5, "Ingestion Partition 0 (Source A)", fontsize=9.5, weight="bold", color="#1d4ed8")

    # Partition 1 Box (Bottom)
    p1_box = FancyBboxPatch((8, 15), 42, 24, boxstyle="round,pad=0.5,rounding_size=1.5",
                            facecolor="#f0fdf4", edgecolor="#22c55e", lw=1.8)
    ax.add_patch(p1_box)
    ax.text(10, 36.5, "Ingestion Partition 1 (Source B)", fontsize=9.5, weight="bold", color="#15803d")

    # Column Headers for Event Records
    for y_header, p_col in [(64, "#1d4ed8"), (33, "#15803d")]:
        ax.text(10, y_header, "Cycle", fontsize=7.5, weight="bold", color=p_col)
        ax.text(18, y_header, "Packet ID", fontsize=7.5, weight="bold", color=p_col)
        ax.text(28, y_header, "Key", fontsize=7.5, weight="bold", color=p_col)
        ax.text(35, y_header, "Event Time", fontsize=7.5, weight="bold", color=p_col)
        ax.text(45, y_header, "Value", fontsize=7.5, weight="bold", color=p_col)
        ax.plot([9, 48], [y_header - 1.2, y_header - 1.2], color="#cbd5e1", lw=0.8)

    # Ingestion Data Records
    # Partition 0 records
    p0_records = [
        ("T1", "A1", "K1", "03 s", "18", "#dbeafe", "#1e40af"),
        ("T2", "A2", "K2", "08 s", "25", "#fee2e2", "#991b1b"),
        ("T3", "A3", "K1", "06 s", "12", "#dbeafe", "#1e40af"),
        ("T4", "A4", "K2", "14 s", "30", "#fee2e2", "#991b1b"),
    ]
    y_pos = 60.5
    for cycle, pid, key, et, val, badge_bg, badge_fg in p0_records:
        ax.text(11, y_pos, cycle, fontsize=8, color="#334155", weight="bold")
        ax.text(19.5, y_pos, pid, fontsize=8, color="#0f172a", fontfamily="monospace")
        # Key Badge
        k_patch = FancyBboxPatch((26.5, y_pos - 1.2), 4.5, 2.4, boxstyle="round,pad=0.2,rounding_size=0.6",
                                 facecolor=badge_bg, edgecolor=badge_fg, lw=0.8)
        ax.add_patch(k_patch)
        ax.text(28.75, y_pos, key, fontsize=7.5, weight="bold", color=badge_fg, ha="center", va="center")
        ax.text(36.5, y_pos, et, fontsize=8, color="#334155", fontfamily="monospace")
        ax.text(46, y_pos, val, fontsize=8.5, weight="bold", color="#0f172a")
        y_pos -= 3.6

    # Partition 1 records
    p1_records = [
        ("T1", "B1", "K2", "04 s", "22", "#fee2e2", "#991b1b"),
        ("T2", "B2", "K1", "09 s", "28", "#dbeafe", "#1e40af"),
        ("T3", "B3", "K1", "05 s", "16", "#dbeafe", "#1e40af"),
        ("T4", "B4", "K2", "11 s", "15", "#fee2e2", "#991b1b"),
    ]
    y_pos = 29.5
    for cycle, pid, key, et, val, badge_bg, badge_fg in p1_records:
        ax.text(11, y_pos, cycle, fontsize=8, color="#334155", weight="bold")
        ax.text(19.5, y_pos, pid, fontsize=8, color="#0f172a", fontfamily="monospace")
        # Key Badge
        k_patch = FancyBboxPatch((26.5, y_pos - 1.2), 4.5, 2.4, boxstyle="round,pad=0.2,rounding_size=0.6",
                                 facecolor=badge_bg, edgecolor=badge_fg, lw=0.8)
        ax.add_patch(k_patch)
        ax.text(28.75, y_pos, key, fontsize=7.5, weight="bold", color=badge_fg, ha="center", va="center")
        ax.text(36.5, y_pos, et, fontsize=8, color="#334155", fontfamily="monospace")
        ax.text(46, y_pos, val, fontsize=8.5, weight="bold", color="#0f172a")
        y_pos -= 3.6

    # -------------------------------------------------------------
    # STAGE 2: WATERMARK ASSIGNER (OPERATOR NODE)
    # -------------------------------------------------------------
    wm_rect = FancyBboxPatch((55, 12), 22, 66, boxstyle="round,pad=0.8,rounding_size=2.0",
                             facecolor="#fefce8", edgecolor="#eab308", lw=1.5, linestyle="--")
    ax.add_patch(wm_rect)
    ax.text(66, 75.5, "STAGE 2: WATERMARK OPERATOR", fontsize=9, weight="bold", color="#854d0e", ha="center")
    ax.text(66, 73.0, "Stream Timestamp & Watermark Assigner", fontsize=7.5, style="italic", color="#a16207", ha="center")

    # Authentic Operator Specification Card (No spoon-fed formulas or cheat-sheets)
    wm_op_card = FancyBboxPatch((56.8, 38), 18.4, 30, boxstyle="round,pad=0.5,rounding_size=1.2",
                                facecolor="#ffffff", edgecolor="#facc15", lw=1.4)
    ax.add_patch(wm_op_card)
    ax.text(66, 64.5, "WatermarkStrategy", fontsize=8.5, weight="bold", color="#854d0e", ha="center")
    ax.plot([58, 74], [62.8, 62.8], color="#fde047", lw=1.0)

    ax.text(58.5, 59.0, "Strategy Type:", fontsize=7.5, weight="bold", color="#475569")
    ax.text(58.5, 56.5, "BoundedOutOfOrderness", fontsize=7, color="#0f172a", fontfamily="monospace")

    ax.text(58.5, 52.0, "Bounded Lag (delta_t):", fontsize=7.5, weight="bold", color="#475569")
    ax.text(58.5, 49.5, "3.000 s", fontsize=8, weight="bold", color="#b45309", fontfamily="monospace")

    ax.text(58.5, 45.0, "Allowed Lateness:", fontsize=7.5, weight="bold", color="#475569")
    ax.text(58.5, 42.5, "0.000 s (Strict)", fontsize=7.5, weight="bold", color="#dc2626", fontfamily="monospace")

    # Ingestion Clock Sync Indicator
    sync_card = FancyBboxPatch((56.8, 16), 18.4, 18, boxstyle="round,pad=0.5,rounding_size=1.2",
                               facecolor="#ffffff", edgecolor="#cbd5e1", lw=1.0)
    ax.add_patch(sync_card)
    ax.text(66, 30.5, "Partitions Synced", fontsize=7.5, weight="bold", color="#334155", ha="center")
    ax.text(66, 27.0, "Event Time Evaluation", fontsize=7, color="#64748b", ha="center")
    ax.text(66, 23.5, "Cycles: T1 -> T4", fontsize=7.5, weight="bold", color="#0f172a", ha="center")
    ax.text(66, 19.5, "Watermark-driven Eviction", fontsize=6.8, style="italic", color="#475569", ha="center")

    # Connect Stage 1 to Stage 2
    ax.annotate("", xy=(55, 58), xytext=(50, 58), arrowprops=dict(arrowstyle="->", lw=1.5, color="#64748b"))
    ax.annotate("", xy=(55, 27), xytext=(50, 27), arrowprops=dict(arrowstyle="->", lw=1.5, color="#64748b"))

    # -------------------------------------------------------------
    # STAGE 3: SHUFFLE INTERCONNECT & ROUTING TOPOLOGY
    # -------------------------------------------------------------
    # Demux Switch Points exiting Stage 2
    # P0 exits at (77, 58), P1 exits at (77, 27)
    # Target Worker 1 (Key K1) is at y = 58
    # Target Worker 2 (Key K2) is at y = 27

    # Worker 1 Box (Upper Engine - Key K1)
    w1_box = FancyBboxPatch((118, 44), 38, 30, boxstyle="round,pad=0.8,rounding_size=2.0",
                            facecolor="#eff6ff", edgecolor="#2563eb", lw=2.0)
    ax.add_patch(w1_box)
    ax.text(137, 71.5, "WORKER 1: STATEFUL AGGREGATOR", fontsize=9.5, weight="bold", color="#1e40af", ha="center")
    ax.text(137, 68.8, "Key K1 Dedicated Engine", fontsize=8.5, weight="bold", color="#2563eb", ha="center")

    # Worker 2 Box (Lower Engine - Key K2)
    w2_box = FancyBboxPatch((118, 12), 38, 28, boxstyle="round,pad=0.8,rounding_size=2.0",
                            facecolor="#fef2f2", edgecolor="#dc2626", lw=1.5)
    ax.add_patch(w2_box)
    ax.text(137, 37.5, "WORKER 2: KEY K2 ENGINE", fontsize=9, weight="bold", color="#991b1b", ha="center")
    ax.text(137, 35.0, "Key K2 Auxiliary Aggregator", fontsize=8, color="#b91c1c", ha="center")

    # Inline Filter on Route A (Upper branch before Worker 1)
    filter_box = FancyBboxPatch((94, 54), 16, 8, boxstyle="round,pad=0.4,rounding_size=1.0",
                                facecolor="#f3e8ff", edgecolor="#9333ea", lw=1.5)
    ax.add_patch(filter_box)
    ax.text(102, 59.5, "PREDICATE FILTER", fontsize=7.5, weight="bold", color="#6b21a8", ha="center")
    ax.text(102, 56.5, "Pass Condition: Value > 15", fontsize=7, weight="bold", color="#581c87", ha="center")

    # DRAWING ROUTING CHANNELS (SHUFFLE TOPOLOGY)
    # Channel 1: P0 -> K1 (Straight to Filter Box -> Worker 1)
    ax.plot([77, 94], [58, 58], color="#2563eb", lw=2.2)
    ax.annotate("", xy=(94, 58), xytext=(88, 58), arrowprops=dict(arrowstyle="->", lw=2.0, color="#2563eb"))
    ax.text(83, 59.5, "P0 [K1]", fontsize=7.5, weight="bold", color="#1d4ed8")

    # From Filter to Worker 1
    ax.plot([110, 118], [58, 58], color="#2563eb", lw=2.2)
    ax.annotate("", xy=(118, 58), xytext=(112, 58), arrowprops=dict(arrowstyle="->", lw=2.0, color="#2563eb"))

    # Channel 2: P1 -> K2 (Straight to Worker 2)
    ax.plot([77, 118], [27, 27], color="#dc2626", lw=2.2)
    ax.annotate("", xy=(118, 27), xytext=(112, 27), arrowprops=dict(arrowstyle="->", lw=2.0, color="#dc2626"))
    ax.text(83, 25.0, "P1 [K2]", fontsize=7.5, weight="bold", color="#b91c1c")

    # Channel 3: P0 -> K2 (Crosses down from (82, 58) to (114, 27))
    # Path for P0 -> K2
    p0_k2_x = [82, 85, 108, 114]
    p0_k2_y = [58, 58, 27, 27]
    ax.plot(p0_k2_x, p0_k2_y, color="#dc2626", lw=1.8, linestyle="-")
    ax.scatter([82], [58], color="#dc2626", s=30, zorder=5) # Demux junction dot on P0
    ax.text(84, 53, "P0 [K2]", fontsize=7.5, color="#dc2626", weight="bold")

    # Channel 4: P1 -> K1 (Crosses up from (85, 27) up to (114, 58))
    # Crosses the P0->K2 wire around x = 96.5, y = 42.5
    # To show an explicit BRIDGE / HOP (NO CONNECTION):
    ax.scatter([85], [27], color="#2563eb", s=30, zorder=5) # Demux junction dot on P1
    ax.text(86, 31, "P1 [K1]", fontsize=7.5, color="#2563eb", weight="bold")

    # Segment before crossing: (85, 27) -> (95, 40.5)
    ax.plot([85, 95], [27, 40.5], color="#2563eb", lw=2.0)

    # Bridge Arc over crossing point (96.5, 42.5)
    bridge_arc = patches.Arc((96.5, 42.5), 3.2, 3.2, angle=53, theta1=0, theta2=180, color="#2563eb", lw=2.0)
    ax.add_patch(bridge_arc)

    # Segment after crossing: (98, 44.5) -> (108, 58) -> (118, 58)
    ax.plot([98, 108, 114], [44.5, 58, 58], color="#2563eb", lw=2.0)
    # Enters Worker 1 directly (bypassing Filter Node!)
    # Demux merge dot right at Worker 1 entrance (114, 58)
    ax.scatter([114], [58], color="#2563eb", s=35, zorder=5)
    ax.text(102, 50, "Bypasses Filter", fontsize=6.8, style="italic", color="#1e40af")

    # Annotate the Bridge Jump explicitly (Lumiere Golden Standard)
    ax.annotate("Wire Crossing\n(No Junction)", xy=(96.5, 44), xytext=(94, 34),
                fontsize=7, weight="bold", color="#475569", ha="center",
                arrowprops=dict(arrowstyle="->", lw=0.8, color="#64748b"))

    # -------------------------------------------------------------
    # DETAILS INSIDE WORKER 1: TUMBLING EVENT-TIME WINDOWS
    # -------------------------------------------------------------
    ax.text(137, 65.5, "Event-Time Tumbling Windows (Size = 5 s)", fontsize=8, color="#334155", ha="center")
    
    # Window W0 Box [0 s, 5 s)
    w0_rect = FancyBboxPatch((120, 47), 10.5, 16, boxstyle="round,pad=0.3,rounding_size=0.8",
                             facecolor="#ffffff", edgecolor="#93c5fd", lw=1.2)
    ax.add_patch(w0_rect)
    ax.text(125.25, 60.5, "Window W0", fontsize=7.5, weight="bold", color="#1e40af", ha="center")
    ax.text(125.25, 58.2, "[00 s, 05 s)", fontsize=7, color="#64748b", ha="center")
    ax.plot([121, 129.5], [56.8, 56.8], color="#e2e8f0", lw=0.8)
    ax.text(125.25, 53.5, "State Sum:\nSigma(V)", fontsize=7, color="#475569", ha="center")

    # Window W1 Box [5 s, 10 s)
    w1_rect = FancyBboxPatch((131.8, 47), 10.5, 16, boxstyle="round,pad=0.3,rounding_size=0.8",
                             facecolor="#ffffff", edgecolor="#93c5fd", lw=1.2)
    ax.add_patch(w1_rect)
    ax.text(137.05, 60.5, "Window W1", fontsize=7.5, weight="bold", color="#1e40af", ha="center")
    ax.text(137.05, 58.2, "[05 s, 10 s)", fontsize=7, color="#64748b", ha="center")
    ax.plot([132.8, 141.3], [56.8, 56.8], color="#e2e8f0", lw=0.8)
    ax.text(137.05, 53.5, "State Sum:\nSigma(V)", fontsize=7, color="#475569", ha="center")

    # Window W2 Box [10 s, 15 s)
    w2_rect = FancyBboxPatch((143.5, 47), 10.5, 16, boxstyle="round,pad=0.3,rounding_size=0.8",
                             facecolor="#ffffff", edgecolor="#93c5fd", lw=1.2)
    ax.add_patch(w2_rect)
    ax.text(148.75, 60.5, "Window W2", fontsize=7.5, weight="bold", color="#1e40af", ha="center")
    ax.text(148.75, 58.2, "[10 s, 15 s)", fontsize=7, color="#64748b", ha="center")
    ax.plot([144.5, 153.0], [56.8, 56.8], color="#e2e8f0", lw=0.8)
    ax.text(148.75, 53.5, "State Sum:\nSigma(V)", fontsize=7, color="#475569", ha="center")

    # Details inside Worker 2
    ax.text(137, 26, "Windowing & State Storage\n(Auxiliary Pipeline for Key K2)", 
            fontsize=7.5, color="#64748b", ha="center", va="center")

    # Bottom Architecture Metadata Banner (Zero spoon-fed rules)
    legend_box = FancyBboxPatch((6, 2.5), 148, 6.0, boxstyle="round,pad=0.4,rounding_size=1.0",
                                facecolor="#f8fafc", edgecolor="#cbd5e1", lw=1.0)
    ax.add_patch(legend_box)
    
    footer_text = (
        "PIPELINE EXECUTION METADATA:   Topology ID: flink-telemetry-ingest-v2   |   Engine: Apache Flink Stream Execution Environment\n"
        "State Backend: EmbeddedRocksDBStateBackend   |   Time Characteristic: TimeCharacteristic.EventTime   |   Parallelism: 2 Partitions"
    )
    ax.text(80, 5.5, footer_text, fontsize=7.2, color="#475569", ha="center", va="center", fontfamily="sans-serif")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"[SUCCESS] Diagram rendered to: {output_path}")

if __name__ == "__main__":
    build_data_engineering_diagram()
