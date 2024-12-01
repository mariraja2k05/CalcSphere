import customtkinter as ctk
import subprocess
import mysql.connector
import re
from PIL import Image, ImageTk
from tkinter import messagebox

#database connecting
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12300952",
    database="calcsphere"
)
cursor = db.cursor()

#login function to command
def login():
    username = loginusername.get()
    password = loginpassword.get()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    if result:
        messagebox.showinfo("Login Success", "Welcome!")
        root.after(1000, run)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
#signup function to the command
def signup():
    name = signupname.get()
    username = signupusername.get()
    phone_number = signupphone.get()
    password = signuppassword.get()
    confirm_password = signupconfirmpassword.get()
    if password != confirm_password:
        messagebox.showerror("Signup Failed", "Passwords do not match!")
        return
    if not re.match(r'^\d{10}$', phone_number):
        messagebox.showerror("Signup Failed", "Phone number must be 10 digits!")
        return
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        messagebox.showerror("Signup Failed", "Username already exists!")
    elif not username or not password or not name or not phone_number:
        messagebox.showerror("Signup Failed", "All fields are required!")
    else:
        cursor.execute("INSERT INTO users (username, password, name, phone_number) VALUES (%s, %s, %s, %s)",
                       (username, password, name, phone_number))
        db.commit()
        messagebox.showinfo("Signup Success", "Account created successfully!")
        show_login()

# Function switch between login and signup
def show_signup():
    login_frame.pack_forget()
    signup_frame.pack(side='top', anchor='center', pady=100)

def show_login():
    signup_frame.pack_forget()
    login_frame.pack(side='top', anchor='center', pady=100)

#clear login
def clear_login_fields():
    loginusername.delete(0, ctk.END)
    loginpassword.delete(0, ctk.END)

#clear signup
def clear_signup_fields():
    signupusername.delete(0, ctk.END)
    signuppassword.delete(0, ctk.END)
    signupconfirmpassword.delete(0, ctk.END)
    signupname.delete(0, ctk.END)
    signupphone.delete(0, ctk.END)

#Function to run the main menu
def run():
    root.destroy()
    subprocess.run(['python', 'menu1.py'])

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry('1000x800')
root.title("Login")
root.config(bg="black")  # Dark background to contrast with frames

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/loginbg.png")  # Path to the logo image
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)  # Resize the image to 1000x600 pixels
logo_photo = ImageTk.PhotoImage(logo_image)
# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Login Frame
login_frame = ctk.CTkFrame(root, width=500, height=500, corner_radius=0,border_width=10,border_color='green',fg_color="aliceblue")
login_frame.pack(side='top', anchor='center', pady=100)

ctk.CTkLabel(login_frame, text="Login", font=ctk.CTkFont(size=30, weight="bold")).pack(pady=20)

ctk.CTkLabel(login_frame, text="Username",font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
loginusername = ctk.CTkEntry(login_frame, placeholder_text='Enter username', width=300, border_width=5, height=25, border_color='#3D59AB', corner_radius=5, font=ctk.CTkFont(size=14), text_color='black')
loginusername.pack(padx=100)

ctk.CTkLabel(login_frame, text="Password",font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
loginpassword = ctk.CTkEntry(login_frame, placeholder_text='Enter Password', width=300, show="*", border_width=5, height=25, border_color='red', corner_radius=5, font=ctk.CTkFont(size=14))
loginpassword.pack(padx=100)

login_button = ctk.CTkButton(login_frame, text="Login", command=login, width=100,font=ctk.CTkFont(size=20, weight="bold"),text_color='white',fg_color='#3D59AB',hover_color="#483D8B")
login_button.pack(pady=20)

signup_link = ctk.CTkButton(login_frame, text="Don't have an account? Signup", command=show_signup, width=200, fg_color="#3D59AB",
                            hover_color="#483D8B",font=ctk.CTkFont(size=20, weight="bold"),text_color='white')
signup_link.pack(pady=20)

# Signup Frame
signup_frame = ctk.CTkFrame(root, width=500, height=500, corner_radius=0,border_width=10,border_color='deepskyblue2',fg_color="aliceblue")

ctk.CTkLabel(signup_frame, text="Signup", font=ctk.CTkFont(size=30, weight="bold")).pack(pady=20)

ctk.CTkLabel(signup_frame, text="Name",font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
signupname = ctk.CTkEntry(signup_frame, width=300)
signupname.pack(padx=100)

ctk.CTkLabel(signup_frame, text="Username",font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
signupusername = ctk.CTkEntry(signup_frame, width=300)
signupusername.pack()

ctk.CTkLabel(signup_frame, text="Phone Number",font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
signupphone = ctk.CTkEntry(signup_frame, width=300)
signupphone.pack()

ctk.CTkLabel(signup_frame, text="Password",font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
signuppassword = ctk.CTkEntry(signup_frame, width=300, show="*")
signuppassword.pack()

ctk.CTkLabel(signup_frame, text="Confirm Password",font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)
signupconfirmpassword = ctk.CTkEntry(signup_frame, width=300, show="*")
signupconfirmpassword.pack()

signup_button = ctk.CTkButton(signup_frame, text="Signup", command=signup, width=200)
signup_button.pack(pady=20)

login_link = ctk.CTkButton(signup_frame, text="Already have an account? Login", command=show_login, width=200, fg_color="transparent", hover_color="gray")
login_link.pack(pady=20)

# Start the main loop
root.mainloop()