import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        dob = entry_dob.get()
        dob_date = datetime.strptime(dob, "%Y-%m-%d")  # Parse DOB in YYYY-MM-DD format
        today = datetime.now()
        if dob_date > today:
            raise ValueError("Date of birth cannot be in the future!")

        # Calculate age
        age_years = today.year - dob_date.year
        age_months = today.month - dob_date.month
        age_days = today.day - dob_date.day

        # Adjust for negative months/days
        if age_days < 0:
            age_months -= 1
            age_days += (dob_date.replace(month=dob_date.month + 1) - dob_date).days

        if age_months < 0:
            age_years -= 1
            age_months += 12

        # Display results
        entry_age_years.delete(0, ctk.END)
        entry_age_years.insert(0, str(age_years))

        entry_age_months.delete(0, ctk.END)
        entry_age_months.insert(0, str(age_months))

        entry_age_days.delete(0, ctk.END)
        entry_age_days.insert(0, str(age_days))

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid date in YYYY-MM-DD format.")

# Function to refresh all fields
def refresh_fields():
    entry_dob.delete(0, ctk.END)  # Clear DOB field
    entry_age_years.delete(0, ctk.END)  # Clear age years field
    entry_age_months.delete(0, ctk.END)  # Clear age months field
    entry_age_days.delete(0, ctk.END)  # Clear age days field

# Exit function
def run():
    root.destroy()

# Create the main window using customtkinter
ctk.set_appearance_mode("dark-blue")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.title("Age Calculator")
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
label_title = ctk.CTkLabel(frame, text="Age Calculator", font=("Helvetica", 30, 'bold'))
label_title.grid(column=1, row=0, pady=20, columnspan=2)

# Date of Birth input
label_dob = ctk.CTkLabel(frame, text="Date of Birth (YYYY-MM-DD):", font=("Helvetica", 15))
label_dob.grid(row=1, column=0, padx=10, pady=10)

entry_dob = ctk.CTkEntry(frame)
entry_dob.grid(row=1, column=1, padx=10, pady=10)

# Age in Years
label_age_years = ctk.CTkLabel(frame, text="Age (Years):", font=("Helvetica", 15))
label_age_years.grid(row=2, column=0, padx=10, pady=10)

entry_age_years = ctk.CTkEntry(frame)
entry_age_years.grid(row=2, column=1, padx=10, pady=10)

# Age in Months
label_age_months = ctk.CTkLabel(frame, text="Age (Months):", font=("Helvetica", 15))
label_age_months.grid(row=3, column=0, padx=10, pady=10)

entry_age_months = ctk.CTkEntry(frame)
entry_age_months.grid(row=3, column=1, padx=10, pady=10)

# Age in Days
label_age_days = ctk.CTkLabel(frame, text="Age (Days):", font=("Helvetica", 15))
label_age_days.grid(row=4, column=0, padx=10, pady=10)

entry_age_days = ctk.CTkEntry(frame)
entry_age_days.grid(row=4, column=1, padx=10, pady=10)

# Calculate button
button_calculate = ctk.CTkButton(frame, text="Calculate", font=("Helvetica", 15), command=calculate_age)
button_calculate.grid(row=5, column=0, padx=20, pady=20, columnspan=1)

# Refresh button
button_refresh = ctk.CTkButton(frame, text="Refresh", font=("Helvetica", 15), command=refresh_fields)
button_refresh.grid(row=5, column=1, padx=20, pady=20, columnspan=1)

# Exit button
button_exit = ctk.CTkButton(frame, text="Exit", font=("Helvetica", 15), command=run)
button_exit.grid(row=6, column=0, padx=20, pady=50, columnspan=2)

root.mainloop()
