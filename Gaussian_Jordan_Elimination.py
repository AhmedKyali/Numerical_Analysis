from customtkinter import *
import tkinter as tk
from tkinter import messagebox, ttk

it = 0
tag = 'even'

def Gauss_j_e():
    tag = 'even'
    row_column_select = CTk()
    row_column_select.title("Enter Rows and Columns")
    rows = 3
    columns = 4

    def Choose_method(choice):
        global Choice
        Choice = choice
        print(Choice)
    def gauss_j_e():

        def back_substitution(matrix):
            n = len(matrix)
            x = [0] * n  # Initialize solution vector

            # Iterate backwards from the last row
            for i in range(n - 1, -1, -1):
                sum = 0
                for j in range(i + 1, n):
                    sum += matrix[i][j] * x[j]
                x[i] = (matrix[i][n] - sum) / matrix[i][i]

            return x


        def display_matrix(matrix, title, factor="", it = 0, tag = 'even'):
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


        def gauss_jordan_elimination(matrix):
            n = len(matrix)
            global it
            global tag
            it, tag = display_matrix(matrix, "Original Matrix", it=it, tag=tag)

            # Gaussian Jordan Elimination with Partial Pivoting
            for i in range(n):
                print(Choice)
                if Choice == 'Pivot':
                    max_row = i
                    for k in range(i + 1, n):
                        if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                            max_row = k

                    # Swap rows if necessary
                    if max_row != i:
                        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
                        it, tag = display_matrix(matrix, f"After Pivoting Row {i + 1} and {max_row + 1}", it=it, tag=tag)

                # Make diagonal element 1 (if not zero)
                if abs(matrix[i][i]) < 1e-10:
                    # Check for singular matrix (optional)
                    messagebox.showerror("Error", "No solution due to singular matrix.")
                    return None
                factor = 1 / matrix[i][i]
                for k in range(n + 1):
                    matrix[i][k] *= factor
                    matrix[i][k] = round(matrix[i][k], 3)
                it, tag = display_matrix(matrix, f"Normalized Row {i + 1}", factor, it=it, tag=tag)

                # Eliminate elements above and below the diagonal element
                for j in range(n):
                    if i != j:
                        factor = matrix[j][i]
                        for k in range(n + 1):
                            matrix[j][k] -= factor * matrix[i][k]
                            matrix[j][k] = round(matrix[j][k], 3)
                        it, tag = display_matrix(matrix, f"Eliminating Element in Row {j + 1}", factor, it=it, tag=tag)

            # Back substitution (omitted for simplicity)

            # Return final matrix
            return matrix


        def solve():
            global tag
            global it
            matrix = []
            for i in range(rows):
                matrix.append([float(entry_grid[i][j].get()) for j in range(columns)])

            result_matrix = gauss_jordan_elimination(matrix)

            # Display result (modify to handle different cases)
            if result_matrix is not None:
                it, tag = display_matrix(result_matrix, "Final Matrix:", it=it, tag=tag)

                x = back_substitution(result_matrix)

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
        window.title("Gaussian Jordan Elimination")
        # Initial window for rows and columns


        # Get rows and columns from entry fields

        # ... (rest of the code for main window) ...

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
        gauss_j_e()




    CTkLabel(row_column_select, text="Choose a method", anchor='w').pack(side='top')
    combo = CTkComboBox(master=row_column_select, values=['Standard', 'Pivot'], command=Choose_method).pack(side='top',
                                                                                                    ipadx=22, pady=5)

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


