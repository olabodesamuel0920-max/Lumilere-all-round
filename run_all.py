#!/usr/bin/env python3
"""
PROJECT LUMIERE: BENCHMARK SUITE RUNNER
=======================================
Master CLI pipeline coordinating:
1. Procedural High-Resolution Multimodal Diagram Generation (Matplotlib/NumPy)
2. Rigorous 21-Point Benchmark Verification & Mathematical Audit Engines
"""

import os
import sys
import subprocess
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def print_banner():
    banner = """
================================================================================
               PROJECT LUMIERE: BENCHMARK & AUDIT SUITE
================================================================================
  Demonstration of:
  - Procedural Multimodal Visual Asset Synthesis (Distributed Stream DAGs)
  - Formal Mathematical Modeling & Ground-Truth Verification
  - 5-Pillar Image Description Word-Count & KaTeX Format Audits
  - 21-Point Quality Compliance & Adversarial Trap Validation
================================================================================
"""
    print(banner)

def check_dependencies():
    missing = []
    try:
        import matplotlib
    except ImportError:
        missing.append("matplotlib")
    try:
        import numpy
    except ImportError:
        missing.append("numpy")
    return missing

def run_diagram_generators():
    print("\n" + "=" * 60)
    print("STAGE 1: PROCEDURAL MULTIMODAL DIAGRAM GENERATION")
    print("=" * 60)
    
    missing = check_dependencies()
    if missing:
        print(f"[!] Note: Visualization dependencies not detected: {', '.join(missing)}")
        print("    Diagram generation requires: pip install -r requirements.txt")
        print("    (Or run with uv: uv run run_all.py)")
        return False
    
    generators = [
        ("Distributed Stream Processing DAG", "generators/generate_data_engineering_diagram.py"),
        ("Level-100 Sliding Window Stream Topology", "generators/generate_level100_diagram.py"),
    ]
    
    all_ok = True
    for name, rel_path in generators:
        script_path = os.path.join(BASE_DIR, rel_path)
        print(f"\n[*] Generating: {name}...")
        t0 = time.time()
        res = subprocess.run([sys.executable, script_path], cwd=BASE_DIR, capture_output=True, text=True)
        elapsed = time.time() - t0
        if res.returncode == 0:
            print(f"    [OK] Rendered successfully ({elapsed:.2f}s)")
            if res.stdout:
                for line in res.stdout.strip().split("\n"):
                    print(f"         {line}")
        else:
            all_ok = False
            print(f"    [FAIL] Error rendering {name}:")
            print(res.stderr)
    return all_ok

def run_audit_suites():
    print("\n" + "=" * 60)
    print("STAGE 2: AUTOMATED BENCHMARK QUALITY & MATHEMATICAL AUDITS")
    print("=" * 60)
    
    audits = [
        ("Cytogenetics Multi-Panel Karyotype & KaTeX Audit", "audits/test_cytogenetics_b9418.py"),
        ("USP7 Interactome Co-IP Condition & Blot Audit", "audits/test_usp7_audits.py"),
        ("Spt6/Rpb3 Transcription Elongation Model Audit", "audits/run_audits.py"),
        ("Payload Structure & 5-Pillar Description Audit", "audits/test_payload.py"),
    ]
    
    results = []
    for name, rel_path in audits:
        script_path = os.path.join(BASE_DIR, rel_path)
        print(f"\n[*] Executing Audit: {name}...")
        t0 = time.time()
        res = subprocess.run([sys.executable, script_path], cwd=BASE_DIR, capture_output=True, text=True)
        elapsed = time.time() - t0
        passed = (res.returncode == 0)
        results.append((name, passed, elapsed, res.stdout, res.stderr))
        
        if passed:
            print(f"    [PASS] Verification passed ({elapsed:.2f}s)")
            out_lines = [l for l in res.stdout.strip().split("\n") if l.strip()]
            for line in out_lines[-3:]:
                print(f"         {line}")
        else:
            print(f"    [FAIL] Audit failed:")
            print(res.stderr)
            
    return results

def print_summary(diag_ok, audit_results):
    print("\n" + "=" * 80)
    print("                             EXECUTIVE SUMMARY")
    print("=" * 80)
    print(f"  {'Subsystem / Test Target':<50} | {'Status':<10} | {'Runtime'}")
    print("  " + "-" * 76)
    
    diag_status = "PASS" if diag_ok else "SKIPPED"
    print(f"  {'Stage 1: Procedural Visual Asset Generators':<50} | {diag_status:<10} | Done")
    
    all_audits_passed = True
    for name, passed, elapsed, _, _ in audit_results:
        status = "PASS" if passed else "FAIL"
        if not passed:
            all_audits_passed = False
        print(f"  {name:<50} | {status:<10} | {elapsed:.2f}s")
        
    print("  " + "-" * 76)
    overall = "100% OPERATIONAL & VERIFIED" if (all_audits_passed and diag_ok) else "AUDITS PASSED (Diagrams Skipped)" if all_audits_passed else "ATTENTION NEEDED"
    print(f"  OVERALL RESULT: {overall}")
    print("=" * 80 + "\n")

def main():
    print_banner()
    os.makedirs(os.path.join(BASE_DIR, "assets"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "scratch"), exist_ok=True)
    
    diag_ok = run_diagram_generators()
    audit_results = run_audit_suites()
    print_summary(diag_ok, audit_results)

if __name__ == "__main__":
    main()
