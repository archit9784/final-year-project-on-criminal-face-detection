import tkinter as tk
from tkinter import ttk
import csv

def load_data():
    try:
        with open("Attendance.csv", "r") as file:
            reader = csv.reader(file)
            # Clear existing items in the treeview
            for record in treeview.get_children():
                treeview.delete(record)
            # Insert data from the CSV file into the treeview
            for row in reader:
                treeview.insert("", "end", values=row)
    except FileNotFoundError:
        print("File not found.")

# Create main window
root = tk.Tk()
root.title("CSV Table")

# Create Treeview widget
treeview = ttk.Treeview(root, columns=("Name", "Time","Date"), show="headings")
treeview.heading("Name", text="Name")
treeview.heading("Date", text="Time")
treeview.heading("Time", text="Date")
treeview.pack(padx=10, pady=10)

# Load data button
load_button = tk.Button(root, text="Load Data", command=load_data)
load_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
