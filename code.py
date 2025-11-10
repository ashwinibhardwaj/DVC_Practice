import pandas as pd

# Define the CSV file path
csv_file = "data/diabetes.csv"

# Load the existing CSV file (or create a new DataFrame if it doesn't exist)
try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", 
                               "BMI", "DiabetesPedigreeFunction", "Age", "target"])

# Define the new row data as a dictionary
new_row = pd.DataFrame([{
    "Pregnancies": 1,
    "Glucose": 110,
    "BloodPressure": 90,
    "SkinThickness": 23,
    "Insulin": 100,
    "BMI": 28.5,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 30,
    "target": 1
}])

# Append the new row using concat
df = pd.concat([df, new_row], ignore_index=True)

# Save the updated DataFrame back to the CSV file
df.to_csv(csv_file, index=False)

print("New row added successfully!")
