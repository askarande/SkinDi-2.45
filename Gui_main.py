import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as ms
from PIL import Image, ImageTk
from subprocess import call

def login():
    root.destroy()
    call(["python", r"C:\Users\User\new\Skin_Disease\login.py"])

def register():
    root.destroy()
    call(["python", r"C:\Users\User\new\Skin_Disease\registration.py"])

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Skin Cancer Prediction System")
root.configure(background="brown")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

background_image = Image.open('Capture.png')
background_image = background_image.resize((1530, 900), Image.LANCZOS)
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0)

title_label = tk.Label(root, text="Skin Disease Detection System using Machine Learning",
                       font=("Times New Roman", 35, 'bold'), background="#152238", fg="white", width=50, height=2)
title_label.place(x=0, y=0)

login_button = tk.Button(root, text="Login", command=login, width=14, height=1, font=('times', 20, 'bold'),
                          bg="lightblue", fg="black")
login_button.place(x=100, y=240)

register_button = tk.Button(root, text="Register", command=register, width=14, height=1, font=('times', 20, 'bold'),
                             bg="lightblue", fg="black")
register_button.place(x=100, y=320)

exit_button = tk.Button(root, text="Exit", command=exit_app, width=14, height=1, font=('times', 20, 'bold'),
                         bg="red", fg="white")
exit_button.place(x=100, y=400)

root.mainloop()
