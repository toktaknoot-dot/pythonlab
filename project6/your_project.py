#Create gui for a simple calculator using tkinter in python
import tkinter as tk

# Define the calculator functions
def add():    
    num1 = float(entry1.get())    
    num2 = float(entry2.get())
    result = num1 + num2
    label3.config(text="Result: " + str(result))    
def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 - num2
    label3.config(text="Result: " + str(result))
def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    label3.config(text="Result: " + str(result))
def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    if num2 != 0:
        result = num1 / num2
        label3.config(text="Result: " + str(result))
    else:
        label3.config(text="Error: Division by zero")   
# Create the main window
root = tk.Tk()
root.title("Calculator")    
# Create the input fields and labels
label1 = tk.Label(root, text="Number 1:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)
label2 = tk.Label(root, text="Number 2:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)
# Create the buttons
button_add = tk.Button(root, text="+", command=add)
button_add.grid(row=2, column=0)
button_subtract = tk.Button(root, text="-", command=subtract)
button_subtract.grid(row=2, column=1)
button_multiply = tk.Button(root, text="*", command=multiply)
button_multiply.grid(row=3, column=0)
button_divide = tk.Button(root, text="/", command=divide)
button_divide.grid(row=3, column=1)
# Create the result label
label3 = tk.Label(root, text="Result: ")
label3.grid(row=4, column=0, columnspan=2)
# Start the main event loop
root.mainloop() 
