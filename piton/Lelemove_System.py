import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Create a MySQL database connection without specifying the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',  # replace with your actual username
    password=''  # replace with your actual password
)

# Create a cursor
c = conn.cursor()

# Create the database if it doesn't exist
c.execute('CREATE DATABASE IF NOT EXISTS Lelemove_System')

# Now we can specify the database
conn.database = 'Lelemove_System'

# Create a table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS Items (
        Item_id VARCHAR(10) PRIMARY KEY,
        Item_height VARCHAR(5),
        Item_width VARCHAR(5),
        Item_length VARCHAR(5),
        Item_volume VARCHAR(10),
        Item_price VARCHAR(5)
    )
''')
conn.commit()

class App:
    def __init__(self, master):
        self.master = master
        master.title("Lelemove System")

        # Create entry fields for each attribute
        self.entries = {}
        for i, attribute in enumerate(["Item_id", "Item_height", "Item_width", "Item_length", "Item_volume", "Item_price"]):
            tk.Label(master, text=attribute).grid(row=i, column=0)
            self.entries[attribute] = tk.Entry(master)
            self.entries[attribute].grid(row=i, column=1)

        # Create a button to add data to the database
        self.add_button = tk.Button(master, text="Add to database", command=self.add_to_database)
        self.add_button.grid(row=6, column=0, columnspan=2)

    def add_to_database(self):
        # Get data from entry fields
        data = {attribute: entry.get() for attribute, entry in self.entries.items() if entry.get() != ''}
    
        if len(data) != 6:  # if not all fields are filled in
            messagebox.showinfo("Error", "Please fill in all fields.")
            return
    
        # Insert data into the table
        query = '''
            INSERT INTO Items (Item_id, Item_height, Item_width, Item_length, Item_volume, Item_price)
            VALUES (%(Item_id)s, %(Item_height)s, %(Item_width)s, %(Item_length)s, %(Item_volume)s, %(Item_price)s)
        '''
        c = conn.cursor()  # create a new cursor
        try:
            c.execute(query, data)
            conn.commit()
            # Notify the user that the data has been stored
            messagebox.showinfo("Success", "The data has been stored in the database.")
        except mysql.connector.Error as err:
            messagebox.showinfo("Error", f"Failed to insert data into database: {err}")

root = tk.Tk()
app = App(root)  # create an instance of the App class
root.mainloop()