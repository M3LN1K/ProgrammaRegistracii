'''import tkinter as tk
def switch_windows():
    window1.withdraw()
    window2.deiconify()
window1 = tk.Tk()
button = tk.Button(window1, text="Перейти к Window 2", command=switch_windows)
button.pack()
window2 = tk.Toplevel()
window2.withdraw()
label = tk.Label(window2, text="Это Window 2")
label.pack()
window1.mainloop()'''


from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3


AppWindow = Tk()
AppWindow.title(f"Страница:")
AppWindow.geometry("1024x768")

canvas = Canvas(bg="black", width=1024, height=768)
canvas.pack(anchor=CENTER, expand=1)

canvas.create_line(0, 150, 1024, 150, fill="white")
canvas.create_oval(10, 10, 100, 100, fill="white", outline="white")

AppWindow.mainloop()