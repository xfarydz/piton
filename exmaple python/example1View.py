from tkinter import * 
import tkinter as tk
import example1_DB as data
from tkinter import ttk

db = data.connectionDB()

def open():
    db.cur.execute("SELECT * FROM listcitizen")
    result = db.cur.fetchall()
    my_w=Tk()
    my_w.geometry('900x400')
    my_w.title("View All Data")
    
    trv=ttk.Treeview(my_w,selectmode='browse')
    trv.grid(row=1,column=1,padx=20,pady=20)
    trv["columns"]=("1","2","3","4","5","6","7","8","9")
    trv['show']='headings'
    trv.column("1",width=80,anchor='c')
    trv.column("2",width=80,anchor='c')
    trv.column("3",width=80,anchor='c')
    trv.column("4",width=80,anchor='c')
    trv.column("5",width=100,anchor='c')
    trv.column("6",width=100,anchor='c')
    trv.column("7",width=100,anchor='c')
    trv.column("8",width=80,anchor='c')
    trv.column("9",width=150,anchor='c')

    trv.heading("1",text="Ic Number")
    trv.heading("2",text="Name")
    trv.heading("3",text="Age")
    trv.heading("4",text="Citizen")
    trv.heading("5",text="Diabetes Mellitus")
    trv.heading("6",text="Hypertension")
    trv.heading("7",text="Heart Disease")
    trv.heading("8",text="Age Status")
    trv.heading("9",text="Vaccien Status")

    for dt in result:
        print(dt)
        trv.insert("",'end',id=dt[0],values=(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8]))
    my_w.mainloop()
