
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import sys
import os


# Function to display details of the criminal
def display_criminal_details(name):
    # Connect to the database
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()

    # Query the database to retrieve details of the criminal
    c.execute("SELECT * FROM registrations WHERE name=?", (name,))
    details = c.fetchone()

    # Close the connection
    conn.close()

    # If criminal details are found, display them
    if details:
        # Create a new window
        window = tk.Tk()
        window.title("Criminal Details")

        # Create labels for each detail
        labels = [
            "Name:",
            "Father's Name:",
            "Mother's Name:",
            "Religion:",
            "Gender:",
            "Nationality:",
            "Crime Convicted:"
        ]
        for i, label in enumerate(labels):
            tk.Label(window, text=label).grid(row=i, column=0, sticky="w")
            tk.Label(window, text=details[i]).grid(row=i, column=1, sticky="w")

        # Display image if path is available
        image_path = details[7]
        if image_path:
            # Check if the image file exists
            if os.path.isfile(image_path):
                # Open the image and resize it to fit within a certain size limit
                max_width = 300
                max_height = 300
                image = Image.open(image_path)
                image.thumbnail((max_width, max_height), Image.ANTIALIAS)
                image = ImageTk.PhotoImage(image)
                img_label = tk.Label(window, image=image)
                img_label.grid(row=0, column=2, rowspan=len(labels), padx=10, pady=10)
                # Keep a reference to the image to prevent garbage collection
                img_label.image = image
            else:
                messagebox.showinfo("Image Not Found", "Image file not found.")
        else:
            messagebox.showinfo("Image Path Not Found", "No image path available in the database.")

        # Adjust window size based on content
        window.update_idletasks()
        window.geometry('{}x{}'.format(window.winfo_reqwidth(), window.winfo_reqheight()))

        window.mainloop()
    else:
        messagebox.showinfo("Not Found", f"No details found for criminal: {name}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        criminal_name = sys.argv[1]
        display_criminal_details(criminal_name)
    else:
        messagebox.showinfo("Error", "No criminal name provided.")

