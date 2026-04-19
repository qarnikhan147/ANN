"""
TASK 9: BUILD USER INTERFACE
Streamlit-based UI for student performance prediction using trained ANN.
Run with: streamlit run app.py
"""

import streamlit as st
import joblib
import numpy as np
import pandas as pd
from predict import evaluate_student

# Page configuration
st.set_page_config(
    page_title="ANN Student Evaluator",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        color: #1f77b4;
        text-align: center;
        padding: 20px;
        border-bottom: 3px solid #1f77b4;
    }
    .metric-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .pass-card {
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        padding: 15px;
        border-radius: 5px;
    }
    .fail-card {
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
        padding: 15px;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="main-header">
        <h1>🎓 ANN-Based Student Performance Evaluator</h1>
        <p><i>Using Artificial Neural Networks for Performance Prediction</i></p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar - Information
with st.sidebar:
    st.markdown("## 📚 About This Tool")
    st.info("""
    This tool uses an **Artificial Neural Network (ANN)** trained on student data 
    to predict whether a student will **PASS** or **FAIL**.
    
    **Input Features:**
    - Attendance (0-100%)
    - Assignment Marks (0-100)
    - Quiz Marks (0-100)
    - Mid-term Marks (0-100)
    - Study Hours/Week (0-50)
    
    **Model:**
    - Type: Classification
    - Architecture: 5→16→8→2
    - Activation: ReLU (hidden), Softmax (output)
    """)
    
    st.markdown("---")
    st.markdown("### 🔍 Model Information")
    try:
        model = joblib.load('model.joblib')
        scaler = joblib.load('scaler.joblib')
        st.success("✅ Model Loaded Successfully")
        st.caption(f"Solver: {model.solver}")
        st.caption(f"Layers: {model.hidden_layer_sizes}")
    except:
        st.error("❌ Model files not found!")

# Main content - Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🎯 Predictor", "📊 Batch Evaluation", "📖 How It Works", "❓ FAQ"])

with tab1:
    st.markdown("## 🎯 Single Student Evaluation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Input Student Information")
        
        attendance = st.slider(
            "📍 Attendance (%)",
            min_value=0,
            max_value=100,
            value=75,
            step=1,
            help="Student's attendance percentage in the course"
        )
        
        assignment = st.slider(
            "📝 Assignment Marks",
            min_value=0,
            max_value=100,
            value=70,
            step=1,
            help="Total marks obtained in assignments"
        )
        
        quiz = st.slider(
            "❓ Quiz Marks",
            min_value=0,
            max_value=100,
            value=72,
            step=1,
            help="Total marks obtained in quizzes"
        )
        
        mid = st.slider(
            "📚 Mid-term Marks",
            min_value=0,
            max_value=100,
            value=75,
            step=1,
            help="Mid-term examination marks"
        )
        
        study_hours = st.slider(
            "⏱️ Study Hours/Week",
            min_value=0,
            max_value=50,
            value=8,
            step=0.5,
            help="Average hours spent studying per week"
        )
    
    # Prediction
    with col2:
        st.markdown("### PREDICTION RESULT")
        
        # Get prediction
        result = evaluate_student(attendance, assignment, quiz, mid, study_hours)
        
        # Display result
        if result['result'] == 1:  # Pass
            st.markdown(f"""
                <div class="pass-card">
                    <h2>✅ PASS</h2>
                    <p><b>Confidence: {result['confidence_percent']:.2f}%</b></p>
                </div>
                """, unsafe_allow_html=True)
        else:  # Fail
            st.markdown(f"""
                <div class="fail-card">
                    <h2>❌ FAIL</h2>
                    <p><b>Confidence: {result['confidence_percent']:.2f}%</b></p>
                </div>
                """, unsafe_allow_html=True)
        
        # Probability breakdown
        st.markdown("### Probability Breakdown")
        col_fail, col_pass = st.columns(2)
        with col_fail:
            st.metric("Fail Probability", f"{result['fail_prob']:.2f}%")
        with col_pass:
            st.metric("Pass Probability", f"{result['pass_prob']:.2f}%")
        
        # Interpretation
        st.markdown("### Detection Analysis")
        col_metrics = st.columns(3)
        with col_metrics[0]:
            st.metric("Attendance Score", f"{attendance}%")
        with col_metrics[1]:
            st.metric("Average Score", f"{(assignment + quiz + mid) / 3:.1f}")
        with col_metrics[2]:
            st.metric("Study Hours", f"{study_hours}h/week")

# Tab 2: Batch Evaluation
with tab2:
    st.markdown("## 📊 Batch Student Evaluation")
    st.info("Evaluate multiple students at once by uploading an Excel file")
    
    uploaded_file = st.file_uploader(
        "Upload Excel file with student data",
        type="xlsx",
        help="Columns: attendance, assignment, quiz, mid, study_hours"
    )
    
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            
            # Validate columns
            required_cols = ['attendance', 'assignment', 'quiz', 'mid', 'study_hours']
            if all(col in df.columns for col in required_cols):
                
                # Evaluate all students
                results = []
                for idx, row in df.iterrows():
                    pred = evaluate_student(
                        row['attendance'],
                        row['assignment'],
                        row['quiz'],
                        row['mid'],
                        row['study_hours']
                    )
                    results.append({
                        'Student': f"S{idx+1}",
                        'Attendance': row['attendance'],
                        'Assignment': row['assignment'],
                        'Quiz': row['quiz'],
                        'Mid': row['mid'],
                        'Study Hours': row['study_hours'],
                        'Prediction': pred['interpretation'],
                        'Confidence': f"{pred['confidence_percent']:.2f}%",
                        'Pass Prob': f"{pred['pass_prob']:.2f}%"
                    })
                
                result_df = pd.DataFrame(results)
                st.dataframe(result_df, use_container_width=True)
                
                # Statistics
                col1, col2, col3 = st.columns(3)
                total_students = len(result_df)
                pass_count = result_df['Prediction'].str.contains('PASS').sum()
                fail_count = total_students - pass_count
                
                with col1:
                    st.metric("Total Students", total_students)
                with col2:
                    st.metric("Predicted Pass", pass_count)
                with col3:
                    st.metric("Predicted Fail", fail_count)
                
                # Download results
                csv = result_df.to_csv(index=False)
                st.download_button(
                    label="📥 Download Results",
                    data=csv,
                    file_name="evaluation_results.csv",
                    mime="text/csv"
                )
            else:
                st.error(f"Missing columns! Required: {', '.join(required_cols)}")
        except Exception as e:
            st.error(f"Error processing file: {e}")

# Tab 3: How It Works
with tab3:
    st.markdown("## 📖 How the ANN Works")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🧠 Neural Network Architecture
        
        **Input Layer (5 neurons)**
        - attendance
        - assignment
        - quiz
        - mid-term
        - study_hours
        
        ⬇️
        
        **Hidden Layer 1 (16 neurons)**
        - ReLU activation
        - Learns feature combinations
        
        ⬇️
        
        **Hidden Layer 2 (8 neurons)**
        - ReLU activation
        - Further pattern refinement
        
        ⬇️
        
        **Output Layer (2 neurons)**
        - Softmax activation
        - Class probabilities (Fail/Pass)
        """)
    
    with col2:
        st.markdown("""
        ### 🔎 Key Concepts
        
        **What is an ANN?**
        - Network of interconnected neurons
        - Learns from data to approximate complex functions
        - Inspired by biological neural networks
        
        **Neurons**
        - Basic computation units
        - Receive weighted inputs
        - Apply activation function
        - Pass output forward
        
        **Activation Functions**
        - ReLU: max(0, x) - Introduces non-linearity
        - Softmax: Converts scores to probabilities
        
        **Training**
        - Adjusts weights to minimize prediction error
        - Uses gradient descent optimization (Adam)
        """)
    
    st.divider()
    
    st.markdown("""
    ### 📊 The Learning Process
    
    1. **Load Data**: Read student performance data
    2. **Preprocessing**: Scale features to normalize ranges
    3. **Split**: 80% training, 20% testing
    4. **Build**: Create multi-layer network
    5. **Train**: Adjust weights using training data
    6. **Evaluate**: Test on unseen data
    7. **Deploy**: Use model to predict for new students
    """)

# Tab 4: FAQ
with tab4:
    st.markdown("## ❓ Frequently Asked Questions")
    
    with st.expander("❓ What is an Artificial Neural Network (ANN)?"):
        st.write("""
        An Artificial Neural Network is a machine learning model inspired by how 
        the brain works. It consists of:
        - **Neurons**: Units that process information
        - **Connections**: Weighted links between neurons
        - **Layers**: Organized rows of neurons
        
        The network learns by adjusting weights during training to minimize errors.
        """)
    
    with st.expander("❓ What function did the model learn?"):
        st.write("""
        The model learned a function: f(X) → Y
        
        Where:
        - **X** = [attendance, assignment, quiz, mid, study_hours]
        - **Y** = Probability of passing (0-1)
        
        This function is encoded in the network's weights and biases 
        across 2 hidden layers.
        """)
    
    with st.expander("❓ How does the system evaluate a new student?"):
        st.write("""
        1. Accept student feature values
        2. Scale features using training data statistics (mean/std)
        3. Pass through the trained neural network
        4. Output probabilities for each class
        5. Select class with higher probability
        6. Return prediction and confidence
        """)
    
    with st.expander("❓ Why is feature scaling important?"):
        st.write("""
        **Scaling normalizes features to similar ranges:**
        
        Without scaling:
        - Feature ranges vary (attendance 0-100, study_hours 0-50)
        - Network learns poorly
        - Training is slow and unstable
        
        With scaling:
        - All features have mean=0, std=1
        - Gradients are balanced
        - Training converges faster and better
        """)
    
    with st.expander("❓ What are the model limitations?"):
        st.write("""
        1. **Limited to training data**: Can only predict within ranges seen during training
        2. **Overfitting risk**: May memorize training data instead of learning patterns
        3. **Black box**: Hard to explain why it makes specific predictions
        4. **Data quality**: Performance depends on data quality and quantity
        5. **Feature engineering**: Success depends on relevant features
        6. **Class imbalance**: If one class dominates, predictions may be biased
        """)
    
    with st.expander("❓ How to improve the model?"):
        st.write("""
        1. **Collect more data**: Larger datasets improve generalization
        2. **Feature engineering**: Add relevant features
        3. **Hyperparameter tuning**: Adjust layers, neurons, learning rate
        4. **Balance data**: Ensure equal representation of both classes
        5. **Cross-validation**: Better estimate of real performance
        6. **Ensemble methods**: Combine multiple models
        7. **Different architectures**: Try TensorFlow/Keras for more flexibility
        """)

# Footer
st.divider()
st.markdown("""
    <center>
    <p style="color: gray; font-size: 12px;">
    🎓 ANN Student Evaluator | Predicting Student Performance Using Neural Networks
    </p>
    </center>
    """, unsafe_allow_html=True)
