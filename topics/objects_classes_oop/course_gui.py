# exam_gui.py
# Prof. Lehman style GUI shell example

import tkinter as tk
from tkinter import messagebox
from Student import *

# -----------------------------
# Function: calculate_grade
# -----------------------------
def calculate_grade():
    
    # get values from entries
    e1 = float(entry1.get())
    e2 = float(entry2.get())
    e3 = float(entry3.get())
    e4 = float(entry4.get())

    # use our data and logic class to get average dropping lowest score
    s = Student( e1, e2, e3, e4 )
    avg = s.getAvg()
    
    # display result
    result_label.config(text=f"Average: {avg:.2f}")

    
# -----------------------------
# GUI Setup
# -----------------------------
window = tk.Tk()
window.title("Exam Grade Calculator")
window.geometry("300x250")

# Labels and Entry boxes
tk.Label(window, text="Exam 1:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

tk.Label(window, text="Exam 2:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

tk.Label(window, text="Exam 3:").grid(row=2, column=0, padx=10, pady=5)
entry3 = tk.Entry(window)
entry3.grid(row=2, column=1)

tk.Label(window, text="Exam 4:").grid(row=3, column=0, padx=10, pady=5)
entry4 = tk.Entry(window)
entry4.grid(row=3, column=1)

# Button
calc_button = tk.Button(window, text="Calculate Grade", command=calculate_grade)
calc_button.grid(row=4, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(window, text="Average: --   Grade: --")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Run GUI
window.mainloop()