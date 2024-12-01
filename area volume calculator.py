import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to calculate area or volume
def calculate():
    try:
        selected_shape = combo_shape.get()
        dimension1 = float(entry_dim1.get())
        dimension2 = float(entry_dim2.get()) if entry_dim2.get() else None
        dimension3 = float(entry_dim3.get()) if entry_dim3.get() else None

        if dimension1 <= 0 or (dimension2 is not None and dimension2 <= 0) or (dimension3 is not None and dimension3 <= 0):
            raise ValueError("Dimensions must be positive numbers.")

        result = None

        # Area Calculations
        if selected_shape == "Square":
            result = dimension1 ** 2
        elif selected_shape == "Rectangle":
            result = dimension1 * dimension2
        elif selected_shape == "Circle":
            result = 3.14159 * dimension1 ** 2
        elif selected_shape == "Triangle":
            result = 0.5 * dimension1 * dimension2

        # Volume Calculations
        elif selected_shape == "Cube":
            result = dimension1 ** 3
        elif selected_shape == "Rectangular Prism":
            result = dimension1 * dimension2 * dimension3
        elif selected_shape == "Sphere":
            result = (4 / 3) * 3.14159 * dimension1 ** 3
        elif selected_shape == "Cylinder":
            result = 3.14159 * dimension1 ** 2 * dimension2

        # Display the result
        if result is not None:
            entry_result.delete(0, ctk.END)
            entry_result.insert(0, f"{result:.2f}")
        else:
            raise ValueError("Invalid shape or dimensions.")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

# Function to refresh all fields
def refresh_fields():
    combo_shape.set("Select Shape")
    entry_dim1.delete(0, ctk.END)
    entry_dim2.delete(0, ctk.END)
    entry_dim3.delete(0, ctk.END)
    entry_result.delete(0, ctk.END)

# Exit function
def run():
    root.destroy()

# Create the main window using customtkinter
ctk.set_appearance_mode("dark-blue")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Area and Volume Calculator")
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
label_title = ctk.CTkLabel(frame, text="Area and Volume Calculator", font=("Helvetica", 30, 'bold'))
label_title.grid(column=1, row=0, pady=20, columnspan=2)

# Shape selection
label_shape = ctk.CTkLabel(frame, text="Select Shape:", font=("Helvetica", 15))
label_shape.grid(row=1, column=0, padx=10, pady=10)

combo_shape = ctk.CTkComboBox(frame, values=["Square", "Rectangle", "Circle", "Triangle", "Cube", "Rectangular Prism", "Sphere", "Cylinder"])
combo_shape.grid(row=1, column=1, padx=10, pady=10)
combo_shape.set("Select Shape")

# Dimension 1
label_dim1 = ctk.CTkLabel(frame, text="Dimension 1 (e.g., Side/Radius):", font=("Helvetica", 15))
label_dim1.grid(row=2, column=0, padx=10, pady=10)

entry_dim1 = ctk.CTkEntry(frame)
entry_dim1.grid(row=2, column=1, padx=10, pady=10)

# Dimension 2
label_dim2 = ctk.CTkLabel(frame, text="Dimension 2 (if applicable):", font=("Helvetica", 15))
label_dim2.grid(row=3, column=0, padx=10, pady=10)

entry_dim2 = ctk.CTkEntry(frame)
entry_dim2.grid(row=3, column=1, padx=10, pady=10)

# Dimension 3
label_dim3 = ctk.CTkLabel(frame, text="Dimension 3 (if applicable):", font=("Helvetica", 15))
label_dim3.grid(row=4, column=0, padx=10, pady=10)

entry_dim3 = ctk.CTkEntry(frame)
entry_dim3.grid(row=4, column=1, padx=10, pady=10)

# Result
label_result = ctk.CTkLabel(frame, text="Result:", font=("Helvetica", 15))
label_result.grid(row=5, column=0, padx=10, pady=10)

entry_result = ctk.CTkEntry(frame)
entry_result.grid(row=5, column=1, padx=10, pady=10)

# Calculate button
button_calculate = ctk.CTkButton(frame, text="Calculate", font=("Helvetica", 15), command=calculate)
button_calculate.grid(row=6, column=0, padx=20, pady=20, columnspan=1)

# Refresh button
button_refresh = ctk.CTkButton(frame, text="Refresh", font=("Helvetica", 15), command=refresh_fields)
button_refresh.grid(row=6, column=1, padx=20, pady=20, columnspan=1)

# Exit button
button_exit = ctk.CTkButton(frame, text="Exit", font=("Helvetica", 15), command=run)
button_exit.grid(row=7, column=0, padx=20, pady=50, columnspan=2)

root.mainloop()
