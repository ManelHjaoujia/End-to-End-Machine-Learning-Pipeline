# MLProject: End-to-End Machine Learning Pipeline

## Overview
MLProject is an end-to-end machine learning project covering data exploration, preprocessing, model training, evaluation, API deployment, and CI/CD automation. It follows best practices in ML engineering, reproducibility, and deployment using Python, Docker, and GitHub Actions. This project is ideal for showcasing production-ready ML skills.

## Features
- **Exploratory Data Analysis (EDA):** Jupyter notebooks for data exploration and visualization.
- **Data Preprocessing:** Scripts for cleaning, transforming, and scaling features.
- **Model Training:** Modular scripts for training, evaluating, and saving machine learning models.
- **API Deployment:** Flask/FastAPI application for serving model predictions.
- **Testing:** Automated endpoint tests to validate API functionality.
- **Containerization:** Dockerfile for reproducible environments.
- **CI/CD:** GitHub Actions workflows for automated testing and deployment.
- **Artifact Management:** Organized folder structure for trained models and outputs.

## Folder Structure

mlproject/                
├── .github/ # CI/CD workflows                        
├── artifacts/ # Trained models and outputs                       
├── notebook/ # Jupyter notebooks for EDA and experimentation                    
├── src/ # Source code (preprocessing, training, utilities)                          
├── templates/ # Reusable scripts or templates                       
├── app.py # Main API application                       
├── endpoint_test.py # Tests for API endpoints                      
├── requirements.txt # Python dependencies                     
├── Dockerfile # Docker configuration                           
├── setup.py # Project packaging                         
└── README.md # Project documentation                         


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

## Contributing

Contributions are welcome!  
Please **fork** the repository and **submit pull requests** to suggest improvements or new features.
