

import tkinter as tk
import os

def open_file1():
    os.system("python3 registerGUI.py")

def open_file2():
    os.system("python3 vedio.py")

def open_file3():
    os.system("python3 detect.py")

def open_file4():
    os.system("python3 database.py")

# Create the main application window
root = tk.Tk()
root.title("CRIMINAL APPLICATION MANAGER")

# Set window size and position
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Add background image
background_image = tk.PhotoImage(file="bck.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Create a frame for better organization
frame = tk.Frame(root, padx=20, pady=10)
frame.pack(expand=True)

# Create buttons to open each file
button1 = tk.Button(frame, text="Criminal Register", command=open_file1, width=30, height=2)
button1.pack(pady=(20, 10))

button2 = tk.Button(frame, text="Video Detector", command=open_file2, width=30, height=2)
button2.pack(pady=10)

button3 = tk.Button(frame, text="Image Detector", command=open_file3, width=30, height=2)
button3.pack(pady=10)

button4 = tk.Button(frame, text="Criminal Capture Data", command=open_file4, width=30, height=2)
button4.pack(pady=10)

root.mainloop()



