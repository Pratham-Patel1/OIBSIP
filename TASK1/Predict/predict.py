"""
IRIS FLOWER PREDICTION SCRIPT
==============================

Purpose:
--------
This script demonstrates how to use the trained Iris classification model
in a real-world scenario. After building and training a machine learning model 
in the analysis notebook, we need a way to apply that model to make predictions 
on new data.

Why This File Is Useful:
------------------------
1. **Model Deployment**: Separates the prediction logic from training, allowing 
   the model to be used independently without running the entire analysis notebook.

2. **Practical Application**: Shows how to use the trained model to classify 
   new iris flower samples based on their measurements.

3. **Reproducibility**: Makes it easy for others to use the model for predictions 
   without understanding the entire training process.

4. **Integration**: Can be imported as a module or run as a standalone script 
   for predictions on new data.

5. **Production Use**: Demonstrates how to load a saved model and use it 
   in production environments.

Usage:
------
As a module:
    from Predict.predict import predict_iris
    prediction = predict_iris([5.1, 3.5, 1.4, 0.2])
    print(f"Predicted Species: {prediction}")

As a script:
    python predict.py
"""

import joblib
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import config


def load_model(model_path=None):
    """
    Load the pre-trained model from disk.
    
    Parameters:
    -----------
    model_path : str, optional
        Path to the saved model file. If None, uses config.MODEL_FILE
    
    Returns:
    --------
    model : sklearn model object
        The loaded trained model
    
    Raises:
    -------
    FileNotFoundError: If the model file doesn't exist
    """
    if model_path is None:
        model_path = config.MODEL_FILE
    
    try:
        model = joblib.load(model_path)
        print(f"✓ Model loaded successfully from {model_path}")
        return model
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Model file not found at {model_path}. "
            f"Please train and save the model first by running the analysis notebook."
        )


def predict_iris(features, model=None):
    """
    Predict the iris species for given flower measurements.
    
    Parameters:
    -----------
    features : list or array-like
        List of four measurements: [Sepal Length, Sepal Width, 
                                    Petal Length, Petal Width]
        All measurements should be in centimeters.
    
    model : sklearn model object, optional
        Pre-loaded model. If None, will load from default path.
    
    Returns:
    --------
    prediction : str
        The predicted iris species
    
    Example:
    --------
    >>> prediction = predict_iris([5.1, 3.5, 1.4, 0.2])
    >>> print(f"Species: {prediction}")
    Species: Iris-setosa
    """
    # Load model if not provided
    if model is None:
        model = load_model()
    
    # Create a DataFrame with the features
    feature_df = pd.DataFrame(
        [features],
        columns=config.FEATURE_COLUMNS
    )
    
    # Make prediction
    prediction = model.predict(feature_df)
    
    return prediction[0]


def predict_iris_with_probability(features, model=None):
    """
    Predict iris species and return prediction probabilities.
    
    Parameters:
    -----------
    features : list or array-like
        List of four measurements: [Sepal Length, Sepal Width, 
                                    Petal Length, Petal Width]
    
    model : sklearn model object, optional
        Pre-loaded model. If None, will load from default path.
    
    Returns:
    --------
    prediction : str
        The predicted iris species
    
    probabilities : dict
        Dictionary with species names and their probabilities
    """
    # Load model if not provided
    if model is None:
        model = load_model()
    
    # Create a DataFrame with the features
    feature_df = pd.DataFrame(
        [features],
        columns=config.FEATURE_COLUMNS
    )
    
    # Make prediction
    prediction = model.predict(feature_df)[0]
    
    # Get prediction probabilities
    probabilities_array = model.predict_proba(feature_df)[0]
    probabilities = {
        species: prob for species, prob in 
        zip(config.IRIS_SPECIES, probabilities_array)
    }
    
    return prediction, probabilities


def main():
    """
    Main function demonstrating the prediction script.
    """
    print("=" * 60)
    print("IRIS FLOWER CLASSIFICATION - PREDICTION DEMO")
    print("=" * 60)
    
    try:
        # Load the model
        model = load_model()
        
        # Example 1: Simple prediction
        print("\n📊 Example 1: Simple Prediction")
        print("-" * 60)
        sample_features = [5.1, 3.5, 1.4, 0.2]
        print(f"Input features (Sepal L, Sepal W, Petal L, Petal W):")
        print(f"  {sample_features}")
        
        prediction = predict_iris(sample_features, model)
        print(f"\n✓ Predicted Species: {prediction}")
        
        # Example 2: Prediction with probabilities
        print("\n\n📊 Example 2: Prediction with Probabilities")
        print("-" * 60)
        sample_features_2 = [6.5, 3.0, 5.5, 1.8]
        print(f"Input features (Sepal L, Sepal W, Petal L, Petal W):")
        print(f"  {sample_features_2}")
        
        prediction_2, probabilities = predict_iris_with_probability(
            sample_features_2, model
        )
        print(f"\n✓ Predicted Species: {prediction_2}")
        print("\nPrediction Probabilities:")
        for species, prob in probabilities.items():
            print(f"  {species}: {prob:.2%}")
        
        # Example 3: Multiple predictions
        print("\n\n📊 Example 3: Multiple Predictions")
        print("-" * 60)
        test_samples = [
            ([5.0, 3.4, 1.5, 0.2], "Setosa-like"),
            ([6.2, 2.9, 4.3, 1.3], "Versicolor-like"),
            ([7.7, 3.0, 6.1, 2.3], "Virginica-like"),
        ]
        
        for features, description in test_samples:
            prediction = predict_iris(features, model)
            print(f"{description}: {features}")
            print(f"  → Predicted: {prediction}\n")
        
        print("=" * 60)
        print("✓ Prediction demo completed successfully!")
        print("=" * 60)
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("\nTo use this script, you need to:")
        print("1. Run the analysis.ipynb notebook to train the model")
        print("2. The notebook will save the model to Model/iris_model.pkl")
        sys.exit(1)


if __name__ == "__main__":
    main()
        'PetalLengthCm',
        'PetalWidthCm'
    ]
)

# Use the trained model to make a prediction on the sample
# The model analyzes the flower measurements and predicts which species it is
prediction = model.predict(sample)

# Display the prediction result
# prediction[0] contains the predicted species name
print("Predicted Species:", prediction[0])