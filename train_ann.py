"""
TASK 1, 2, 3, 4, 5, 6: Load Data, Preprocess, Build and Train ANN
This script handles data loading, preprocessing, model building, and training.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib
import matplotlib.pyplot as plt

# ============================================================================
# TASK 1: UNDERSTAND THE DATASET (What)
# ============================================================================

print("=" * 80)
print("TASK 1: UNDERSTANDING THE DATASET")
print("=" * 80)

# Load the Excel file
df = pd.read_excel('synthetic_student_data.xlsx')  # Updated to use your real data

print("\n📊 DATASET OVERVIEW:")
print(f"Shape: {df.shape} (rows, columns) - Your real student data!")
print(f"\nColumn Names: {list(df.columns)}")

print("\n📋 FIRST 5 ROWS:")
print(df.head())

print("\n📈 DATASET STATISTICS:")
print(df.describe())

print("\n❓ DATA TYPES:")
print(df.dtypes)

print("\n✅ MISSING VALUES:")
print(df.isnull().sum())

# ============================================================================
# IDENTIFY FEATURES AND TARGET
# ============================================================================

print("\n" + "=" * 80)
print("IDENTIFYING FEATURES (X) AND TARGET (Y)")
print("=" * 80)

# Features: everything except 'result'
X = df[['attendance', 'assignment', 'quiz', 'mid', 'study_hours']]
y = df['result']  # Target: Pass (0) or Fail (1) - Classification problem

print("\n🔹 Input Features (X):")
print(f"  - attendance: Student attendance percentage")
print(f"  - assignment: Assignment marks")
print(f"  - quiz: Quiz marks")
print(f"  - mid: Mid-term marks")
print(f"  - study_hours: Hours studied per week")

print("\n🔹 Target Variable (y):")
print(f"  - result: 0=Fail, 1=Pass")

print("\nTarget Distribution:")
print(y.value_counts())
print(f"\nPass Rate: {(y.sum() / len(y) * 100):.2f}% (from your real data)")

print("\n❓ PROBLEM TYPE: CLASSIFICATION ✓")
print("Justification: We're predicting discrete classes (Pass/Fail), not continuous values.")

# ============================================================================
# TASK 3: DATA PREPROCESSING (How)
# ============================================================================

print("\n" + "=" * 80)
print("TASK 3: DATA PREPROCESSING")
print("=" * 80)

print("\n🔄 Splitting Dataset (80% train, 20% test)...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training set size: {len(X_train)} samples")
print(f"Testing set size: {len(X_test)} samples")

# ============================================================================
# SCALING EXPLANATION
# ============================================================================

print("\n📌 WHY DO WE SCALE DATA IN ANN?")
print("""
1. Neural networks use gradient descent optimization
2. Features with different scales (e.g., attendance 0-100, study_hours 0-10)
   can cause slow convergence and unstable training
3. Scaling brings all features to similar range (mean=0, std=1)
4. Results in faster training and better performance
5. StandardScaler: (x - mean) / std_dev
""")

print("\n🔄 Applying StandardScaler...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Sample scaled values:\n{X_train_scaled[:3]}")

# ============================================================================
# TASK 4: BUILD ANN MODEL
# ============================================================================

print("\n" + "=" * 80)
print("TASK 4: BUILDING THE ANN MODEL")
print("=" * 80)

print("\n📚 ANN COMPONENTS EXPLANATION:")
print("""
1. INPUT LAYER: 5 neurons (one for each feature)
   - attendance, assignment, quiz, mid, study_hours

2. HIDDEN LAYERS: 
   - Layer 1: 16 neurons with ReLU activation
   - Layer 2: 8 neurons with ReLU activation
   
3. OUTPUT LAYER: 2 neurons (softmax for classification)
   - Neuron 1: Probability of class 0 (Fail)
   - Neuron 2: Probability of class 1 (Pass)

4. ACTIVATION FUNCTIONS:
   - ReLU (hidden): Introduces non-linearity, f(x) = max(0, x)
   - Softmax (output): Converts scores to probabilities
   
5. NEURONS: 
   - Basic units that receive inputs, apply weights, and activation
   - 5 → 16 → 8 → 2 architecture (pyramid shape)
""")

# Create the model
model = MLPClassifier(
    hidden_layer_sizes=(16, 8),  # Two hidden layers: 16 and 8 neurons
    activation='relu',            # ReLU activation for hidden layers
    solver='adam',                # Adam optimizer
    max_iter=500,                 # Maximum iterations
    learning_rate_init=0.001,     # Learning rate
    random_state=42,
    verbose=1,
    early_stopping=True,          # Stop if not improving
    validation_fraction=0.1,
    n_iter_no_change=20
)

print("\n🔧 MODEL CONFIGURATION:")
print(f"  - Hidden layers: {model.hidden_layer_sizes}")
print(f"  - Activation: {model.activation}")
print(f"  - Solver: {model.solver}")
print(f"  - Max iterations: {model.max_iter}")

# ============================================================================
# TASK 5: TRAIN THE MODEL
# ============================================================================

print("\n" + "=" * 80)
print("TASK 5: TRAINING THE ANN MODEL")
print("=" * 80)

print("\n🚀 Starting training...")
model.fit(X_train_scaled, y_train)

print("\n✅ TRAINING COMPLETED")
print(f"Iterations completed: {model.n_iter_}")
print(f"Converged: {model.n_iter_ < model.max_iter}")
print(f"Training loss: {model.loss_:.4f}")

# ============================================================================
# TASK 6: EVALUATE MODEL (Why)
# ============================================================================

print("\n" + "=" * 80)
print("TASK 6: EVALUATING THE MODEL")
print("=" * 80)

# Predictions
y_train_pred = model.predict(X_train_scaled)
y_test_pred = model.predict(X_test_scaled)

# Accuracy
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

print(f"\n📊 ACCURACY SCORES:")
print(f"  Training Accuracy: {train_accuracy:.4f} ({train_accuracy*100:.2f}%)")
print(f"  Testing Accuracy:  {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")

print("\n❓ WHAT DOES ACCURACY MEAN?")
print(f"""
Accuracy = (Correct Predictions) / (Total Predictions)
Accuracy = {test_accuracy:.4f}
This means the model correctly predicts student performance {test_accuracy*100:.2f}% of the time.
""")

# Confusion Matrix
print("\n🔴 CONFUSION MATRIX (Test Set):")
cm = confusion_matrix(y_test, y_test_pred)
print(cm)
print(f"\nTP (True Pass):  {cm[1,1]} students correctly predicted as Pass")
print(f"TN (True Fail):  {cm[0,0]} students correctly predicted as Fail")
print(f"FP (False Pass): {cm[0,1]} students incorrectly predicted as Pass (should be Fail)")
print(f"FN (False Fail): {cm[1,0]} students incorrectly predicted as Fail (should be Pass)")

# Classification Report
print("\n📈 CLASSIFICATION REPORT:")
print(classification_report(y_test, y_test_pred, target_names=['Fail', 'Pass']))

print("\n❓ WHAT MISTAKES IS THE MODEL MAKING?")
if cm[0,1] > 0:
    print(f"  - {cm[0,1]} False Positives: Predicting PASS when actual is FAIL")
    print(f"    (Risky - student might fail but we said pass)")
if cm[1,0] > 0:
    print(f"  - {cm[1,0]} False Negatives: Predicting FAIL when actual is PASS")
    print(f"    (Conservative - student might pass but we said fail)")

# ============================================================================
# SAVE THE MODEL AND SCALER
# ============================================================================

print("\n" + "=" * 80)
print("TASK 8: SAVING MODEL AND SCALER")
print("=" * 80)

joblib.dump(model, 'model.joblib')
joblib.dump(scaler, 'scaler.joblib')

print("\n✅ MODEL SAVED: model.joblib")
print("✅ SCALER SAVED: scaler.joblib")

print("\n❓ WHY SAVE BOTH MODEL AND SCALER?")
print("""
We must save BOTH because:
1. MODEL: Contains learned patterns (weights and biases)
2. SCALER: Contains training data statistics (mean and std_dev)

When predicting for new students:
- We must use THE SAME scaler that trained the model
- Otherwise, new features won't be in the same scale
- This would give incorrect predictions
""")

print("\n" + "=" * 80)
print("ALL TASKS COMPLETED ✅")
print("=" * 80)
