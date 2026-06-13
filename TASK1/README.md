# Iris Flower Classification

A machine learning project for classifying iris flower species using supervised learning algorithms.

## 📋 Project Overview

This project demonstrates a complete machine learning pipeline for the famous Iris dataset. It includes data exploration, model training, evaluation, and inference on the Iris dataset containing measurements of iris flowers and their species classification.

**Dataset**: Iris Dataset (150 samples, 4 features, 3 classes)  
**Objective**: Classify iris flowers into one of three species using their measurements

## 📁 Project Structure

```
iris-classification/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup configuration
├── .gitignore                   # Git ignore rules
├── config.py                    # Configuration management
│
├── DATASET/                     # Data directory
│   └── Iris.csv                # Raw iris dataset
│
├── Model/                       # Trained models
│   └── iris_model.pkl          # Serialized trained model
│
├── Notebook/                    # Jupyter notebooks
│   └── analysis.ipynb          # Exploratory data analysis & model training
│
├── Predict/                     # Prediction module
│   ├── __init__.py             # Package initialization
│   └── predict.py              # Inference script
│
└── Images/                      # Visualizations & figures
    └── (output plots here)
```

## 🎯 Features

- **Data Exploration**: Comprehensive analysis of the Iris dataset
- **Data Visualization**: Exploratory plots and distribution analysis
- **Model Training**: Multiple classification algorithms compared
- **Model Evaluation**: Metrics including accuracy, precision, recall, F1-score
- **Prediction**: Script for classifying new iris samples
- **Professional Structure**: Following Python best practices and standards

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip or conda package manager

### Installation

1. **Navigate to project directory**
   ```bash
   cd iris-classification
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Using venv
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Project Workflow

### 1. Data Exploration & Analysis
Open and run `Notebook/analysis.ipynb` to:
- Load and explore the Iris dataset
- Visualize feature distributions and relationships
- Perform statistical analysis
- Identify patterns in the data

### 2. Model Training
The notebook includes:
- Data preprocessing and scaling
- Train-test split
- Model training (Random Forest, SVM, etc.)
- Hyperparameter tuning
- Model evaluation and comparison
- Model serialization and saving

### 3. Making Predictions
Run the prediction script:
```bash
python -m Predict.predict
```

Or use it as a module in your code:
```python
from Predict.predict import predict_iris
prediction = predict_iris([5.1, 3.5, 1.4, 0.2])
print(f"Predicted Species: {prediction}")
```

## 📈 Dataset Information

**Iris Dataset Attributes:**
- **Sepal Length** (cm): Length of the sepals
- **Sepal Width** (cm): Width of the sepals
- **Petal Length** (cm): Length of the petals
- **Petal Width** (cm): Width of the petals

**Target Classes:**
- Iris-setosa
- Iris-versicolor
- Iris-virginica

## 📦 Dependencies

Key libraries:
- `pandas` - Data manipulation and analysis
- `numpy` - Numerical computations
- `scikit-learn` - Machine learning algorithms
- `matplotlib` - Visualization
- `seaborn` - Statistical visualization
- `joblib` - Model serialization

See `requirements.txt` for complete list with versions.

## 🔧 Configuration

Edit `config.py` to customize:
- Model parameters
- Dataset paths
- Output directories
- Random seed for reproducibility
- Feature and target columns

## 📝 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run Jupyter notebook for analysis
jupyter notebook Notebook/analysis.ipynb

# 3. Make predictions (after training)
python -m Predict.predict
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Model file not found | Run the analysis notebook to train and save the model |
| Missing dependencies | Run `pip install -r requirements.txt` |
| Data file not found | Ensure `DATASET/Iris.csv` exists in the correct location |
| Import errors | Ensure virtual environment is activated |

## 📚 References

- [Iris Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Python Best Practices](https://pep8.org/)

## 👤 Author

**OASIS INFOBYTE Internship Program** - Data Science Track

## 📄 License

Educational project - OASIS INFOBYTE Internship Program

---

**Last Updated**: June 2026  
**Status**: ✅ Production Ready
