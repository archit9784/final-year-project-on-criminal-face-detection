


import tkinter as tk
from tkinter import messagebox
import subprocess
import sqlite3

# Function to register new user
def register_user():
    username = reg_username_entry.get()
    password = reg_password_entry.get()

    # Connect to the database
    conn = sqlite3.connect("user_credentials.db")
    c = conn.cursor()

    # Insert new user into the database
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    conn.close()

    messagebox.showinfo("Registration Successful", "You have successfully registered!")

# Function to validate login
def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    # Connect to the database
    conn = sqlite3.connect("user_credentials.db")
    c = conn.cursor()

    # Check if username and password are correct
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()

    if user:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        # Open the new Python file
        subprocess.Popen(["python3", "start.py"])
        # Destroy the login window
        root.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to switch to registration interface
def switch_to_register():
    login_frame.grid_forget()
    register_frame.grid(row=0, column=0, padx=20, pady=20)

# Function to switch to login interface
def switch_to_login():
    register_frame.grid_forget()
    login_frame.grid(row=0, column=0, padx=20, pady=20)

# Create main window
root = tk.Tk()
root.title("Login Page")

# Set window size
window_width = 600
window_height = 400
root.geometry(f"{window_width}x{window_height}")


background_image = tk.PhotoImage(file="/Users/dhakad/Downloads/CFIS-criminal-face-identification-system-master/cyber.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create database table if not exists
conn = sqlite3.connect("user_credentials.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY,
             username TEXT NOT NULL,
             password TEXT NOT NULL)''')
conn.commit()
conn.close()

# Create a frame for login interface
login_frame = tk.Frame(root)

# Create username label and entry for login
username_label = tk.Label(login_frame, text="Username:", font=("Arial", 14))
username_label.grid(row=1, column=1, padx=10, pady=5)
username_entry = tk.Entry(login_frame, font=("Arial", 14))
username_entry.grid(row=1, column=2, padx=10, pady=5)

# Create password label and entry for login
password_label = tk.Label(login_frame, text="Password:", font=("Arial", 14))
password_label.grid(row=2, column=1, padx=10, pady=5)
password_entry = tk.Entry(login_frame, show="*", font=("Arial", 14))
password_entry.grid(row=2, column=2, padx=10, pady=5)

# Create login button
login_button = tk.Button(login_frame, text="Login", command=validate_login, font=("Arial", 14))
login_button.grid(row=3, columnspan=3, pady=10)

# Create a frame for registration interface
register_frame = tk.Frame(root)

# Create username label and entry for registration
reg_username_label = tk.Label(register_frame, text="Username:", font=("Arial", 14))
reg_username_label.grid(row=1, column=1, padx=10, pady=5)
reg_username_entry = tk.Entry(register_frame, font=("Arial", 14))
reg_username_entry.grid(row=1, column=2, padx=10, pady=5)

# Create password label and entry for registration
reg_password_label = tk.Label(register_frame, text="Password:", font=("Arial", 14))
reg_password_label.grid(row=2, column=1, padx=10, pady=5)
reg_password_entry = tk.Entry(register_frame, show="*", font=("Arial", 14))
reg_password_entry.grid(row=2, column=2, padx=10, pady=5)

# Create register button
register_button = tk.Button(register_frame, text="Register", command=register_user, font=("Arial", 14))
register_button.grid(row=3, columnspan=3, pady=10)

# Create login and register buttons in the main window
login_button_main = tk.Button(root, text="Login", command=switch_to_login, font=("Arial", 14))
login_button_main.grid(row=2, column=1, padx=20, pady=10)

register_button_main = tk.Button(root, text="Register", command=switch_to_register, font=("Arial", 14))
register_button_main.grid(row=2, column=2, padx=20, pady=10)

# Initially display the login interface
login_frame.grid(row=1, column=1, padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()


