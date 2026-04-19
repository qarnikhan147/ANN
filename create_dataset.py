"""
Create sample dataset for student performance evaluation
This script generates a realistic Excel file with student data.
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample student data
n_students = 100

# Create realistic data
attendance = np.random.normal(72, 15, n_students)
attendance = np.clip(attendance, 0, 100)  # Clip to 0-100 range

assignment = np.random.normal(70, 15, n_students)
assignment = np.clip(assignment, 0, 100)

quiz = np.random.normal(68, 16, n_students)
quiz = np.clip(quiz, 0, 100)

mid = np.random.normal(70, 18, n_students)
mid = np.clip(mid, 0, 100)

study_hours = np.random.exponential(6, n_students)
study_hours = np.clip(study_hours, 0, 50)

# Generate target: Pass/Fail based on weighted combination of features
# This creates a realistic relationship between features and outcome
weights = {
    'attendance': 0.2,
    'assignment': 0.2,
    'quiz': 0.2,
    'mid': 0.2,
    'study_hours': 0.2  # 2 hours per week = 20 points
}

# Calculate score
score = (
    weights['attendance'] * (attendance / 100) * 100 +
    weights['assignment'] * (assignment / 100) * 100 +
    weights['quiz'] * (quiz / 100) * 100 +
    weights['mid'] * (mid / 100) * 100 +
    weights['study_hours'] * (study_hours * 2)  # study_hours contribution
)

# Add some noise
score += np.random.normal(0, 5, n_students)

# Threshold for pass (typically 50%)
result = (score >= 50).astype(int)

# Create DataFrame
df = pd.DataFrame({
    'attendance': attendance.round(1),
    'assignment': assignment.round(1),
    'quiz': quiz.round(1),
    'mid': mid.round(1),
    'study_hours': study_hours.round(1),
    'result': result
})

# Save to Excel
df.to_excel('dataset.xlsx', index=False)

print("✅ Dataset created successfully!")
print(f"📊 Shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\n📊 Statistics:")
print(df.describe())
print(f"\n📈 Result Distribution:")
print(f"Fail (0): {(result == 0).sum()} students ({(result == 0).sum() / len(result) * 100:.1f}%)")
print(f"Pass (1): {(result == 1).sum()} students ({(result == 1).sum() / len(result) * 100:.1f}%)")
