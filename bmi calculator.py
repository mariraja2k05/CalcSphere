import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess


# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # Convert cm to meters
        age = int(entry_age.get())
        gender = combo_gender.get()

        if weight <= 0 or height <= 0 or age <= 0:
            raise ValueError

        bmi = weight / (height ** 2)
        entry_bmi.delete(0, ctk.END)
        entry_bmi.insert(0, f"{bmi:.2f}")  # Display BMI rounded to 2 decimal places

        # BMI categories
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        label_category.configure(text=f"Category: {category}\nGender: {gender}, Age: {age}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid weight, height, and age values.")

# Function to refresh all fields
def refresh_fields():
    entry_weight.delete(0, ctk.END)  # Clear weight entry field
    entry_height.delete(0, ctk.END)  # Clear height entry field
    entry_age.delete(0, ctk.END)  # Clear age entry field
    combo_gender.set("Select Gender")  # Reset gender combo box
    entry_bmi.delete(0, ctk.END)  # Clear BMI output field
    label_category.configure(text="Category:")  # Reset category label

# Exit function
def run():
    root.destroy()
    subprocess.run(['python', 'menu.py'])

# Create the main window using customtkinter
ctk.set_appearance_mode("dark-blue")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.title("BMI Calculator")
root.geometry('1000x800')

# Resize and display background image
bg_image = Image.open("Background images/loginbg.png")  # Path to your background image
bg_image = bg_image.resize((1000, 800), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = ctk.CTkLabel(root, image=bg_photo)
bg_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10, fg_color='black')
frame.pack(padx=10, pady=150)

# Title label
label_title = ctk.CTkLabel(frame, text="BMI Calculator", font=("Helvetica", 30, 'bold'))
label_title.grid(column=1, row=0, pady=20, columnspan=2)

# Weight input
label_weight = ctk.CTkLabel(frame, text="Weight (kg):", font=("Helvetica", 15))
label_weight.grid(row=1, column=0, padx=10, pady=10)

entry_weight = ctk.CTkEntry(frame)
entry_weight.grid(row=1, column=1, padx=10, pady=10)

# Height input
label_height = ctk.CTkLabel(frame, text="Height (cm):", font=("Helvetica", 15))
label_height.grid(row=2, column=0, padx=10, pady=10)

entry_height = ctk.CTkEntry(frame)
entry_height.grid(row=2, column=1, padx=10, pady=10)

# Age input
label_age = ctk.CTkLabel(frame, text="Age:", font=("Helvetica", 15))
label_age.grid(row=3, column=0, padx=10, pady=10)

entry_age = ctk.CTkEntry(frame)
entry_age.grid(row=3, column=1, padx=10, pady=10)

# Gender combo box
label_gender = ctk.CTkLabel(frame, text="Gender:", font=("Helvetica", 15))
label_gender.grid(row=4, column=0, padx=10, pady=10)

combo_gender = ctk.CTkComboBox(frame, values=["Male", "Female", "Other"], state="readonly")
combo_gender.grid(row=4, column=1, padx=10, pady=10)
combo_gender.set("Select Gender")

# BMI output
label_bmi = ctk.CTkLabel(frame, text="BMI:", font=("Helvetica", 15))
label_bmi.grid(row=5, column=0, padx=10, pady=10)

entry_bmi = ctk.CTkEntry(frame)
entry_bmi.grid(row=5, column=1, padx=10, pady=10)

# BMI category
label_category = ctk.CTkLabel(frame, text="Category:", font=("Helvetica", 15))
label_category.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

# Calculate button
button_calculate = ctk.CTkButton(frame, text="Calculate", font=("Helvetica", 15), command=calculate_bmi)
button_calculate.grid(row=7, column=0, padx=20, pady=20, columnspan=1)

# Refresh button
button_refresh = ctk.CTkButton(frame, text="Refresh", font=("Helvetica", 15), command=refresh_fields)
button_refresh.grid(row=7, column=1, padx=20, pady=20, columnspan=1)

# Exit button
button_exit = ctk.CTkButton(frame, text="Exit", font=("Helvetica", 15), command=run)
button_exit.grid(row=8, column=0, padx=20, pady=50, columnspan=2)

root.mainloop()
