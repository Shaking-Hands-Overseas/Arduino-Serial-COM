import tkinter as tk
from tkinter.font import Font
from Var import *

TITLE = 'Shaking Hands Overseas\n'
SUBTITLE = 'Sender-Receiver COM'
OPTIONS_SELECTION = ["Receiver", "Sender"]
BACKGROUND_COLOR = "#d4fffa"
PAD_X = 10
PAD_Y = 10


def main():

        root = tk.Tk()
        # Basic Information
        root.title(TITLE)
        root.geometry('950x700')
        root.config(bg=BACKGROUND_COLOR)
        title_font = Font(family="Helvetica", size=24, weight="bold")
        subtitle_font = Font(family="Helvetica", size=16, weight="bold")
        tk.Label(root, text=SUBTITLE, bg=BACKGROUND_COLOR, font=title_font).grid(row=0, column=1)
        tk.Label(root, text=TITLE, bg=BACKGROUND_COLOR, font=subtitle_font).grid(row=1, column=1)
        tk.Label(root, text="", bg=BACKGROUND_COLOR).grid(row=2, column=1)

        # Options
        selection = tk.StringVar()
        tk.Label(root, text="Select whether you want to be a Sender or a Receiver", bg=BACKGROUND_COLOR).grid(row=4, column=0, padx=PAD_X, pady=PAD_Y)
        options = tk.OptionMenu(root, selection, *OPTIONS_SELECTION, command=lambda x: print(selection.get()))
        options.grid(row=4, column=1, padx=PAD_X, pady=PAD_Y)
        options.config(width=10)

        serial_port = tk.StringVar()
        tk.Label(root, text="Select a Serial Port", bg=BACKGROUND_COLOR).grid(row=5, column=0, padx=PAD_X, pady=PAD_Y)
        options2 = tk.OptionMenu(root, serial_port, *SERIAL_PORTS, command=lambda x: print(serial_port.get()))
        options2.grid(row=5, column=1, padx=PAD_X, pady=PAD_Y)
        options2.config(width=10)

        api_url = tk.StringVar()
        api_url.set(URL_R)
        tk.Label(root, text="Input API URL", bg=BACKGROUND_COLOR).grid(row=6, column=0, padx=PAD_X, pady=PAD_Y)
        options3 = tk.Entry(root, textvariable=api_url, width=30)
        options3.grid(row=6, column=1, padx=PAD_X, pady=PAD_Y)
        root.mainloop()


if __name__ == "__main__":
    main()