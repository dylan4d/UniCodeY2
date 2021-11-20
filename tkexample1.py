
import tkinter as tk

def onclick():
    L1.config(text = "Modified text")

root = tk.Tk()
root.geometry('400x400')

L1 = tk.Label(root, text='Some text')
L1.pack()

btn = tk.Button(root, text="OK", command=onclick)
btn.pack()

root.mainloop()