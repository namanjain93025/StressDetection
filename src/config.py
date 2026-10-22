"""Project-wide paths, constants, and type annotations.

This module centralises file‑system paths and experiment‑wide configuration
values for the StressDetection project. Adding explicit type hints makes the
codebase easier to understand and enables static analysis tools such as
``mypy``.
"""
from pathlib import Path
from typing import List, Dict

# Base directories -----------------------------------------------------------
ROOT: Path = Path(__file__).resolve().parents[1]
WESAD_DIR: Path = ROOT / "WESAD"
PROCESSED_DIR: Path = ROOT / "data" / "processed"
OUTPUT_DIR: Path = ROOT / "outputs"
MODEL_DIR: Path = ROOT / "models"

# Dataset subjects ----------------------------------------------------------
# WESAD has 15 usable subjects (S1 and S12 were discarded by the authors)
SUBJECTS: List[str] = [f"S{i}" for i in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17)]

# Sampling rates ------------------------------------------------------------
FS_RAW: int = 700  # RespiBAN chest sampling rate (Hz)
FS: int = 100      # after anti‑aliased decimation (factor 7)
CHANNELS: List[str] = ["ECG", "EDA", "EMG", "Temp", "Resp"]

# Windowing parameters ------------------------------------------------------
WINDOW_S: int = 60   # window length (seconds)
STEP_S: int = 15     # hop between windows (seconds) → 75% overlap

# Label mapping -------------------------------------------------------------
# WESAD protocol labels we keep (0 = transient, 5‑7 = ignore)
LABELS: Dict[int, str] = {1: "Baseline", 2: "Stress", 3: "Amusement", 4: "Meditation"}
CLASS_NAMES: List[str] = list(LABELS.values())

# Task definitions ----------------------------------------------------------
# Classification tasks: original class index (0‑3) → task‑specific index
TASKS: Dict[str, Dict[str, object]] = {
    "4class": {
        "classes": ["Baseline", "Stress", "Amusement", "Meditation"],
        "map": {0: 0, 1: 1, 2: 2, 3: 3},
    },
    "3class": {
        "classes": ["Baseline", "Stress", "Amusement"],
        "map": {0: 0, 1: 1, 2: 2},
    },
    # Binary setup from the WESAD paper: stress vs. non‑stress (baseline + amusement)
    "binary": {
        "classes": ["Non-stress", "Stress"],
        "map": {0: 0, 1: 1, 2: 0},
    },
}

# Convenience path for the processed NumPy archive --------------------------
PROCESSED_FILE: Path = PROCESSED_DIR / f"wesad_{FS}hz_{WINDOW_S}s_step{STEP_S}.npz"
