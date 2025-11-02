# Student Marks Prediction using Linear Regression

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Step 1: Create dataset
data = {'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Scores': [10, 20, 30, 40, 50, 55, 65, 75, 85, 95]}
df = pd.DataFrame(data)

# Step 2: Visualize data
plt.scatter(df['Hours'], df['Scores'], color='blue')
plt.title('Hours vs Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()

# Step 3: Prepare data
X = df[['Hours']]
y = df['Scores']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Step 4: Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predict results
y_pred = model.predict(X_test)

# Step 6: Compare actual vs predicted
df_compare = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df_compare)

# Step 7: Test with your own value
hours = [[9.25]]
predicted_score = model.predict(hours)
print(f"Predicted Score for {hours[0][0]} hours of study = {predicted_score[0]:.2f}")

# Step 8: Evaluate model
error = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", error)
