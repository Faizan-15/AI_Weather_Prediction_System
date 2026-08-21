# AI Weather Prediction System

## Author

**Muhammad Faizan Ashraf**  
BS Computer Science Student

---

## Project Overview

This project was developed as a Semester Project for the Artificial Intelligence (AI) course during the 3rd Semester of my BS Computer Science degree.

The system uses Machine Learning algorithms to predict:

- Temperature
- Rainfall Forecast

based on weather-related inputs such as:

- Month
- Humidity

A user-friendly interface has been built using Streamlit, allowing users to enter values and receive predictions instantly. The project demonstrates the practical implementation of Artificial Intelligence and Machine Learning concepts in a weather prediction application.

---

## Objectives

- Apply Artificial Intelligence concepts in a practical environment.
- Build and train Machine Learning models for prediction tasks.
- Predict temperature using regression techniques.
- Predict rainfall using classification techniques.
- Develop an interactive web-based interface.
- Understand the complete Machine Learning workflow from data preparation to deployment.

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-Learn
- Pickle

### Machine Learning Models

- Support Vector Regression (SVR) for Temperature Prediction
- Support Vector Classification (SVC) for Rainfall Prediction

---

## Project Structure

```text
├── weather.py
├── customdataset.py
├── temperature_model.pkl
├── rainfall_model.pkl
└── README.md
```

### File Description

#### weather.py

Main application file responsible for:

- Training machine learning models
- Loading saved models
- Evaluating model performance
- Providing the Streamlit user interface
- Generating weather predictions

#### customdataset.py

Contains the custom dataset used for training and testing the weather prediction models, including:

- Month
- Humidity
- Temperature
- Rainfall Information

---

## Features

- Temperature Prediction
- Rainfall Forecasting
- Interactive Streamlit Interface
- Automatic Model Training
- Saved Model Loading
- Machine Learning Based Predictions
- Educational Demonstration of AI Concepts

---

## How It Works

1. The dataset is loaded from the custom dataset file.
2. Relevant features are selected for training.
3. The temperature prediction model is trained using Support Vector Regression (SVR).
4. The rainfall prediction model is trained using Support Vector Classification (SVC).
5. Trained models are saved using Pickle.
6. Users provide Month and Humidity values through the Streamlit interface.
7. The system generates temperature and rainfall predictions based on the provided inputs.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Faizan-15/AI_Weather_Prediction_System.git
cd AI-Weather-Prediction-System
```

### Install Dependencies

```bash
pip install streamlit pandas scikit-learn
```

### Run the Application

```bash
streamlit run weather.py
```

---

## Learning Outcomes

Through this project, I gained practical experience in:

- Artificial Intelligence Fundamentals
- Machine Learning Model Development
- Regression and Classification Techniques
- Data Preprocessing
- Model Evaluation
- Python Programming
- Streamlit Application Development
- Software Project Organization

---

## Personal Project Declaration

This repository contains a project independently developed by **Muhammad Faizan Ashraf** as part of the Artificial Intelligence course during the 3rd Semester of BS Computer Science.

- The project idea, implementation, coding, testing, debugging, and documentation were completed by me.
- This repository reflects my personal learning, research, and practical understanding of Artificial Intelligence and Machine Learning concepts.
- The project is included in my GitHub portfolio to showcase my academic work and software development skills.
- Any future improvements, updates, or enhancements will continue to be maintained by me unless stated otherwise.

---

## Academic Note

This project was created for educational and learning purposes. Its primary goal is to demonstrate the implementation of Machine Learning techniques using Python and Streamlit while applying theoretical AI concepts in a practical project environment.

---

## About Me

**Muhammad Faizan Ashraf**  
BS Computer Science Student

GitHub: https://github.com/Faizan-15

---

⭐ Thank you for visiting this repository. Feedback, suggestions, and constructive comments are always welcome.