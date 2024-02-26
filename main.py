import tkinter as tk
from tkinter import messagebox, ttk
from customtkinter import *
from PIL import Image, ImageTk
from Chapter_1 import ch_1


menu = CTk()
menu.title("Main Menu")
menu.geometry('500x200')
frame1 = CTkFrame(menu)
frame1.pack(side="top", fill='x')
Main_menu = CTkLabel(frame1, text='Main Menu', font=('Arial', 40))
Main_menu.pack(fill='both', expand=True)


frame2 = CTkFrame(menu)
frame2.pack(fill='both', expand=True)
button1 = CTkButton(frame2, text="Chapter 1", corner_radius=35, command=ch_1, border_color='#ffffff',
                    border_width=2, hover_color='#ededed', fg_color='#5c5b5b')
button1.pack(side='left', padx=10)

button2 = CTkButton(frame2, text="Chapter 2", corner_radius=35, border_color='#ffffff',
                    border_width=2, hover_color='#ededed', fg_color='#5c5b5b')
button2.pack(side='right', padx=10)

menu.mainloop()