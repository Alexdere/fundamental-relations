#!/bin/bash
# Run all Collatz-Cascade analysis scripts
# Requires: Python 3.6+

echo "=========================================="
echo "Collatz-Cascade Bridge: Full Analysis"
echo "=========================================="
echo

echo "[1/5] Core engine: tiers, Baker bounds, death spiral..."
python3 collatz_engine.py
echo
echo "=========================================="

echo "[2/5] Convergent families and phase constraints..."
python3 collatz_convergents.py
echo
echo "=========================================="

echo "[3/5] Deep analysis: asymptotic race, growth rates..."
python3 collatz_deep_analysis.py
echo
echo "=========================================="

echo "[4/5] Pell defect propagation analysis..."
python3 collatz_pell_propagation.py
echo
echo "=========================================="

echo "[5/5] Coherence audit: what pulls back from Q(sqrt2,i) to Z..."
python3 collatz_coherence.py
echo
echo "=========================================="
echo "Done. See collatz_cascade_synthesis_2026-05-20.md for full write-up."
