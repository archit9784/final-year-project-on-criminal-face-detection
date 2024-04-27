
import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import subprocess

# Function to detect images using OpenCV
def detect_image(image_path):
    # Connect to the database
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()

    # Query the database to retrieve criminal details
    c.execute("SELECT name FROM registrations WHERE image_path=?", (image_path,))
    row = c.fetchone()

    # Close the connection
    conn.close()

    # If criminal details are found, display the name and open data.py
    if row:
        name = row[0]
        messagebox.showinfo("Match Found", f"Name: {name}")
        # Open data.py using subprocess
        subprocess.Popen(['python3', 'data.py', name])
    else:
        messagebox.showinfo("Not Found", "No matching entry found.")

# Function to handle image selection
def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        detect_image(file_path)

# Create the main application window
root = tk.Tk()
root.title("Image Recognition")

# Set the window size
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

background_image = tk.PhotoImage(file="/Users/dhakad/Downloads/CFIS-criminal-face-identification-system-master/detaa.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Set the font size
font_size = 14

# Create a label and button for image selection
label_select = tk.Label(root, text="Select Image:", font=("Arial", font_size))
label_select.pack(pady=40)
btn_select = tk.Button(root, text="Browse", command=select_image, font=("Arial", font_size))
btn_select.pack(pady=20)

root.mainloop()





