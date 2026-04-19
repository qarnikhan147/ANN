# 🚀 HOW TO RUN THE PROJECT

## Step 1: Navigate to Project Directory

```bash
cd d:\ANN
```

## Step 2: Activate Virtual Environment

```bash
venv\Scripts\activate
```

You should see `(venv)` at the start of your terminal.

## Step 3: Launch Streamlit Web Interface

```bash
streamlit run app.py
```

### What happens:
- Opens web browser to `http://localhost:8501`
- Loads the trained ANN model
- Ready for predictions!

## Step 4: Using the Web Interface

### 🎯 Predictor Tab
1. Adjust sliders for student information:
   - Attendance (0-100%)
   - Assignment marks (0-100)
   - Quiz marks (0-100)
   - Mid-term marks (0-100)
   - Study hours/week (0-50)
2. Instant prediction appears on the right
3. See confidence level and probability breakdown

### 📊 Batch Evaluation Tab
1. Upload Excel file with student data
2. Required columns: `attendance, assignment, quiz, mid, study_hours`
3. System evaluates all students automatically
4. Download results as CSV

### 📖 How It Works Tab
- Learn about ANN architecture
- Understand the learning process
- See key concepts explained

### ❓ FAQ Tab
- What is an ANN?
- What function did the model learn?
- How does evaluation work?
- Why is scaling important?
- What are limitations?
- How to improve?

---

## 📊 Testing Examples

### Example 1: Good Student (Should PASS)
- Attendance: 90%
- Assignment: 85
- Quiz: 88
- Mid: 85
- Study Hours: 12

### Example 2: At-Risk Student (May FAIL)
- Attendance: 50%
- Assignment: 55
- Quiz: 48
- Mid: 60
- Study Hours: 2

### Example 3: Average Student (Should PASS)
- Attendance: 75%
- Assignment: 75
- Quiz: 75
- Mid: 75
- Study Hours: 8

---

## 🔄 If You Need to Retrain

```bash
# Run training with full output
python train_ann.py

# You'll see:
# - Dataset analysis
# - Training progress
# - Final accuracy (80%)
# ✅ Both model.joblib and scaler.joblib will be updated
```

## 🆕 If You Need New Dataset

```bash
# Generate fresh dataset with 100 random students
python create_dataset.py

# Then retrain:
python train_ann.py
```

---

## ⚙️ Installation (First Time Only)

```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import pandas, sklearn, streamlit; print('✅ All packages installed!')"
```

---

## 🐛 Troubleshooting

### Streamlit won't start
```bash
pip install --upgrade streamlit
streamlit run app.py
```

### ModuleNotFoundError
```bash
# Make sure venv is activated
venv\Scripts\activate

# Reinstall packages
pip install -r requirements.txt
```

### "model.joblib not found"
```bash
# Run training first
python train_ann.py

# Creates model.joblib and scaler.joblib
```

### Port 8501 already in use
```bash
streamlit run app.py --server.port 8502
```

---

## 📱 Accessing from Other Computers

If both computers are on same network:

```bash
streamlit run app.py --server.address 0.0.0.0
```

Then access from other computer at:
```
http://<your-computer-ip>:8501
```

---

## 📊 Quick Command Reference

| Task | Command |
|------|---------|
| **Activate venv** | `venv\Scripts\activate` |
| **Train model** | `python train_ann.py` |
| **Generate data** | `python create_dataset.py` |
| **Launch web UI** | `streamlit run app.py` |
| **Test prediction** | `python predict.py` |
| **Deactivate venv** | `deactivate` |

---

## ✅ Verification Checklist

- [ ] Virtual environment activated (`(venv)` in terminal)
- [ ] All packages installed (`pip list` shows pandas, sklearn, streamlit)
- [ ] Dataset exists (`dataset.xlsx` in folder)
- [ ] Model trained (`model.joblib` file exists)
- [ ] Scaler saved (`scaler.joblib` file exists)
- [ ] Streamlit running on `http://localhost:8501`
- [ ] Can enter student data and get predictions
- [ ] Can upload batch Excel file (Tab 2)

---

## 📚 Project Files Quick Reference

| File | Purpose | When Run |
|------|---------|----------|
| `create_dataset.py` | Generate test data | Once (optional) |
| `train_ann.py` | Train ANN model | Once initially, then if retrain needed |
| `predict.py` | Evaluation function | Imported by app.py |
| `app.py` | Web interface | Always (main entry point) |
| `model.joblib` | Trained weights | Auto-loaded when app starts |
| `scaler.joblib` | Feature scaler | Auto-loaded when app starts |
| `dataset.xlsx` | Student data | Training data |

---

## 🎓 Learning Path

1. **First**: Read `README.md` to understand project
2. **Second**: Review `train_ann.py` to see how model is trained
3. **Third**: Check `EXPLANATION.md` for detailed answers
4. **Finally**: Run `streamlit run app.py` and experiment!

---

## 💡 Pro Tips

1. **Keep venv activated**: Always see `(venv)` in terminal
2. **Check ports**: Streamlit uses port 8501 by default
3. **Save frequently**: If modifying code, test often
4. **Monitor browser**: Keep browser tab open to app
5. **Read outputs**: All training info printed to console
6. **Use examples**: Try provided test cases first

---

## 🎉 Success Indicators

- ✅ Streamlit opens without errors
- ✅ Model loads successfully
- ✅ Can adjust sliders and get predictions
- ✅ Predictions make sense (high scores → PASS)
- ✅ Can upload Excel file and see results
- ✅ All tabs work (Info, Batch, How It Works, FAQ)

---

## 📞 Quick Help

**Q: How long does it run?**
A: Training takes ~30-60 seconds. Predictions are instant (< 1 second).

**Q: Can I modify the model?**
A: Yes! Edit `train_ann.py` to change layers, neurons, or iterations.

**Q: Can I use my own data?**
A: Yes! Replace `dataset.xlsx` with your own (same columns).

**Q: What's the accuracy?**
A: Training: 77.5%, Testing: 80% (see `train_ann.py` output)

**Q: Why does prediction differ sometimes?**
A: Inputs differ, and model finds complex patterns (non-linear).

---

Good luck! 🚀
