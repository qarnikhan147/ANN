"""
Analyze the user's real student data file
"""

import pandas as pd
import numpy as np

# Read the user's data
try:
    df = pd.read_excel('synthetic_student_data.xlsx')
    print("✅ Successfully loaded your data!")
    print(f"📊 Shape: {df.shape} (rows, columns)")
    print(f"\n📋 Column Names: {list(df.columns)}")

    print(f"\n📋 First 5 rows:")
    print(df.head())

    print(f"\n📈 Data Statistics:")
    print(df.describe())

    print(f"\n❓ Data Types:")
    print(df.dtypes)

    print(f"\n✅ Missing Values:")
    print(df.isnull().sum())

    # Check for result column
    if 'result' in df.columns:
        print(f"\n📊 Result Distribution:")
        result_counts = df['result'].value_counts()
        print(result_counts)
        print(f"Pass Rate: {(result_counts.get(1, 0) / len(df) * 100):.2f}%")

    # Check for required columns
    required_cols = ['attendance', 'assignment', 'quiz', 'mid', 'study_hours', 'result']
    missing_cols = [col for col in required_cols if col not in df.columns]

    if missing_cols:
        print(f"\n⚠️  Missing required columns: {missing_cols}")
        print("Available columns:", list(df.columns))
    else:
        print(f"\n✅ All required columns present!")

except Exception as e:
    print(f"❌ Error reading file: {e}")
    print("Make sure the file 'synthetic_student_data.xlsx' exists in the current directory")