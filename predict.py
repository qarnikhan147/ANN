"""
TASK 7: CREATE EVALUATION FUNCTION
This module provides the evaluate_student function that uses the trained ANN model
to predict performance for new students (not in training dataset).
"""

import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('model.joblib')
scaler = joblib.load('scaler.joblib')

def evaluate_student(attendance, assignment, quiz, mid, study_hours):
    """
    Task 7: ANN-based Student Performance Evaluator
    
    This function represents the learned ANN model.
    It can predict performance for new students not in the dataset.
    
    Args:
        attendance (float): Attendance percentage (0-100)
        assignment (float): Assignment marks (0-100)
        quiz (float): Quiz marks (0-100)
        mid (float): Mid-term marks (0-100)
        study_hours (float): Study hours per week (0-50)
    
    Returns:
        dict: Contains prediction result and confidence
              {
                  'result': 0 (Fail) or 1 (Pass),
                  'probability': confidence score (0-1),
                  'interpretation': readable result,
                  'confidence': confidence percentage
              }
    
    How it works:
    1. Take new student features as input
    2. Scale them using the training scaler (IMPORTANT!)
    3. Pass through the trained ANN
    4. Get prediction probabilities
    5. Return the most likely class and confidence
    """
    
    # Create feature array
    features = np.array([[attendance, assignment, quiz, mid, study_hours]])
    
    # Scale features using the training scaler
    features_scaled = scaler.transform(features)
    
    # Get prediction
    prediction = model.predict(features_scaled)[0]
    
    # Get prediction probability
    probabilities = model.predict_proba(features_scaled)[0]
    confidence = max(probabilities)
    
    # Convert prediction to readable format
    interpretation = "PASS ✅" if prediction == 1 else "FAIL ❌"
    
    return {
        'result': prediction,
        'probability': confidence,
        'interpretation': interpretation,
        'confidence_percent': confidence * 100,
        'fail_prob': probabilities[0] * 100,
        'pass_prob': probabilities[1] * 100
    }


# Example usage (for testing)
if __name__ == "__main__":
    print("Testing evaluate_student function...\n")
    
    # Example 1: Good student
    print("Example 1: Student with good attendance and study habits")
    result1 = evaluate_student(
        attendance=95,
        assignment=88,
        quiz=90,
        mid=85,
        study_hours=15
    )
    print(f"  Input: attendance=95, assignment=88, quiz=90, mid=85, study_hours=15")
    print(f"  Prediction: {result1['interpretation']}")
    print(f"  Confidence: {result1['confidence_percent']:.2f}%")
    print(f"  Pass Probability: {result1['pass_prob']:.2f}%\n")
    
    # Example 2: Weak student
    print("Example 2: Student with low attendance and study time")
    result2 = evaluate_student(
        attendance=45,
        assignment=50,
        quiz=48,
        mid=55,
        study_hours=3
    )
    print(f"  Input: attendance=45, assignment=50, quiz=48, mid=55, study_hours=3")
    print(f"  Prediction: {result2['interpretation']}")
    print(f"  Confidence: {result2['confidence_percent']:.2f}%")
    print(f"  Pass Probability: {result2['pass_prob']:.2f}%\n")
    
    # Example 3: Average student
    print("Example 3: Student with average performance")
    result3 = evaluate_student(
        attendance=70,
        assignment=72,
        quiz=75,
        mid=70,
        study_hours=8
    )
    print(f"  Input: attendance=70, assignment=72, quiz=75, mid=70, study_hours=8")
    print(f"  Prediction: {result3['interpretation']}")
    print(f"  Confidence: {result3['confidence_percent']:.2f}%")
    print(f"  Pass Probability: {result3['pass_prob']:.2f}%")
