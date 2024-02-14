import random
import tkinter as tk
from tkinter import messagebox, ttk
from customtkinter import *
from sympy import symbols, expand
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def iter_com():
    req_iter_entry.configure(state='normal')
    req_Error_entry.delete('0', END)
    req_Error_entry.configure(state='disabled')
def error_com():
    req_Error_entry.configure(state='normal')
    req_iter_entry.delete('0', END)
    req_iter_entry.configure(state='disabled')
def solve_equation():
    req_Error = round(float(req_Error_entry.get() if req_Error_entry.get() != '' else '0'), 3)
    req_iter = round(float(req_iter_entry.get() if req_iter_entry.get() != '' else '10000'), 3)
    x_l = x_l_i = round(float(x_l_entry.get()), 3)
    x_u = x_u_i = round(float(x_u_entry.get()), 3)

    x = symbols('x')
    f_x = (fx_entry.get()).replace('^', '**').strip()
    for i in range(len(f_x)):
        if f_x[i] == 'x' and ('0' <= f_x[i - 1] <= '9') and i != 0:
            f_x = f_x[0:i] + '*x' + f_x[i+1:]

    f_x = expand(f_x)
    f_x.subs(x, x_l)

    if f_x.subs(x, x_l) * f_x.subs(x, x_u) >= 0:
        messagebox.showerror("Error", "No root exists in this range. Please try again.")
        return

    cur_Error = 100
    i = 1
    x_r = (x_l + x_u) / 2

    xx = np.linspace(x_l_i, x_u_i, 120)
    plt.plot(xx, [f_x.subs(x, i) for i in xx])
    table.insert(parent='', index=0, values=(0, round(x_l, 3), round(f_x.subs(x, x_l), 3), round(x_u, 3), round(f_x.subs(x, x_u), 3),
                                             round(x_r, 3), round(f_x.subs(x, x_r), 3), None))
    colors = np.array(
        ["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan",
         "magenta"])
    color = random.randint(0, 12)
    scatter = plt.scatter(x_l, f_x.subs(x, x_l), color=colors[color], zorder=2)
    scatter = plt.scatter(x_u, f_x.subs(x, x_u), color=colors[color], zorder=2)
    # Show the initial plot
    plt.draw()
    while True:
        plt.title(f'Iteration {i}')
        #scatter.remove()

        if f_x.subs(x, x_l) * f_x.subs(x, x_r) < 0:
            x_u = x_r
        elif f_x.subs(x, x_l) * f_x.subs(x, x_r) > 0:
            x_l = x_r
        else:
            break

        x_r_old = x_r
        x_r = (x_l + x_u) / 2

        cur_Error = abs((x_r - x_r_old) / x_r * 100)
        table.insert(parent='', index=i,
                     values=(i, round(x_l, 3), round(f_x.subs(x, x_l), 3), round(x_u, 3), round(f_x.subs(x, x_u), 3),
                             round(x_r, 3), round(f_x.subs(x, x_r), 3), round(cur_Error, 3)))
        #plt.cla()
        color = random.randint(0, 12)
        scatter = plt.scatter(x_l, f_x.subs(x, x_l), color=colors[color], zorder=2)
        scatter = plt.scatter(x_u, f_x.subs(x, x_u), color=colors[color], zorder=2)
        # Show the initial plot
        plt.draw()
        if cur_Error <= req_Error or i >= req_iter:
            break

        i += 1

    table.insert(parent='', index=0, values=('---', '---', '---', '---', '---', '---', '---', '---'))


# Create the main window
root = CTk()
root.title("Root Finder")

# Labels and Entry fields

frame2 = CTkFrame(root)
frame2.pack(fill='x')
CTkLabel(frame2, text="Lower Value (x_l):", anchor='w').pack(side='left')
x_l_entry = CTkEntry(frame2, placeholder_text="EX: 0...")
x_l_entry.pack(side='right', ipadx=22)

frame3 = CTkFrame(root)
frame3.pack(fill='x')
CTkLabel(frame3, text="Upper Value (x_u):", anchor='w').pack(side='left')
x_u_entry = CTkEntry(frame3, placeholder_text="EX: 1...")
x_u_entry.pack(side='right', ipadx=22)

frame4 = CTkFrame(root)
frame4.pack(fill='x')
CTkLabel(frame4, text="F(x):", anchor='w').pack(side='left')
fx_entry = CTkEntry(frame4, placeholder_text="EX: 2x^3-4x+5...")
fx_entry.pack(side='right', ipadx=22)

# Create a new frame for the last two label-entry pairs and the buttons
frame_last = CTkFrame(root)
frame_last.pack(fill='x')

frame1 = CTkFrame(frame_last)
frame1.pack(side='left', fill='x', expand=True)
CTkLabel(frame1, text="Requested Error Percentage:", anchor='w').pack(side='left')
req_Error_entry = CTkEntry(frame1, placeholder_text="EX: 10...", state='disabled')
req_Error_entry.pack(side='right', ipadx=22)

image_file = ImageTk.PhotoImage(Image.open("img.png").resize((20, 20), Image.Resampling.LANCZOS))
image_file2 = ImageTk.PhotoImage(Image.open("img2.png").resize((20, 20), Image.Resampling.LANCZOS))
# Create the first button and pack it to the left in frame_last
button1 = CTkButton(frame_last, image=image_file2, text="", command=error_com, corner_radius=35, border_color='#ffffff',
                    border_width=2, width=20, hover_color='#ededed', fg_color='#5c5b5b')
button1.pack(side='left', ipadx=20)

# Create the second button and pack it to the left in frame_last
button2 = CTkButton(frame_last, image=image_file, text="", corner_radius=35, command=iter_com, border_color='#ffffff',
                    border_width=2, width=20, hover_color='#ededed', fg_color='#5c5b5b')
button2.pack(side='left', ipadx=20)

frame5 = CTkFrame(frame_last)
frame5.pack(side='left', fill='x',ipadx=25, expand=True)
CTkLabel(frame5, text="Requested iterations:", anchor='e').pack(side='left')
req_iter_entry = CTkEntry(frame5, placeholder_text="EX: 5...", state='disabled')
req_iter_entry.pack(side='right', ipadx=22)


# Button to solve equation
solve_button = CTkButton(master=root, text="Solve", command=solve_equation, corner_radius=35, fg_color="transparent",
                         hover_color="#5c5b5b", border_color='#ffffff', border_width=2)
solve_button.pack()



# Output Text widget
frame_t_f = CTkScrollableFrame(root)
tabview = CTkTabview(master=frame_t_f)
tabview.pack(fill='both', expand=True)
tabview.add('Table')
tabview.add('Chart')
frame_t_f.pack(fill='both', expand=True)
table = ttk.Treeview(tabview.tab('Table'), columns=('i', 'x_l', 'F(x_l)', 'x_u', 'F(x_u)', 'x_r', 'F(x_r)', 'ε_a'),
                     show='headings', selectmode="extended")
table.heading('i', text='i')
table.column("i", minwidth=0, width=80)
table.heading('x_l', text='x_l')
table.column("x_l", minwidth=0, width=80)
table.heading('F(x_l)', text='F(x_l)')
table.column("F(x_l)", minwidth=0, width=80)
table.heading('x_u', text='x_u')
table.column("x_u", minwidth=0, width=80)
table.heading('F(x_u)', text='F(x_u)')
table.column("F(x_u)", minwidth=0, width=80)
table.heading('x_r', text='x_r')
table.column("x_r", minwidth=0, width=80)
table.heading('F(x_r)', text='F(x_r)')
table.column("F(x_r)", minwidth=0, width=80)
table.heading('ε_a', text='ε_a')
table.column("ε_a", minwidth=0, width=80)
table.pack(side='left', fill='both', expand=True)


fig, ax = plt.subplots()
plt.xlabel('X')
plt.ylabel('Y')
canvas = FigureCanvasTkAgg(fig, master=tabview.tab('Chart'))
canvas.get_tk_widget().pack(side='right', fill='both', expand=True)
# Plot the initial points



root.mainloop()