import tkinter as tk
from customtkinter import *
from bracketing import bracket
from Newton import newton_method
from Secant import Secant_method
from Simple_fixed import Simple_fixed_method

menu = CTk()
menu.title("Main Menu")

frame1 = CTkFrame(menu)
frame1.pack(side="top", fill='x')
Main_menu = CTkLabel(frame1, text='Main Menu', font=('Arial', 40))
Main_menu.pack(fill='both', expand=True)

frame2 = CTkFrame(menu)
frame2.pack(fill='both', expand=True)

button1 = CTkButton(frame2, text="Bracketing Methods", corner_radius=35, command=bracket, border_color='#ffffff',
                    border_width=2, hover_color='#ededed', fg_color='#5c5b5b')
button1.pack(side='left', padx=10)

button2 = CTkButton(frame2, text="Newton Method", corner_radius=35, border_color='#ffffff',
                    border_width=2, hover_color='#ededed', fg_color='#5c5b5b', command=newton_method)
button2.pack(side='right', padx=10)

button3 = CTkButton(frame2, text="Secant Method", corner_radius=35, border_color='#ffffff',
                    border_width=2, hover_color='#ededed', fg_color='#5c5b5b', command=Secant_method)
button3.pack(side='right', padx=10)

button4 = CTkButton(frame2, text="Simple Fixed point", corner_radius=35, border_color='#ffffff',
                    border_width=2, hover_color='#ededed', fg_color='#5c5b5b', command=Simple_fixed_method)
button4.pack(side='left', pady=10)

menu.mainloop()
