import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


print("=" * 50)
print("   STUDENT PERFORMANCE PREDICTOR")
print("=" * 50)

# Load dataset
data = pd.read_csv("student_data.csv")

print("\nDataset:")
print(data)

# Basic information
print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

# Features and target
X = data[["Study_Hours", "Attendance", "Previous_Marks", "Assignments"]]
y = data["Final_Marks"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model evaluation
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n===== MODEL PERFORMANCE =====")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")

# User input
print("\n===== PREDICT YOUR PERFORMANCE =====")

study_hours = float(input("Enter study hours per day: "))
attendance = float(input("Enter attendance percentage: "))
previous_marks = float(input("Enter previous exam marks: "))
assignments = float(input("Enter completed assignments: "))

student = pd.DataFrame({
    "Study_Hours": [study_hours],
    "Attendance": [attendance],
    "Previous_Marks": [previous_marks],
    "Assignments": [assignments]
})

prediction = model.predict(student)[0]

print(f"\nPredicted Final Marks: {prediction:.2f}")

# Study recommendation
print("\n===== STUDY RECOMMENDATION =====")

if prediction >= 80:
    print("Excellent performance! Keep maintaining your study routine.")
elif prediction >= 65:
    print("Good performance. Increase revision and practice.")
elif prediction >= 50:
    print("Average performance. Focus more on study hours and assignments.")
else:
    print("Needs improvement. Increase study time, attendance, and practice.")

# Visualization
plt.figure(figsize=(8, 5))
plt.scatter(data["Study_Hours"], data["Final_Marks"])
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")
plt.grid(True)
plt.show()