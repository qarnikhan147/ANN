# 🎓 ANN-Based Student Performance Evaluator

## 📋 Project Overview

This is a complete machine learning project that uses an **Artificial Neural Network (ANN)** to predict student academic performance (Pass/Fail) based on five input features.

**Key Features:**
- ✅ Trained ANN with 77.5% training accuracy and 80% testing accuracy
- ✅ Interactive Streamlit web interface
- ✅ Batch prediction capability
- ✅ Comprehensive documentation and explanations
- ✅ Production-ready code with model persistence

---

## 📂 Project Structure

```
ANN/
├── .venv/                    # Python virtual environment (auto-created)
│
├── 📊 DATA FILES
├── create_dataset.py         # Script to generate sample dataset
├── dataset.xlsx              # 100 student records (pre-generated)
│
├── 🧠 MODEL FILES
├── train_ann.py              # Complete training pipeline
├── model.joblib              # Trained ANN model (auto-generated)
├── scaler.joblib             # Feature scaler (auto-generated)
│
├── 🔮 PREDICTION FILES
├── predict.py                # Evaluation function for new students
│
├── 🎨 USER INTERFACE
├── app.py                    # Streamlit web application
│
├── 📚 DOCUMENTATION
├── requirements.txt          # Python package dependencies
├── README.md                 # This file
└── EXPLANATION.md            # Detailed assignment explanations
```

---

## 🚀 Quick Start

### 1. **Setup Environment** (One-time)

```bash
# Navigate to project directory
cd d:\ANN

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. **Generate Dataset** (If needed)

```bash
python create_dataset.py
```

Output:
- ✅ `dataset.xlsx` with 100 student records
- 📊 Statistics and distribution info

### 3. **Train the ANN Model** (One-time)

```bash
python train_ann.py
```

This performs all these tasks:
- ✅ Task 1: Load & understand dataset
- ✅ Task 2: Preprocess data
- ✅ Task 3: Build ANN architecture
- ✅ Task 4: Train with gradient descent
- ✅ Task 5: Evaluate performance
- ✅ Task 6: Save model & scaler

**Output:**
```
✅ TRAINING COMPLETED
Iterations completed: 58
Training Accuracy: 87.50%
Testing Accuracy:  89.17%
Model saved: model.joblib
Scaler saved: scaler.joblib
```

### 4. **Launch Web Interface**

```bash
streamlit run app.py
```

Opens at: `http://localhost:8501`

---

## 📊 Model Architecture

```
INPUT LAYER (5 features)
    ↓
HIDDEN LAYER 1: 16 neurons + ReLU activation
    ↓
HIDDEN LAYER 2: 8 neurons + ReLU activation
    ↓
OUTPUT LAYER: 2 neurons + Softmax activation
    ↓
CLASS PROBABILITIES: [P(Fail), P(Pass)]
```

**Model Specification:**
| Parameter | Value |
|-----------|-------|
| Input Features | 5 (attendance, assignment, quiz, mid, study_hours) |
| Hidden Layers | 2 |
| Hidden Neurons | 16, 8 |
| Activation | ReLU (hidden), Softmax (output) |
| Optimizer | Adam |
| Loss Function | Cross-Entropy |
| Training Accuracy | 77.5% |
| Testing Accuracy | 80.0% |

---

## 💾 Dataset Description

### Input Features (X):
| Feature | Range | Description |
|---------|-------|-------------|
| **attendance** | 0-100% | Class attendance percentage |
| **assignment** | 0-100 | Assignment marks |
| **quiz** | 0-100 | Quiz marks |
| **mid** | 0-100 | Mid-term exam marks |
| **study_hours** | 0-50 | Weekly study hours |

### Target Variable (y):
| Value | Meaning |
|-------|---------|
| **0** | FAIL ❌ |
| **1** | PASS ✅ |

### Dataset Statistics:
```
Source: Your real student data (600 records)
Total Students: 600
Pass Rate: 53.67%
Fail Rate: 46.33%

Train Set: 480 students (80%)
Test Set:  120 students (20%)
```

---

## 🧠 How to Use the System

### Option 1: Command-Line Prediction

```python
from predict import evaluate_student

# Test a student
result = evaluate_student(
    attendance=85,
    assignment=80,
    quiz=82,
    mid=78,
    study_hours=10
)

print(f"Prediction: {result['interpretation']}")
print(f"Confidence: {result['confidence_percent']:.2f}%")
print(f"Pass Probability: {result['pass_prob']:.2f}%")
```

### Option 2: Web Interface (Recommended)

**Run:**
```bash
streamlit run app.py
```

**Features:**
- 🎯 **Predictor Tab**: Evaluate single student
- 📊 **Batch Evaluation**: Upload Excel file with multiple students
- 📖 **How It Works**: Learn about ANN concepts
- ❓ **FAQ**: Answer common questions

---

## 📈 Model Performance

### Accuracy Metrics

```
Training Accuracy: 87.50%
Testing Accuracy:  89.17%
```

### Confusion Matrix (Test Set)

```
           Predicted
           Fail  Pass
Actual  Fail  48    8     (48 True Negatives, 8 False Positives)
        Pass   5   59     (59 True Positives, 5 False Negatives)
```

### Classification Report

```
         Precision  Recall  F1-Score  Support
Fail         0.91    0.86     0.88      56
Pass         0.88    0.92     0.90      64
```

### Interpretation

- ✅ **Excellent Performance**: 89.17% overall accuracy
- ✅ **Balanced Results**: Good performance on both pass and fail predictions
- ✅ **High Precision & Recall**: Model correctly identifies both classes
- ✅ **Real Data Advantage**: Much better than synthetic data results

---

## 🔧 Technical Details

### Feature Scaling

**Why?** Neural networks require normalized inputs:
- Prevents gradient explosion
- Ensures equal feature importance
- Speeds up convergence

**Method:** StandardScaler
```python
scaled = (original - mean) / std_dev
```

### Training Process

1. **Data Split**: 80% train, 20% test
2. **Initialization**: Random weight initialization
3. **Forward Pass**: Compute layer outputs
4. **Loss Calculation**: Cross-entropy from actual vs. predicted
5. **Backward Pass**: Compute gradients
6. **Weight Update**: Gradient descent optimization
7. **Validation**: Monitor on validation set
8. **Early Stopping**: Stop if no improvement

**Convergence:**
- Started: Loss = 0.5958
- Ended: Loss = 0.4914
- Iterations: 30 / 500 (early stopped at epoch 30)

---

## 📚 Educational Value

This project teaches:

| Concept | Coverage |
|---------|----------|
| **Neural Networks** | Architecture, neurons, layers, weights |
| **Activation Functions** | ReLU, Softmax |
| **Optimization** | Gradient descent, Adam optimizer |
| **Data Preprocessing** | Scaling, normalization, train/test split |
| **Model Evaluation** | Accuracy, confusion matrix, F1-score |
| **Model Persistence** | Saving and loading models |
| **Deployment** | Web UI with Streamlit |
| **Python** | scikit-learn, pandas, numpy |

---

## ⚠️ Limitations & Future Improvements

### Current Limitations:
1. **Small Dataset**: Only 100 samples
2. **Class Imbalance**: 86% pass vs. 14% fail
3. **Limited Features**: Only 5 features
4. **Black Box**: Hard to explain predictions
5. **Static Model**: Doesn't adapt to new data

### Improvements:
- [ ] Collect more training data (500+ samples)
- [ ] Balance dataset with SMOTE oversampling
- [ ] Add more features (GPA history, study resources, etc.)
- [ ] Try TensorFlow/Keras for deeper networks
- [ ] Implement SHAP for model explainability
- [ ] Add continuous retraining pipeline
- [ ] Compare with other models (Random Forest, XGBoost)
- [ ] Implement cross-validation

---

## 🎯 Real-World Applications

This system can be used for:
- 📚 **Academic Planning**: Identify at-risk students early
- 🎓 **Intervention Programs**: Target students who need support
- 📊 **Admissions**: Predict success of applicants
- 📈 **Curriculum Design**: Improve course effectiveness
- 👥 **Personalized Learning**: Tailor content for each student

---

## 📖 Files Explanation

### `create_dataset.py`
Generates `dataset.xlsx` with realistic student data
- 100 student records
- Realistic feature distributions
- Balanced/imbalanced outcome
- Reproducible (fixed random seed)

### `train_ann.py`
Complete machine learning pipeline
- Loads and explores data (Task 1)
- Preprocesses and scales features (Task 3)
- Builds 5→16→8→2 ANN (Task 4)
- Trains with validation (Task 5)
- Evaluates performance (Task 6)
- Saves model and scaler (Task 8)

### `predict.py`
Production prediction module
- Loads trained model and scaler
- Defines `evaluate_student()` function (Task 7)
- Returns prediction with confidence
- Can be imported in other scripts

### `app.py`
Interactive Streamlit web application (Task 9)
- Single student prediction
- Batch student evaluation
- Educational content
- FAQ section

### `EXPLANATION.md`
Detailed assignment responses
- What is ANN (conceptual)
- Function learned by model
- Evaluation process
- Why scaling matters
- Model limitations

### `requirements.txt`
All Python package dependencies
- pandas: Data manipulation
- numpy: Numerical computing
- scikit-learn: ML models
- matplotlib: Visualization
- streamlit: Web framework
- openpyxl: Excel handling
- joblib: Model serialization

---

## 🔍 Troubleshooting

### Problem: "Model files not found"
**Solution:** Run `python train_ann.py` first

### Problem: Streamlit not starting
**Solution:** Ensure streamlit is installed: `pip install streamlit`

### Problem: "ModuleNotFoundError"
**Solution:** Activate venv: `venv\Scripts\activate`

### Problem: "Excel file not found"
**Solution:** Run `python create_dataset.py` to generate it

---

## 📞 Support & Questions

For detailed explanations, see `EXPLANATION.md`:
- **What is ANN?** → Section 1
- **What function did model learn?** → Section 2
- **How does evaluation work?** → Section 3
- **Why is scaling important?** → Section 4
- **What are limitations?** → Section 5

---

## 🎓 Learning Outcomes

After completing this project, you should understand:

1. ✅ How neural networks learn from data
2. ✅ The role of hidden layers and activation functions
3. ✅ Why feature scaling matters
4. ✅ How to evaluate classification models
5. ✅ How to save and load trained models
6. ✅ How to build a practical ML system
7. ✅ How to create a user-friendly interface
8. ✅ Limitations and best practices of ANNs

---

## 📝 License

This project is for educational purposes.

---

## 🙏 Credits

Created as part of ANN (Artificial Neural Networks) course assignment.

**Technologies Used:**
- Python 3.13
- scikit-learn (ML)
- pandas & numpy (Data)
- Streamlit (Web UI)
- joblib (Model persistence)

---

**Last Updated:** April 19, 2026  
**Status:** ✅ Complete
