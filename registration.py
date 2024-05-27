import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import *
import sqlite3
from PIL import Image, ImageTk
import re
import random
import subprocess
import threading


# Create the main window
window = tk.Tk()
window.geometry("650x900")
window.title("REGISTRATION FORM")

# Define tkinter StringVar and IntVar variables
fullname_var = tk.StringVar()
address_var = tk.StringVar()
username_var = tk.StringVar()
email_var = tk.StringVar()
phoneno_var = tk.StringVar()
gender_var = tk.IntVar()
age_var = tk.IntVar()
password_var = tk.StringVar()
confirm_password_var = tk.StringVar()

# Generate a random ID for each registration
registration_id = random.randint(1, 1000)

# Connect to the SQLite database
db = sqlite3.connect('evaluation1.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration "
               "(id INTEGER NOT NULL UNIQUE, Fullname TEXT, Address TEXT, Username TEXT, "
               "Email TEXT, Phoneno TEXT, Gender TEXT, Age TEXT, Password TEXT)")
db.commit()

# Function to check password strength
def password_check(password):
    special_symbols = ['$', '@', '#', '%']
    if len(password) < 6:
        return False, 'Password length should be at least 6 characters'
    if len(password) > 20:
        return False, 'Password length should not be greater than 20 characters'
    if not any(char.isdigit() for char in password):
        return False, 'Password should have at least one numeral'
    if not any(char.isupper() for char in password):
        return False, 'Password should have at least one uppercase letter'
    if not any(char.islower() for char in password):
        return False, 'Password should have at least one lowercase letter'
    if not any(char in special_symbols for char in password):
        return False, 'Password should have at least one of the symbols $@#'
    return True, 'Password is strong'


# Function to insert data into the database
def insert_data():
    # def _insert_data():
        # Create a new SQLite connection and cursor within the thread
        conn = sqlite3.connect('evaluation1.db')
        cursor = conn.cursor()
        
        fullname = fullname_var.get()
        address = address_var.get()
        username = username_var.get()
        email = email_var.get()
        phoneno = phoneno_var.get()
        gender = gender_var.get()
        age = age_var.get()
        password = password_var.get()
        confirm_password = confirm_password_var.get()

        # Check if the email is valid
        if not re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email):
            tk.messagebox.showinfo("Invalid Email", "Please enter a valid email address")
            return

        # Check if the phone number is valid
        if len(str(phoneno)) != 10:
            tk.messagebox.showinfo("Invalid Phone Number", "Please enter a 10-digit phone number")
            return
        
        if username == "":
            tk.messagebox.showinfo("Invalid User Name", "Please enter a username")
            return

        # Check if the age is valid
        if age <= 0 or age > 100:
            tk.messagebox.showinfo("Invalid Age", "Please enter a valid age")
            return

        # Check if the passwords match
        if password != confirm_password:
            tk.messagebox.showinfo("Passwords Don't Match", "Password and Confirm Password must be the same")
            return

        # Check if the password is strong
        is_strong, message = password_check(password)
        if not is_strong:
            tk.messagebox.showinfo("Weak Password", message)
            return

        # Insert data into the database
        cursor.execute("INSERT INTO registration (id, Fullname, Address, Username, Email, Phoneno, Gender, Age, Password) "
                       "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (registration_id, fullname, address, username, email, phoneno, gender, age, password))
        conn.commit()
        conn.close()  # Close the connection

        tk.messagebox.showinfo('Success!', 'Account Created Successfully!')

        # window.after(100, window.destroy())
        # window.destroy()
        # tkfun = Tk()
        # tkfun.destroy()
        

    # threading.Thread(target=_insert_data).start()


# insert_data()
# root = tk.Tk()
# string_var = tk.StringVar(root)
# frame = ttk.Frame(root)
# frame.pack()
# entry = ttk.Entry(frame, textvariable=string_var)
# entry.pack()
# root.destroy()
        
def register_and_insert():
    if window.winfo_exists():  # Check if the window still exists
        insert_data()
        window.destroy()
        subprocess.call(["python", "login.py"])  # Execute the login.py file



# Load and display background image
background_image = Image.open('register.jpg').resize((650, 800), Image.LANCZOS)
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0)

# Create labels and entry fields for registration form
tk.Label(window, text="REGISTRATION FORM", font=("Times new roman", 25, "bold"), bg="#FFF5EE", fg="#800517").place(
    x=160, y=50)
tk.Label(window, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow").place(x=130, y=150)
tk.Entry(window, textvar=fullname_var, width=20, font=('', 15)).place(x=330, y=150)
tk.Label(window, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="snow").place(x=130, y=200)
tk.Entry(window, textvar=address_var, width=20, font=('', 15)).place(x=330, y=200)
tk.Label(window, text="E-mail :", width=12, font=("Times new roman", 15, "bold"), bg="snow").place(x=130, y=250)
tk.Entry(window, textvar=email_var, width=20, font=('', 15)).place(x=330, y=250)
tk.Label(window, text="Phone number :", width=12, font=("Times new roman", 15, "bold"), bg="snow").place(x=130, y=300)
tk.Entry(window, textvar=phoneno_var, width=20, font=('', 15)).place(x=330, y=300)
tk.Label(window, text="Gender :", width=12, font=("Times new roman", 15, "bold"), bg="snow").place(x=130, y=350)
tk.Radiobutton(window, text="Male", padx=5, width=5, bg="snow", font=("bold", 15), variable=gender_var, value=1).place(
    x=330, y=350)
tk.Radiobutton(window, text="Female", padx=20, width=4, bg="snow", font=("bold", 15), variable=gender_var,
                value=2).place(x=440, y=350)
tk.Label(window, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="snow").place(x=130, y=400)
tk.Entry(window, textvar=age_var, width=20, font=('', 15)).place(x=330, y=400)
tk.Label(window, text="Username :", width=12, font=("Times new roman", 15, "bold"), bg="snow").place(x=130, y=450)
tk.Entry(window, textvar=username_var, width=20, font=('', 15)).place(x=330, y=450)
tk.Label(window, text="Password :", width=12, font=("Times new roman", 15, "bold"), bg="snow").place(x=130, y=500)
tk.Entry(window, textvar=password_var, width=20, font=('', 15), show="*").place(x=330, y=500)
tk.Label(window, text="Confirm Password:", width=13, font=("Times new roman", 15, "bold"), bg="snow").place(x=130, y=550)
tk.Entry(window, textvar=confirm_password_var, width=20, font=('', 15), show="*").place(x=330, y=550)

# Create a Register button to submit the form
tk.Button(window, text="Register", bg="red", font=("", 20), fg="white", width=9, height=1, command=register_and_insert).place(
    x=260, y=620)

# Run the Tkinter event loop
window.mainloop()
