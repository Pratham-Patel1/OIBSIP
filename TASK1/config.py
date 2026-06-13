"""
Configuration module for Iris Classification Project

This module centralizes all configuration parameters used throughout the project.
Modify these settings to customize the behavior of the analysis and prediction pipeline.
"""

import os
from pathlib import Path

# ============================================================================
# PROJECT PATHS
# ============================================================================

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.absolute()

# Data paths
DATASET_DIR = PROJECT_ROOT / "DATASET"
DATA_FILE = DATASET_DIR / "Iris.csv"

# Model paths
MODEL_DIR = PROJECT_ROOT / "Model"
MODEL_FILE = MODEL_DIR / "iris_model.pkl"

# Output paths
OUTPUT_DIR = PROJECT_ROOT / "Images"
NOTEBOOK_DIR = PROJECT_ROOT / "Notebook"
PREDICT_DIR = PROJECT_ROOT / "Predict"

# ============================================================================
# DATA CONFIGURATION
# ============================================================================

# Feature columns in the dataset
FEATURE_COLUMNS = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

# Target column
TARGET_COLUMN = 'Species'

# Iris species classes
IRIS_SPECIES = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# ============================================================================
# MODEL CONFIGURATION
# ============================================================================

# Random seed for reproducibility
RANDOM_SEED = 42

# Train-test split ratio
TEST_SIZE = 0.2

# Cross-validation folds
CV_FOLDS = 5

# Model parameters (Random Forest)
RF_PARAMS = {
    'n_estimators': 100,
    'max_depth': 10,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'random_state': RANDOM_SEED
}

# Feature scaling
SCALE_FEATURES = True
SCALER_TYPE = 'StandardScaler'  # 'StandardScaler' or 'MinMaxScaler'

# ============================================================================
# VISUALIZATION CONFIGURATION
# ============================================================================

# Figure size for plots
FIGURE_SIZE = (12, 8)

# Color palette
COLOR_PALETTE = 'husl'

# DPI for saved figures
DPI = 300

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

# Enable logging
ENABLE_LOGGING = True

# Log level
LOG_LEVEL = 'INFO'

# ============================================================================
# VALIDATION
# ============================================================================

def validate_paths():
    """Validate that all required paths exist."""
    required_dirs = [
        DATASET_DIR,
        MODEL_DIR,
        OUTPUT_DIR,
    ]
    
    for dir_path in required_dirs:
        if not dir_path.exists():
            print(f"Warning: Directory {dir_path} does not exist. Creating it...")
            dir_path.mkdir(parents=True, exist_ok=True)
    
    if not DATA_FILE.exists():
        print(f"Warning: Data file {DATA_FILE} not found!")
        return False
    
    return True


if __name__ == "__main__":
    # Test configuration
    print("Project Configuration")
    print("=" * 50)
    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Data File: {DATA_FILE}")
    print(f"Model File: {MODEL_FILE}")
    print(f"Output Dir: {OUTPUT_DIR}")
    print("=" * 50)
    print(f"Features: {FEATURE_COLUMNS}")
    print(f"Target: {TARGET_COLUMN}")
    print(f"Classes: {IRIS_SPECIES}")
    print("=" * 50)
    print(f"Random Seed: {RANDOM_SEED}")
    print(f"Test Size: {TEST_SIZE}")
    print("=" * 50)
    validate_paths()
    print("✓ Configuration validated successfully!")
