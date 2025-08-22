import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Load the pre-trained drug classification model (make sure the path is correct)
model = joblib.load('drug_classification_model.pkl')  # Update this with your model file path

# Create the main Tkinter window
root = tk.Tk()
root.title("Drug Classification System")
root.geometry("400x350")

# Function to classify the drug based on input
def classify_drug():
    try:
        # Get values from input fields
        age = float(age_entry.get())
        cholesterol = float(cholesterol_entry.get())
        bp = float(bp_entry.get())
        drug_type = float(drug_type_entry.get())

        # Prepare the feature array for prediction (make sure it's in the correct shape)
        features = np.array([[age, cholesterol, bp, drug_type]])

        # Get prediction from the model
        prediction = model.predict(features)

        # Show the prediction in a message box
        messagebox.showinfo("Prediction", f"Predicted Drug Class: {prediction[0]}")
    
    except ValueError:
        # Handle invalid input
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

# Create labels and input fields
tk.Label(root, text="Age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

tk.Label(root, text="Cholesterol Level (mg/dL):").pack(pady=5)
cholesterol_entry = tk.Entry(root)
cholesterol_entry.pack(pady=5)

tk.Label(root, text="Blood Pressure (mmHg):").pack(pady=5)
bp_entry = tk.Entry(root)
bp_entry.pack(pady=5)

tk.Label(root, text="Drug Type:").pack(pady=5)
drug_type_entry = tk.Entry(root)
drug_type_entry.pack(pady=5)

# Button to trigger classification
classify_button = tk.Button(root, text="Classify", command=classify_drug)
classify_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
