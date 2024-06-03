import tkinter as tk
from tkinter import messagebox
from parcel_calculator import calculate_price

class ParcelCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Parcel Calculator")
        master.configure(bg='lightblue')  # Change the background color

        # Create length input label and entry field
        self.length_label = tk.Label(master, text="Length (cm):", bg='lightblue')
        self.length_label.grid(row=0, column=0)
        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1)

        # Create width input label and entry field
        self.width_label = tk.Label(master, text="Width (cm):", bg='lightblue')
        self.width_label.grid(row=1, column=0)
        self.width_entry = tk.Entry(master)
        self.width_entry.grid(row=1, column=1)

        # Create height input label and entry field
        self.height_label = tk.Label(master, text="Height (cm):", bg='lightblue')
        self.height_label.grid(row=2, column=0)
        self.height_entry = tk.Entry(master)
        self.height_entry.grid(row=2, column=1)

        # Create weight input label and entry field
        self.weight_label = tk.Label(master, text="Weight (kg):", bg='lightblue')
        self.weight_label.grid(row=3, column=0)
        self.weight_entry = tk.Entry(master)
        self.weight_entry.grid(row=3, column=1)

        # Create calculate button
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_price)
        self.calculate_button.grid(row=4, column=0, columnspan=2)

    def calculate_price(self):
        # Get parcel dimensions and weight from entry fields
        length = float(self.length_entry.get())
        width = float(self.width_entry.get())
        height = float(self.height_entry.get())
        weight = float(self.weight_entry.get())

        # Calculate parcel price using imported function
        price = calculate_price(length, width, height, weight)

        # Show the result in a messagebox
        messagebox.showinfo("Result", "The price of your parcel is: $" + str(price))

root = tk.Tk()
root.title("Parcel Price Calculator")  # Set a title for the window
parcel_calculator_gui = ParcelCalculatorGUI(root)
root.mainloop()