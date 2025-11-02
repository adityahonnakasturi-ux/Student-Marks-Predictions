# Student-Marks-Predictions
Predict student marks using Linear Regression in Python.
Student Marks Prediction using Linear Regression
📘 Overview

This project predicts a student’s marks based on the number of study hours using a Simple Linear Regression model.
It is a beginner-friendly project that demonstrates how to use Python, pandas, matplotlib, and scikit-learn for basic machine learning tasks.

🧠 Objective

To develop a predictive model that estimates student scores from the number of hours they study.

🧰 Technologies Used

Python

Pandas

NumPy

Matplotlib

Scikit-learn

📂 Dataset

A small sample dataset is used containing two columns:

Hours → Number of hours studied

Scores → Marks obtained

Hours, Scores
1, 10
2, 20
3, 30
4, 40
5, 50
6, 55
7, 65
8, 75
9, 85
10, 95

⚙️ Steps Performed

Imported and visualized the dataset using Matplotlib.

Split data into training and testing sets.

Trained the model using LinearRegression from scikit-learn.

Predicted marks for test data and compared with actual values.

Tested with a custom input (e.g., 9.25 hours → ~93 marks).

Evaluated performance using Mean Absolute Error.

📊 Sample Output
   Actual  Predicted
2      30  34.80
8      85  81.42
4      50  48.38
9      95  91.56
1      20  21.70

Predicted Score for 9.25 hours of study = 92.91
Mean Absolute Error: 4.18

📈 Visualization

A scatter plot shows the relationship between Hours Studied and Percentage Score, with the regression line representing predictions.

🏁 Conclusion

The model successfully predicts a student’s marks based on study hours with minimal error.
This project demonstrates the core steps in building a regression model — data preparation, training, prediction, and evaluation.

👨‍💻 Author

Adithya H
3rd Year | Information Science Engineering
