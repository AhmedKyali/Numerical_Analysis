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

it = 0
tag = 'even'
flag = False
swap = ""

def Choose_method(choice):
    global Choice
    Choice = choice
    print(Choice)


def LU_Decomp():
    it = 0
    tag = 'even'
    flag = False
    swap = ""
    row_column_select = CTk()
    row_column_select.title("Enter Rows and Columns")
    rows = 3
    columns = 4

    def gauss_e():
        def display_matrix(matrix, title, factor="", it=0, tag='even'):
            table.insert(parent='', index=it, values=(title, matrix[0], factor), tags=tag)
            it += 1
            for row in range(1, len(matrix)):
                table.insert(parent='', index=it, values=("", matrix[row], ""), tags=tag)
                it += 1
            table.insert(parent='', index=it, values=("", "", ""), tags=tag)
            it += 1
            if it % 4 == 0:
                if (it / 4) % 2 == 1:
                    tag = 'odd'
                else:
                    tag = 'even'
            return it, tag


        def partial_pivot_gauss_elimination(matrix):
            n = len(matrix)
            global it
            global tag
            global flag
            global swap
            global Choice
            it, tag = display_matrix(matrix, "Original Matrix", it=it, tag=tag)
            B = []
            B.append(matrix[0][3])
            B.append(matrix[1][3])
            B.append(matrix[2][3])
            # Create identity matrix (L) for LU decomposition
            L = np.identity(n)
            L = L.tolist()

            Factors = []
            for i in range(n):
                # Partial pivoting (if Choice is 'Pivot')
                if Choice == 'Pivot':
                    max_row = i
                    for k in range(i + 1, n):
                        if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                            max_row = k

                    # Swap rows in matrix and L
                    if max_row != i:
                        if i == 1:
                            flag = True
                        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
                        it, tag = display_matrix(matrix, f"After Pivoting Row {i + 1} and {max_row + 1}", it=it, tag=tag)
                        swap += str(i)
                        swap += str(max_row)
                        print(swap)

                # Gaussian elimination
                for j in range(i + 1, n):
                    factor = matrix[j][i] / matrix[i][i]
                    Factors.append(factor)   # Fill L with elimination factors


                    # Update remaining elements in row j
                    for k in range(i, n+1):
                        matrix[j][k] -= factor * matrix[i][k]
                        matrix[j][k] = round(matrix[j][k], 3)
                    it, tag = display_matrix(matrix, f"After Eliminating Row {j + 1} using Row {i + 1}", factor, it=it, tag=tag)

            L[1][0] = Factors[0]
            L[2][0] = Factors[1]
            L[2][1] = Factors[2]

            it, tag = display_matrix(L, "Lower Triangular (L)", it=it, tag=tag)
            it, tag = display_matrix(matrix, "Upper Triangular (U)", it=it, tag=tag)

            while len(swap):
                B[int(swap[0])], B[int(swap[1])] = B[int(swap[1])], B[int(swap[0])]
                it, tag = display_matrix(B, f"After Pivoting Row {int(swap[0])+1} and {int(swap[1])+1} in B", it=it, tag=tag)
                swap = swap[2:]
            if flag:
                L[2][0], L[1][0] = L[1][0], L[2][0]

            if Choice == 'Pivot':
                it, tag = display_matrix(L, f"After Swapping Multiplier M_21 with M_31 in L", it=it, tag=tag)
            # Now you have L (lower triangular) and U (upper triangular) matrices

            # Display L and U matrices (optional)


            return L, matrix, B

        def solve():
            global tag
            global it
            matrix = []
            for i in range(rows):
                matrix.append([float(entry_grid[i][j].get()) for j in range(columns)])

            # Perform LU decomposition
            L, U, B = partial_pivot_gauss_elimination(matrix.copy())  # Use a copy to avoid modifying the original matrix

            # Solve for intermediate vector C (L * C = B)
            n = len(matrix)
            C = np.zeros(n)  # Initialize C vector

            # Forward substitution to solve for C
            for i in range(n):
                sum = 0
                for j in range(i):
                    sum += L[i][j] * C[j]
                C[i] = B[i] - sum
                print(C[i])

            # Solve for solution vector X (U * X = C)
            X = np.zeros(n)  # Initialize X vector

            # Backward substitution to solve for X
            for i in range(n - 1, -1, -1):
                sum = 0
                for j in range(i + 1, n):
                    sum += U[i][j] * X[j]
                X[i] = (C[i] - sum) / U[i][i]
                print(X[i])
            # Display solution (X vector)
            solution_text = ""
            for i in range(rows):
                solution_text += f"x{i + 1} = {X[i]:.2f}\n"
            messagebox.showinfo("Solution", solution_text)

            # Display solution in treeview (optional)
            table.insert("", tk.END, values=("Solution", f"x{1}", f"{X[0]:.2f}"))
            for i in range(1, rows):
                table.insert("", tk.END, values=("", f"x{i + 1}", f"{X[i]:.2f}"))  # Add solution row to treeview

        # ... (rest of your code for window creation, entry grid, solve button, etc.) ...

        # Create tkinter window
        window = CTk()
        window.title("Partial Pivoting Gaussian Elimination with LU Decomposition")

        # Create grid for entering matrix

        # Create three frames for the entry grid
        frames = []
        # Create three frames for the entry grid
        for i in range(rows):
            frames.append(CTkFrame(window))
            frames[i].pack(side="top", fill="both")

        entry_grid = []
        # Create entries and pack them within each frame
        for i in range(rows):
            entry_grid.append([])
            for j in range(columns):
                entry = CTkEntry(window)
                entry.pack(side="left", padx=5, pady=5, in_=frames[i])
                entry_grid[i].append(entry)

        # Button to solve
        solve_button = CTkButton(window, text="Solve", corner_radius=35, fg_color="transparent",
                                 hover_color="#5c5b5b", border_color='#ffffff', border_width=2, command=solve)
        solve_button.pack(side="top")

        # Labels to display result
        result_label_grid = []

        table = ttk.Treeview(window, columns=('Title', 'Row', 'Factor'),
                             show='headings', selectmode="extended")
        table.heading('Title', text='Title')
        table.column("Title", minwidth=0, width=80)
        table.heading('Row', text='Row')
        table.column("Row", minwidth=0, width=80)
        table.heading('Factor', text='Factor')
        table.column("Factor", minwidth=0, width=80)
        table.tag_configure('even', background='#4f4e4e')
        table.tag_configure('odd', background='#858585')

        table.pack(side='bottom', fill='both', expand=True)

        window.mainloop()
    def enter():
        global rows
        global columns
        rows = int(rows_entry.get())
        columns = int(columns_entry.get())
        gauss_e()


    CTkLabel(row_column_select, text="Choose a method", anchor='w').pack(side='top')
    combo = CTkComboBox(master=row_column_select, values=['Standard', 'Pivot'], command=Choose_method).pack(side='top',
                                                                                                            ipadx=22,
                                                                                                            pady=5)

    CTkLabel(row_column_select, text="Rows", anchor='w').pack(side='left')
    text_r = tk.StringVar()
    text_r.set("3")
    rows_entry = CTkEntry(row_column_select, placeholder_text="EX: 3", textvariable=text_r)
    rows_entry.pack(side='left')
    text_c = tk.StringVar()
    text_c.set("4")
    CTkLabel(row_column_select, text="Columns", anchor='w').pack(side='right')
    columns_entry = CTkEntry(row_column_select, placeholder_text="EX: 4", textvariable=text_c)
    columns_entry.pack(side='right')

    submit = CTkButton(row_column_select, text="Submit", corner_radius=35, fg_color="transparent",
                       hover_color="#5c5b5b", border_color='#ffffff', border_width=2, command=enter)
    submit.pack(side="bottom")
    row_column_select.mainloop()
