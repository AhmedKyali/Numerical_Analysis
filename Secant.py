from customtkinter import *
import random
import tkinter as tk
from tkinter import messagebox, ttk
from sympy import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import re
from utils import transform_expression

def Secant_method():
    def iter_com():
        req_iter_entry.configure(state='normal')
        button1.configure(hover_color='#ededed', fg_color='#5c5b5b')
        button2.configure(hover_color='#ffffff', fg_color='#ffffff')
        solve_button.configure(text='Solve : By Iterations')
        req_Error_entry.delete('0', END)
        req_Error_entry.configure(state='disabled')
    def error_com():
        req_Error_entry.configure(state='normal')
        button1.configure(hover_color='#ffffff', fg_color='#ffffff')
        button2.configure(hover_color='#ededed', fg_color='#5c5b5b')
        solve_button.configure(text='Solve : By Error')
        req_iter_entry.delete('0', END)
        req_iter_entry.configure(state='disabled')
    def solve_equation():
        flag = False
        iter = 0
        error = 100
        req_iter = round(float(req_iter_entry.get() if req_iter_entry.get() != '' else '10000'), 3)
        x_i = float(x_i_entry.get())
        x_i_minus = float(x_i_minus_entry.get())
        eps = round(float(req_Error_entry.get() if req_Error_entry.get() != '' else '0'), 3)
        x = symbols('x')
        f_x = (fx_entry.get())
        f_x = transform_expression(f_x)
        f_x = expand(f_x)
        scatter = plt.scatter(x_i_minus, f_x.subs(x, x_i_minus), zorder=2)
        x_i_max = max(x_i, x_i_minus)
        x_i_min = min(x_i, x_i_minus)
        while True:
            x_i_max = max(x_i, x_i_max)
            x_i_min = min(x_i, x_i_min)
            x_i_max = max(x_i_minus, x_i_max)
            x_i_min = min(x_i_minus, x_i_min)
            table.insert(parent='', index=iter,
                         values=(iter, round(x_i_minus, 3), round(float(f_x.subs(x, x_i_minus)), 3),
                                 round(x_i, 3), round(float(f_x.subs(x, x_i)), 3)
                                 , None if error == 100 else round(error, 3)), tags='even' if iter % 2 == 0 else 'odd')

            scatter = plt.scatter(x_i, f_x.subs(x, x_i), zorder=2)
            plt.draw()

            x_iPlus1 = x_i - ((f_x.subs(x, x_i) * (x_i_minus - x_i))/(f_x.subs(x, x_i_minus) - f_x.subs(x, x_i)))
            error = abs(x_iPlus1-x_i)/x_iPlus1*100

            x_i_minus = x_i
            x_i = x_iPlus1

            if flag == True or req_iter <= iter:
                break
            iter += 1
            if eps >= error:
                flag = True
        xx = np.linspace(float(x_i_min), float(x_i_max), 120)
        plt.plot(xx, [f_x.subs(x, i) for i in xx])

    root = CTk()
    root.title("Root Finder")
    frame2 = CTkFrame(root)
    frame2.pack(fill='x')
    CTkLabel(frame2, text="Minus one Value (x_i-1):", anchor='w').pack(side='left')
    x_i_minus_entry = CTkEntry(frame2, placeholder_text="EX: 1...")
    x_i_minus_entry.pack(side='right', ipadx=22, pady=5)

    frame3 = CTkFrame(root)
    frame3.pack(fill='x')
    CTkLabel(frame3, text="Initial Value (x_o):", anchor='w').pack(side='left')
    x_i_entry = CTkEntry(frame3, placeholder_text="EX: 1...")
    x_i_entry.pack(side='right', ipadx=22, pady=5)

    frame4 = CTkFrame(root)
    frame4.pack(fill='x')
    CTkLabel(frame4, text="F(x):", anchor='w').pack(side='left')
    fx_entry = CTkEntry(frame4, placeholder_text="EX: 2x^3-4x+5...")
    fx_entry.pack(side='right', ipadx=22, pady=5)

    frame_last = CTkFrame(root)
    frame_last.pack(fill='x')

    frame1 = CTkFrame(frame_last)
    frame1.pack(side='left', fill='x', expand=True)
    CTkLabel(frame1, text="Requested Error Percentage:", anchor='w').pack(side='left')
    req_Error_entry = CTkEntry(frame1, placeholder_text="EX: 10...", state='disabled')
    req_Error_entry.pack(side='right', ipadx=22, pady=5)

    button1 = CTkButton(frame_last, text="By Error", corner_radius=35, border_color='#ffffff',
                    border_width=2, width=20, hover_color='#ededed', fg_color='#5c5b5b', command=error_com)
    button1.pack(side='left', ipadx=20, padx=5)

    # Create the second button and pack it to the left in frame_last
    button2 = CTkButton(frame_last, text="By Iterations", corner_radius=35, border_color='#ffffff',
                    border_width=2, width=20, hover_color='#ededed', fg_color='#5c5b5b', command=iter_com)
    button2.pack(side='left', ipadx=20, padx=5)

    frame5 = CTkFrame(frame_last)
    frame5.pack(side='left', fill='x', ipadx=25, expand=True)
    CTkLabel(frame5, text="Requested iterations:", anchor='e').pack(side='left')
    req_iter_entry = CTkEntry(frame5, placeholder_text="EX: 5...", state='disabled')
    req_iter_entry.pack(side='right', ipadx=22)

    # Button to solve equation
    solve_button = CTkButton(master=root, text="Solve", corner_radius=35, fg_color="transparent",
                         hover_color="#5c5b5b", border_color='#ffffff', border_width=2, command=solve_equation)
    solve_button.pack(pady=10)

    frame_t_f = CTkScrollableFrame(root)
    frame_t_f.pack(side='bottom', fill='both', expand=True)
    tabview = CTkTabview(master=frame_t_f)
    tabview.pack(fill='both', expand=True)
    tabview.add('Table')
    tabview.add('Chart')

    table = ttk.Treeview(tabview.tab('Table'), columns=('i', 'x_i-1', 'F(x_i-1)', 'x_i', 'F(x_i)', 'ε_a'),
                     show='headings', selectmode="extended")
    table.heading('i', text='i')
    table.column("i", minwidth=0, width=80)
    table.heading('x_i-1', text='x_i-1')
    table.column("x_i-1", minwidth=0, width=80)
    table.heading('F(x_i-1)', text='F(x_i-1)')
    table.column("F(x_i-1)", minwidth=0, width=80)
    table.heading('x_i', text='x_i')
    table.column("x_i", minwidth=0, width=80)
    table.heading('F(x_i)', text='F(x_i)')
    table.column("F(x_i)", minwidth=0, width=80)
    table.heading('ε_a', text='ε_a')
    table.column("ε_a", minwidth=0, width=80)
    table.tag_configure('even', background='#4f4e4e')
    table.tag_configure('odd', background='#858585')
    table.pack(side='bottom', fill='both', expand=True)

    fig, ax = plt.subplots()
    plt.xlabel('X')
    plt.ylabel('Y')
    canvas = FigureCanvasTkAgg(fig, master=tabview.tab('Chart'))
    canvas.get_tk_widget().pack(side='bottom', fill='both', expand=True)

    root.mainloop()