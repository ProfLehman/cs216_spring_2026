# gui_shell.py
# spring 2025
# prof. lehman
#
# Simple Tkinter GUI shell
# Can be reused for many basic IPO programs
#

import tkinter as tk
from tkinter import messagebox


# function called by button
def process_data():
    try:
        # input
        data = input_entry.get()

        # process
        # replace this line with whatever your program should do
        result = f"You entered: {data}"

        # output
        output_label.config(text=result)

    except Exception:
        messagebox.showerror("Error", "Something went wrong.")


# main window
root = tk.Tk()
root.title("GUI Program Shell")
root.geometry("350x150")

# text box for input
input_entry = tk.Entry(root, width=30)
input_entry.pack(pady=10)

# button to process data
process_button = tk.Button(root, text="Process", command=process_data)
process_button.pack(pady=10)

# label for output
output_label = tk.Label(root, text="Output will appear here.")
output_label.pack(pady=10)

# start GUI
root.mainloop()