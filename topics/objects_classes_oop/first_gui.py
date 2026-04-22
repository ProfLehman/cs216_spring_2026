import tkinter as tk

from Chapel import *

def do_something():
    #print("in do something ...")
    #temp = msg_entry.get()
    #print( temp )
    #msg_label.config(text=temp)
    
    number = int( msg_entry.get() )
   
    chapel_helper = Chapel()
   
    chapel_helper.set_chapels( number )
    
    answer = chapel_helper.get_remaining()
    msg_label.config(text=answer)
    
    

# main
root = tk.Tk()
root.title("first gui")
root.geometry("500x250")

# declare instances of components
msg_label = tk.Label(root, text="msg")

msg_entry = tk.Entry(root, width=30)
msg_entry.insert(0,"0")

msg_button = tk.Button(root, text="Do Something", command=do_something)

# add components to grid
msg_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
msg_entry.grid(row=1, column=0, padx=10, pady=10)
msg_button.grid(row=2, column=0, pady=10)

root.mainloop()