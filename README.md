# Project Lumière: Benchmark Generation & Verification Engine

This repository contains the standalone code architecture for **Project Lumière**, demonstrating how frontier multimodal benchmarks are engineered, visually synthesized, and programmatically audited.

---

## 1. What This Code Demonstrates

When you run this project, you will see two core engineering capabilities in action:

1. **Procedural Multimodal Visual Asset Generation (`generators/`)**:
   - Synthesizes publication-grade, high-resolution (300 DPI) technical schematics and stream processing topologies using pure code (`matplotlib` and `numpy`).
   - Generates authentic pipeline structures: partitioned ingestion buffers, watermark generators, non-planar bridge jumps, predicate filters, and stateful sliding window aggregations.
   - Outputs saved directly to `assets/`.

2. **Automated Quality Compliance & Mathematical Audits (`audits/`)**:
   - Enforces the strict 21-point evaluation rubric for AI multimodal benchmarks.
   - **Ground-Truth Verification**: Runs algorithmic validations of biological karyotypes, Fundamental Number ($NF$) arm equations, and Western blot Co-IP binding matrices.
   - **KaTeX/LaTeX String Sanitization**: Scans all prompt texts and solutions to guarantee zero banned Unicode math characters (`\le`, `\ge`, `\times` formatted properly).
   - **5-Pillar Image Description Audits**: Validates that all 5 required structural pillars (Modality, Layout, Readouts, Artifacts, Ground Truth) are present and exceed the required 200-word minimum threshold.
   - **Adversarial Distractor Validation**: Guarantees exactly 5 mechanistic distractors derived from genuine frontier model perceptual failure modes.

---

## 2. Quick Start

### Installation
All audit scripts run out-of-the-box using the standard Python library.  
To also render the high-resolution visual diagrams:

```bash
pip install -r requirements.txt
```

*(Or if you use `uv`: `uv run run_all.py`)*

### Run Everything
To execute the entire asset generation and verification pipeline end-to-end:

```bash
python run_all.py
```

---

## 3. Repository Architecture

```text
Lumilere all-round/
├── README.md                                   # This architectural guide
├── requirements.txt                            # Minimal visualization dependencies
├── run_all.py                                  # Master pipeline runner
├── assets/                                     # Output folder for generated 300 DPI diagrams
│   ├── data_engineering_stream_dag.png
│   └── level100_stream_dag.png
├── generators/                                 # Visual benchmark synthesis scripts
│   ├── generate_data_engineering_diagram.py    # Flink DAG telemetry topology generator
│   └── generate_level100_diagram.py            # Level-100 sliding window benchmark generator
└── audits/                                     # Quality & mathematical verification suites
    ├── test_cytogenetics_b9418.py              # Karyotype arm-ratio & KaTeX audit
    ├── test_usp7_audits.py                     # Western blot interactome Co-IP audit
    ├── run_audits.py                           # Spt6/Rpb3 transcription elongation audit
    └── test_payload.py                         # 5-pillar description & length audit
```

---

## 4. Running Individual Modules

You can also run any module independently:

- **Generate Data Engineering Stream Diagram:**
  ```bash
  python generators/generate_data_engineering_diagram.py
  ```
- **Generate Level-100 Sliding Window Diagram:**
  ```bash
  python generators/generate_level100_diagram.py
  ```
- **Run Cytogenetics Karyotype Mathematical Audit:**
  ```bash
  python audits/test_cytogenetics_b9418.py
  ```
- **Run Western Blot Interactome Audit:**
  ```bash
  python audits/test_usp7_audits.py
  ```
