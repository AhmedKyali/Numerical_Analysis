from customtkinter import *
import random
from tkinter import messagebox, ttk
from sympy import symbols, expand
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from utils import transform_expression
def bracket():
    def Choose_method(choice):
        global Choice
        Choice = choice
        print(Choice)
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
        req_Error = round(float(req_Error_entry.get() if req_Error_entry.get() != '' else '0'), 3)
        req_iter = round(float(req_iter_entry.get() if req_iter_entry.get() != '' else '10000'), 3)
        x_l = x_l_i = round(float(x_l_entry.get()), 3)
        x_u = x_u_i = round(float(x_u_entry.get()), 3)

        x = symbols('x')
        f_x = (fx_entry.get())
        f_x = transform_expression(f_x)
        f_x = expand(f_x)
        f_x.subs(x, x_l)

        if f_x.subs(x, x_l) * f_x.subs(x, x_u) >= 0:
            messagebox.showerror("Error", "No root exists in this range. Please try again.")
            return

        cur_Error = 100
        i = 0
        x_r = (x_l + x_u) / 2
        plt.title(f'Root is {round(x_r, 3)} for Iteration {i + 1}')
        xx = np.linspace(x_l_i, x_u_i, 120)
        plt.plot(xx, [f_x.subs(x, i) for i in xx])
        table.insert(parent='', index=0, values=(0, round(x_l, 3), round(f_x.subs(x, x_l), 3), round(x_u, 3), round(f_x.subs(x, x_u), 3),
                                                 round(x_r, 3), round(f_x.subs(x, x_r), 3), None), tags='even')
        i+=1
        colors = np.array(
            ["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "beige", "brown", "gray", "cyan",
             "magenta"])
        color = random.randint(0, 12)
        scatter = plt.scatter(x_l, f_x.subs(x, x_l), color=colors[color], zorder=2)
        scatter = plt.scatter(x_u, f_x.subs(x, x_u), color=colors[color], zorder=2)
        # Show the initial plot
        plt.draw()
        while cur_Error > req_Error and i < req_iter:
            plt.title(f'Root is {round(x_r,3)} for Iteration {i+1}')
            #scatter.remove()

            if f_x.subs(x, x_l) * f_x.subs(x, x_r) < 0:
                x_u = x_r
            elif f_x.subs(x, x_l) * f_x.subs(x, x_r) > 0:
                x_l = x_r
            else:
                break

            x_r_old = x_r

            if Choice == 'Bisection':
                x_r = (x_l + x_u) / 2
            elif Choice == 'False position':
                x_r = x_u - ((f_x.subs(x, x_u) * (x_l - x_u))/(f_x.subs(x, x_l) - f_x.subs(x, x_u)))
            else:
                messagebox.showerror("Error", "No Method are chosen. Please try again.")
                return


            cur_Error = abs((x_r - x_r_old) / x_r * 100)

            table.insert(parent='', index=i,
                         values=(i, round(x_l, 3), round(f_x.subs(x, x_l), 3), round(x_u, 3), round(f_x.subs(x, x_u), 3),
                                 round(x_r, 3), round(f_x.subs(x, x_r), 3), round(cur_Error, 3)), tags='even' if i % 2 == 0 else 'odd')
            #plt.cla()
            color = random.randint(0, 12)
            scatter = plt.scatter(x_l, f_x.subs(x, x_l), color=colors[color], zorder=2)
            scatter = plt.scatter(x_u, f_x.subs(x, x_u), color=colors[color], zorder=2)
            # Show the initial plot
            plt.draw()
            i += 1


        table.insert(parent='', index=0, values=('---', '---', '---', '---', '---', '---', '---', '---'))


    # Create the main window
    root = CTk()
    root.title("Bracketing Methods")

    # Labels and Entry fields
    frame6 = CTkFrame(root)
    frame6.pack(fill='x')
    method_CoB = (CTkComboBox(master=frame6, values=['Empty', 'Bisection', 'False position'], command=Choose_method).
                  pack(side='right', ipadx=22, pady=5))
    CTkLabel(frame6, text="Choose a method", anchor='w').pack(side='left')

    frame2 = CTkFrame(root)
    frame2.pack(fill='x')
    CTkLabel(frame2, text="Lower Value (x_l):", anchor='w').pack(side='left')
    x_l_entry = CTkEntry(frame2, placeholder_text="EX: 0...")
    x_l_entry.pack(side='right', ipadx=22, pady=5)

    frame3 = CTkFrame(root)
    frame3.pack(fill='x')
    CTkLabel(frame3, text="Upper Value (x_u):", anchor='w').pack(side='left')
    x_u_entry = CTkEntry(frame3, placeholder_text="EX: 1...")
    x_u_entry.pack(side='right', ipadx=22, pady=5)

    frame4 = CTkFrame(root)
    frame4.pack(fill='x')
    CTkLabel(frame4, text="F(x):", anchor='w').pack(side='left')
    fx_entry = CTkEntry(frame4, placeholder_text="EX: 2x^3-4x+5...")
    fx_entry.pack(side='right', ipadx=22, pady=5)

    # Create a new frame for the last two label-entry pairs and the buttons
    frame_last = CTkFrame(root)
    frame_last.pack(fill='x')

    frame1 = CTkFrame(frame_last)
    frame1.pack(side='left', fill='x', expand=True)
    CTkLabel(frame1, text="Requested Error Percentage:", anchor='w').pack(side='left')
    req_Error_entry = CTkEntry(frame1, placeholder_text="EX: 10...", state='disabled')
    req_Error_entry.pack(side='right', ipadx=22, pady=5)

    # Create the first button and pack it to the left in frame_last
    button1 = CTkButton(frame_last,  text="By Error", command=error_com, corner_radius=35, border_color='#ffffff',
                        border_width=2, width=20, hover_color='#ededed', fg_color='#5c5b5b')
    button1.pack(side='left', ipadx=20, padx=5)

    # Create the second button and pack it to the left in frame_last
    button2 = CTkButton(frame_last, text="By Iterations", corner_radius=35, command=iter_com, border_color='#ffffff',
                        border_width=2, width=20, hover_color='#ededed', fg_color='#5c5b5b')
    button2.pack(side='left', ipadx=20, padx=5)

    frame5 = CTkFrame(frame_last)
    frame5.pack(side='left', fill='x', ipadx=25, expand=True)
    CTkLabel(frame5, text="Requested iterations:", anchor='e').pack(side='left')
    req_iter_entry = CTkEntry(frame5, placeholder_text="EX: 5...", state='disabled')
    req_iter_entry.pack(side='right', ipadx=22)


    # Button to solve equation
    solve_button = CTkButton(master=root, text="Solve", command=solve_equation, corner_radius=35, fg_color="transparent",
                             hover_color="#5c5b5b", border_color='#ffffff', border_width=2)
    solve_button.pack(pady=10)



    # Output Text widget
    frame_t_f = CTkScrollableFrame(root)
    frame_t_f.pack(fill='both', expand=True)
    tabview = CTkTabview(master=frame_t_f)
    tabview.pack(fill='both', expand=True)
    tabview.add('Table')
    tabview.add('Chart')

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
    table.tag_configure('even', background='#4f4e4e')
    table.tag_configure('odd', background='#858585')
    table.pack(side='left', fill='both', expand=True)

    fig, ax = plt.subplots()
    plt.xlabel('X')
    plt.ylabel('Y')
    canvas = FigureCanvasTkAgg(fig, master=tabview.tab('Chart'))
    canvas.get_tk_widget().pack(side='right', fill='both', expand=True)
    # Plot the initial points

    root.mainloop()
