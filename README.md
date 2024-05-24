# Numerical Analysis Project

## Overview

This project is a college assignment focused on numerical analysis, where various methods and techniques from data science have been applied. The project is implemented in Python and utilizes libraries such as NumPy for mathematical operations and Matplotlib for visualizations. The goal of the project is to demonstrate the application of numerical methods to solve mathematical problems and to visualize the results effectively.

## Features

- Implementation of various numerical methods
- Use of NumPy for efficient mathematical computations
- Visualization of results using Matplotlib
- Examples and test cases for each method

## Numerical Methods Implemented

1. **Root Finding Methods**
   - Bisection Method
   - Newton-Raphson Method
   - Secant Method

2. **Interpolation and Polynomial Approximation**
   - Lagrange Interpolation
   - Newton's Divided Differences

3. **Numerical Integration**
   - Trapezoidal Rule
   - Simpson's Rule

4. **Linear Algebraic Equations**
   - Gaussian Elimination
   - LU Decomposition

5. **Ordinary Differential Equations (ODEs)**
   - Euler's Method
   - Runge-Kutta Methods

## Installation

To run this project, you need to have Python installed along with the following libraries:

- NumPy
- Matplotlib

You can install these libraries using pip:

```sh
pip install numpy matplotlib
```

## Usage

Clone the repository:

```sh
git clone https://github.com/AhmedKyali/Numerical_Analysis.git
cd Numerical_Analysis
```

Run the main script to see the implementation and visualization of different numerical methods:

```sh
python main.py
```



## Examples

### Root Finding: Bisection Method

```python
while cur_Error > req_Error and i < req_iter:
  plt.title(f'Root is {round(x_r,3)} for Iteration {i+1}')
  
  
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
```

### System Equation: Cramer's Rule

```python
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
        table.insert("", tk.END, values=("", f"x{i + 1}", f"{x[i]:.2f}"))
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Contact

For any questions or suggestions, feel free to open an issue or contact me at ahmed.kaiialy@gmail.com.

---

This project provided a valuable opportunity to bridge the concepts of numerical analysis with data science techniques, showcasing the practical application of these methods in solving and visualizing mathematical problems.
