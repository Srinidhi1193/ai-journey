# Student Score Predictor

A machine learning practice project to predict students' math scores using demographic, educational, reading score, and writing score features.

## Dataset

Students Performance in Exams dataset.

## Target

- Math Score

## Features

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Reading Score
- Writing Score

## Models

- Linear Regression
- Ridge Regression
- Lasso Regression

## Preprocessing

- One-Hot Encoding
- ColumnTransformer
- Train-Test Split

## Evaluation Metrics

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## Hyperparameter Tuning

Ridge Regression was tuned using GridSearchCV with 5-fold cross-validation.

Tested alpha values:

- 0.01
- 0.1
- 1
- 10
- 100