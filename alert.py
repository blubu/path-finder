
import tkinter as tk
from tkinter import font


class AlertWindow:
    def __init__(self, steps):
        self.window = tk.Tk()
        self.window.title('')
        self.window.geometry('300x100')
        self.window.geometry("+500+300")
        self.label = ''

        if steps == 0:
            self.label = tk.Label(self.window, text='No path found !!!')
            self.label.pack()
            self.label.place(x=70, y=35)
            self.font = font.Font(weight='bold', size=12)
            self.label.configure(foreground='red', font=self.font)
        else:
            self.label = tk.Label(self.window, text=f'Step Cost: {steps}')
            self.label.pack()
            self.label.place(x=90, y=35)
            self.font = font.Font(weight='bold', size=12)
            self.label.configure(font=self.font)

        self.window.mainloop()
