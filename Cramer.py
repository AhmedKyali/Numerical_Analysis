from customtkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
import numpy as np


it = 0
tag = 'even'
def Cramer():
    it = 0
    tag = 'even'
    row_column_select = CTk()
    row_column_select.title("Enter Rows and Columns")
    rows = 3
    columns = 4

    def cramer():
        def display_matrix(matrix, title, det="", it=0, tag='even'):
            table.insert(parent='', index=it, values=(title, matrix[0], det), tags=tag)
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

        def get_As(matrix):
            # Calculate determinant of original matrix
            As = []
            B = [matrix[0][3], matrix[1][3], matrix[2][3]]
            global it
            global tag
            matrix = np.delete(matrix, 3, 1)
            det_A = np.linalg.det(matrix)
            As.append(det_A)
            it, tag = display_matrix(matrix, "Original Matrix: A", it=it, tag=tag, det=det_A)

            # Create matrices A1, A2, A3, and A4 by replacing columns with B
            A1 = np.copy(matrix)
            A1[:, 0] = B

            A2 = np.copy(matrix)
            A2[:, 1] = B

            A3 = np.copy(matrix)
            A3[:, 2] = B

            # Calculate determinants of A1, A2, A3, and A4
            As.append(np.linalg.det(A1))
            As.append(np.linalg.det(A2))
            As.append(np.linalg.det(A3))

            # Display matrices with calculated determinants (optional)
            # ... (use display_matrix function for each matrix with its determinant)

            it, tag = display_matrix(A1, "Matrix: A_1", it=it, tag=tag, det=As[1])
            it, tag = display_matrix(A2, "Matrix: A_2", it=it, tag=tag, det=As[2])
            it, tag = display_matrix(A3, "Matrix: A_3", it=it, tag=tag, det=As[3])
            return As

        def solve():
            global tag
            global it
            matrix = []
            for i in range(rows):
                matrix.append([float(entry_grid[i][j].get()) for j in range(columns)])

            As = get_As(matrix)
            x = [As[1] / As[0], As[2] / As[0], As[3] / As[0]]

            solution_text = ""
            for i in range(rows):
                solution_text += f"x{i + 1} = {x[i]:.2f}\n"
            messagebox.showinfo("Solution", solution_text)

            # Display result in treeview
            table.insert("", tk.END, values=("Solution", f"x{1}", f"{x[0]:.2f}"))
            for i in range(1, rows):
                table.insert("", tk.END, values=("", f"x{i + 1}", f"{x[i]:.2f}"))  # Add solution row to treeview

            # ... rest of the code for window creation, entry grid, solve button ...

        # ... (rest of your code for window creation, entry grid, solve button, etc.) ...

        # Create tkinter window
        window = CTk()
        window.title("Solve system using Cramer's rule")

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

        table = ttk.Treeview(window, columns=('Title', 'Row', 'Det'),
                             show='headings', selectmode="extended")
        table.heading('Title', text='Title')
        table.column("Title", minwidth=0, width=80)
        table.heading('Row', text='Row')
        table.column("Row", minwidth=0, width=80)
        table.heading('Det', text='Det')
        table.column("Det", minwidth=0, width=80)
        table.tag_configure('even', background='#4f4e4e')
        table.tag_configure('odd', background='#858585')

        table.pack(side='bottom', fill='both', expand=True)

        window.mainloop()

    def enter():
        global rows
        global columns
        rows = int(rows_entry.get())
        columns = int(columns_entry.get())
        cramer()

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

