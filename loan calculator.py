import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to calculate loan payments
def calculate_loan():
    try:
        # Retrieve inputs
        loan_amount = float(entry_loan_amount.get())
        annual_interest_rate = float(entry_interest_rate.get())
        loan_tenure = int(entry_loan_tenure.get())

        if loan_amount <= 0 or annual_interest_rate <= 0 or loan_tenure <= 0:
            raise ValueError

        # Convert annual interest rate to monthly and loan tenure to months
        monthly_interest_rate = annual_interest_rate / 100 / 12
        loan_months = loan_tenure * 12

        # Calculate monthly payment using the loan formula
        monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_months)
        total_repayment = monthly_payment * loan_months

        # Display results
        entry_monthly_payment.delete(0, ctk.END)
        entry_monthly_payment.insert(0, f"{monthly_payment:.2f}")

        entry_total_repayment.delete(0, ctk.END)
        entry_total_repayment.insert(0, f"{total_repayment:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Function to refresh all fields
def refresh_fields():
    entry_loan_amount.delete(0, ctk.END)  # Clear loan amount field
    entry_interest_rate.delete(0, ctk.END)  # Clear interest rate field
    entry_loan_tenure.delete(0, ctk.END)  # Clear loan tenure field
    entry_monthly_payment.delete(0, ctk.END)  # Clear monthly payment field
    entry_total_repayment.delete(0, ctk.END)  # Clear total repayment field

# Exit function
def run():
    root.destroy()

# Create the main window using customtkinter
ctk.set_appearance_mode("dark-blue")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()
root.title("Loan Calculator")
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
label_title = ctk.CTkLabel(frame, text="Loan Calculator", font=("Helvetica", 30, 'bold'))
label_title.grid(column=1, row=0, pady=20, columnspan=2)

# Loan amount input
label_loan_amount = ctk.CTkLabel(frame, text="Loan Amount ($):", font=("Helvetica", 15))
label_loan_amount.grid(row=1, column=0, padx=10, pady=10)

entry_loan_amount = ctk.CTkEntry(frame)
entry_loan_amount.grid(row=1, column=1, padx=10, pady=10)

# Annual interest rate input
label_interest_rate = ctk.CTkLabel(frame, text="Annual Interest Rate (%):", font=("Helvetica", 15))
label_interest_rate.grid(row=2, column=0, padx=10, pady=10)

entry_interest_rate = ctk.CTkEntry(frame)
entry_interest_rate.grid(row=2, column=1, padx=10, pady=10)

# Loan tenure input
label_loan_tenure = ctk.CTkLabel(frame, text="Loan Tenure (years):", font=("Helvetica", 15))
label_loan_tenure.grid(row=3, column=0, padx=10, pady=10)

entry_loan_tenure = ctk.CTkEntry(frame)
entry_loan_tenure.grid(row=3, column=1, padx=10, pady=10)

# Monthly payment output
label_monthly_payment = ctk.CTkLabel(frame, text="Monthly Payment ($):", font=("Helvetica", 15))
label_monthly_payment.grid(row=4, column=0, padx=10, pady=10)

entry_monthly_payment = ctk.CTkEntry(frame)
entry_monthly_payment.grid(row=4, column=1, padx=10, pady=10)

# Total repayment output
label_total_repayment = ctk.CTkLabel(frame, text="Total Repayment ($):", font=("Helvetica", 15))
label_total_repayment.grid(row=5, column=0, padx=10, pady=10)

entry_total_repayment = ctk.CTkEntry(frame)
entry_total_repayment.grid(row=5, column=1, padx=10, pady=10)

# Calculate button
button_calculate = ctk.CTkButton(frame, text="Calculate", font=("Helvetica", 15), command=calculate_loan)
button_calculate.grid(row=6, column=0, padx=20, pady=20, columnspan=1)

# Refresh button
button_refresh = ctk.CTkButton(frame, text="Refresh", font=("Helvetica", 15), command=refresh_fields)
button_refresh.grid(row=6, column=1, padx=20, pady=20, columnspan=1)

# Exit button
button_exit = ctk.CTkButton(frame, text="Exit", font=("Helvetica", 15), command=run)
button_exit.grid(row=7, column=0, padx=20, pady=50, columnspan=2)

root.mainloop()
