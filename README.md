# Student Performance Indicator  
**End-to-End Machine Learning Project**

This project predicts **students’ academic performance** (test scores) based on several socio-demographic and behavioral factors such as **gender**, **parental education level**, **lunch type**, and **test preparation course completion**.

---

## Project Overview

The goal of this project is to explore how different factors affect students’ test performance and to build a **machine learning model** that can predict a student’s average score.  
This project follows the complete lifecycle of a typical **ML pipeline**, from **data analysis** to **deployment**.

---

## Machine Learning Lifecycle

1. **Problem Understanding** – Identify variables affecting student scores.  
2. **Data Collection** – Load and inspect the dataset.  
3. **Data Validation** – Check for missing values, duplicates, and data types.  
4. **Exploratory Data Analysis (EDA)** – Visualize relationships between features.  
5. **Feature Engineering** – Create new features like `total_score` and `average`.  
6. **Data Preprocessing** – Handle categorical variables and scaling.  
7. **Model Training & Evaluation** – Train multiple models and select the best one.  
8. **Model Deployment (optional)** – Prepare the model for API deployment.  

---

## Dataset Information

- **Source:** [Kaggle – Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)  
- **Shape:** 1000 rows × 8 columns  

### **Features**
| Feature | Description |
|----------|--------------|
| `gender` | Male / Female |
| `race/ethnicity` | Group A–E |
| `parental level of education` | High school, Bachelor’s, Master’s, etc. |
| `lunch` | Standard or free/reduced |
| `test preparation course` | Completed or not completed |
| `math score`, `reading score`, `writing score` | Student test results |

---

## Exploratory Data Analysis (Key Insights)

- No missing or duplicate values.  
- Female students tend to perform better on average.  
- Standard lunch is associated with higher performance.  
- Math is the hardest subject overall (lowest average).  
- Parental education shows minor correlation with performance.  
- Math, Reading, and Writing scores are **positively correlated**.

---

## Tech Stack & Tools

| Category | Tools |
|-----------|-------|
| **Languages** | Python |
| **Libraries** | Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn, XGBoost, CatBoost |
| **Environment** | Jupyter Notebook |
| **Version Control** | Git & GitHub |

---

## Model Building

We trained multiple regression models to predict **Math scores**.  

### Preprocessing
- **Numerical features**: StandardScaler  
- **Categorical features**: OneHotEncoder  
- ColumnTransformer was used to preprocess all features before training.  
- Data was split into **training (80%)** and **testing (20%)** sets.

---

## Modeling & Evaluation

### Models Used
- Linear Regression
- Lasso Regression
- Ridge Regression
- K-Neighbors Regressor
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

### Evaluation 
- Ridge and Linear Regression performed best for predicting Math scores.

- Ensemble models like AdaBoost, CatBoost, and Random Forest also achieved strong results.

- K-Neighbors and Decision Tree had lower performance, possibly due to overfitting or dataset characteristics.

## Results

The trained regression models accurately predict students’ performance based on socio-demographic features.  
Visual analysis confirms that **gender**, **lunch type**, and **test preparation** significantly influence outcomes.

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/ManelHjaoujia/mlproject.git
cd mlproject
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Run Jupyter notebooks (optional)**
```bash
jupyter notebook
```
4. **Run the API**
```bash
python app.py
```

## Docker Usage
You can either pull the prebuilt image from Docker Hub or build it locally.

**Option 1: Pull from Docker Hub**
```bash
docker pull manelhjaoujia07/mlproject:latest
docker run -p 5000:5000 manelhjaoujia07/mlproject:latest
```

**Option 2: Build locally**
```bash
docker build -t mlproject:latest .
docker run -p 5000:5000 mlproject:latest
```

## GitHub Actions CI/CD

Workflows automatically:

- Checkout repository  
- Set up Python environment  
- Install dependencies  
- Run Flask app  
- Test API endpoints  

This ensures your code is **continuously integrated, tested, and ready for deployment**.

---

## Learning Outcomes

- Implement the **entire ML workflow** from raw data to deployment.  
- Perform **data preprocessing** and **feature engineering**.  
- Visualize and interpret **data distributions**.  
- Compare and evaluate **multiple regression models**.  
- Structure a **machine learning project** for real-world applications.


## Contributing

Contributions are welcome!  
Please **fork** the repository and **submit pull requests** to suggest improvements or new features.

##  Author

**Manel Hjaoujia**  
Master’s Student in Information Systems Engineering & Data Science
