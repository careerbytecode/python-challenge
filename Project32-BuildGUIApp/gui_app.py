import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x200")

tk.Label(root, text="Enter number 1:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter number 2:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

tk.Button(root, text="Calculate Sum", command=calculate_sum).pack(pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

root.mainloop()

