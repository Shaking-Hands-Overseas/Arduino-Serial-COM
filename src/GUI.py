import tkinter as tk
from tkinter import font
from tkinter.font import Font

TITLE = 'Shaking Hands Overseas Sender-Receiver COM'


root = tk.Tk()

title_font = Font(family="Helvetica", size=24, weight="bold")
root.title(TITLE)
root.geometry('1000x700')
tk.Label(root, text=TITLE, font=title_font).pack()
root.mainloop()