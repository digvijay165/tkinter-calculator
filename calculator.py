from tkinter import *

# Create main window
root = Tk()
root.title("Tkinter Calculator")
root.geometry("300x400")

# Entry widget to display numbers and results
display = Entry(root, width=20, font=("Arial", 18), borderwidth=5, justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Variables to store first number and selected operator
first_number = 0
operator = ""

# Function to insert numbers into the display
def click(number):
    display.insert(END, str(number))

# Function to clear the display
def clear():
    display.delete(0, END)

# Arithmetic functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error"
    return a / b

# Function to save the first number and operator
def set_operator(op):
    global first_number, operator

    if display.get() == "":
        return

    first_number = float(display.get())
    operator = op
    display.delete(0, END)

# Function to calculate the result
def calculate():
    global first_number, operator

    if display.get() == "":
        return

    second_number = float(display.get())

    if operator == "+":
        result = add(first_number, second_number)
    elif operator == "-":
        result = subtract(first_number, second_number)
    elif operator == "*":
        result = multiply(first_number, second_number)
    elif operator == "/":
        result = divide(first_number, second_number)
    else:
        result = "Error"

    display.delete(0, END)
    display.insert(0, str(result))

# Number Buttons
Button(root, text="7", width=6, height=2, command=lambda: click(7)).grid(row=1, column=0)
Button(root, text="8", width=6, height=2, command=lambda: click(8)).grid(row=1, column=1)
Button(root, text="9", width=6, height=2, command=lambda: click(9)).grid(row=1, column=2)
Button(root, text="/", width=6, height=2, command=lambda: set_operator("/")).grid(row=1, column=3)

Button(root, text="4", width=6, height=2, command=lambda: click(4)).grid(row=2, column=0)
Button(root, text="5", width=6, height=2, command=lambda: click(5)).grid(row=2, column=1)
Button(root, text="6", width=6, height=2, command=lambda: click(6)).grid(row=2, column=2)
Button(root, text="*", width=6, height=2, command=lambda: set_operator("*")).grid(row=2, column=3)

Button(root, text="1", width=6, height=2, command=lambda: click(1)).grid(row=3, column=0)
Button(root, text="2", width=6, height=2, command=lambda: click(2)).grid(row=3, column=1)
Button(root, text="3", width=6, height=2, command=lambda: click(3)).grid(row=3, column=2)
Button(root, text="-", width=6, height=2, command=lambda: set_operator("-")).grid(row=3, column=3)

Button(root, text="0", width=6, height=2, command=lambda: click(0)).grid(row=4, column=0)
Button(root, text="C", width=6, height=2, command=clear).grid(row=4, column=1)
Button(root, text="=", width=6, height=2, command=calculate).grid(row=4, column=2)
Button(root, text="+", width=6, height=2, command=lambda: set_operator("+")).grid(row=4, column=3)

# Start the GUI
root.mainloop()