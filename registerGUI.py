
import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3

def select_image():
    file_path = filedialog.askopenfilename()
    entry_image.delete(0, tk.END)
    entry_image.insert(tk.END, file_path)

def register():
    name = entry_name.get()
    father_name = entry_father_name.get()
    mother_name = entry_mother_name.get()
    religion = entry_religion.get()
    gender = gender_var.get()
    nationality = entry_nationality.get()
    crime_convicted = crime_convicted_var.get()
    image_path = entry_image.get()

    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS registrations
                 (name TEXT, father_name TEXT, mother_name TEXT,
                 religion TEXT, gender TEXT, nationality TEXT,
                 crime_convicted TEXT, image_path TEXT)''')

    c.execute("INSERT INTO registrations VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (name, father_name, mother_name, religion, gender, nationality, crime_convicted, image_path))

    conn.commit()
    conn.close()
    messagebox.showinfo("Registration", "Registration successful!")

root = tk.Tk()
root.title("Registration Form")

window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

frame = tk.Frame(root, padx=50, pady=20, bg="white")
frame.pack(expand=True)

label_name = tk.Label(frame, text="Name:", font=("Helvetica", 14))
label_name.grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame, font=("Helvetica", 14))
entry_name.grid(row=0, column=1)

label_father_name = tk.Label(frame, text="Father's Name:", font=("Helvetica", 14))
label_father_name.grid(row=1, column=0, sticky="w")
entry_father_name = tk.Entry(frame, font=("Helvetica", 14))
entry_father_name.grid(row=1, column=1)

label_mother_name = tk.Label(frame, text="Mother's Name:", font=("Helvetica", 14))
label_mother_name.grid(row=2, column=0, sticky="w")
entry_mother_name = tk.Entry(frame, font=("Helvetica", 14))
entry_mother_name.grid(row=2, column=1)

label_religion = tk.Label(frame, text="Religion:", font=("Helvetica", 14))
label_religion.grid(row=3, column=0, sticky="w")
entry_religion = tk.Entry(frame, font=("Helvetica", 14))
entry_religion.grid(row=3, column=1)

label_gender = tk.Label(frame, text="Gender:", font=("Helvetica", 14))
label_gender.grid(row=4, column=0, sticky="w")
gender_var = tk.StringVar()
gender_var.set("Male")
gender_male = tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male", font=("Helvetica", 14))
gender_male.grid(row=4, column=1, sticky="w")
gender_female = tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female", font=("Helvetica", 14))
gender_female.grid(row=4, column=1, sticky="e")

label_nationality = tk.Label(frame, text="Nationality:", font=("Helvetica", 14))
label_nationality.grid(row=5, column=0, sticky="w")
entry_nationality = tk.Entry(frame, font=("Helvetica", 14))
entry_nationality.grid(row=5, column=1)

label_crime_convicted = tk.Label(frame, text="Crime Convicted:", font=("Helvetica", 14))
label_crime_convicted.grid(row=6, column=0, sticky="w")
crime_convicted_var = tk.StringVar()
crime_convicted_var.set("No")
crime_convicted_yes = tk.Radiobutton(frame, text="Yes", variable=crime_convicted_var, value="Yes", font=("Helvetica", 14))
crime_convicted_yes.grid(row=6, column=1, sticky="w")
crime_convicted_no = tk.Radiobutton(frame, text="No", variable=crime_convicted_var, value="No", font=("Helvetica", 14))
crime_convicted_no.grid(row=6, column=1, sticky="e")

label_image = tk.Label(frame, text="Image Path:", font=("Helvetica", 14))
label_image.grid(row=7, column=0, sticky="w")
entry_image = tk.Entry(frame, font=("Helvetica", 14))
entry_image.grid(row=7, column=1, sticky="ew")

image_button = tk.Button(frame, text="Select Image", command=select_image, font=("Helvetica", 14))
image_button.grid(row=7, column=2, sticky="e")

submit_button = tk.Button(root, text="Submit", command=register, font=("Helvetica", 14))
submit_button.pack(pady=10)

root.mainloop()



