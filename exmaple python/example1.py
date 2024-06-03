from tkinter import*
from tkinter import messagebox
import example1_DB as data
import example1View as viewdata

db = data.connectionDB()

window = Tk()
window.title("VACCINE REGISTRATION")

def radio_sel():
    citizen = citizenR.get()
    age = int(ageR.get())

    if citizen == "Yes":
        if age >= 60:
            ageStatus = "Senior Citizen"
            remarks = "Eligible for Vaccine"
        elif 30 <= age < 60:
            ageStatus = "Adult"
            remarks = "Eligible for Vaccine"
        elif 18 <= age < 30:
            ageStatus = "Teenager"
            remarks = "Eligible for Vaccine"
        else:
            ageStatus = "Child"
            remarks = "Not eligible for Vaccine"
    else:
        ageStatus = "None"
        remarks = "Invalid Age"

    categoryE.configure(text=ageStatus)
    vacStatusE.configure(text=remarks)

def insert():
    name = nameE.get()
    icnumber = icnumberE.get()
    age = ageR.get()
    citizen = citizenR.get()
    Diabetes = DiabetesC.get()
    Hyper = HyperC.get()
    Heart = HeartC.get()
    ageStatus = categoryE.cget("text")
    vacStatus = vacStatusE.cget("text")

    mesej = messagebox.askquestion("Submit","Are you sure to Submit?")
    if mesej == 'yes':
        try:
            db.cur.execute('INSERT INTO listcitizen (icnumber, name, age, citizen, Diabetes, Hyper, Heart, ageStatus, vacStatus) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)', 
                    (icnumber, name, age, citizen, Diabetes, Hyper, Heart, ageStatus, vacStatus))
            db.conn.commit()
            messagebox.showinfo("Record Success","Record inserted")
        except:
            db.conn.rollback()
    else:
        messagebox.showerror("Record","Record not inserted")

def selectAll():
    if(allC.get()==1):
        c1.select()
        c2.select()
        c3.select()       
    else: 
        c1.deselect()
        c2.deselect()
        c3.deselect()

#Data citizen
citizenlbl=Label(window, text="Malaysian citizen : ", font=("Arial Bold",11))
citizenlbl.grid(column=0, row=1, sticky='W')
#radio button
citizenR = StringVar()
yesR = Radiobutton(window, text="Yes", variable=citizenR, value="Yes", command=radio_sel)
yesR.grid(column=1, row=1, sticky='W')
noR = Radiobutton(window, text="No", variable=citizenR, value="No", command=radio_sel)
noR.grid(column=1, row=2, sticky='W')

lbl1=Label(window, text="----- Please complete the information below -----", font=("Arial Bold", 12))
lbl1.grid(columnspan=3, row=3, sticky='W')

#Data name
namelbl=Label(window, text="Name : ", font=("Arial Bold",11))
namelbl.grid(column=0, row=4, sticky='W')
nameE=Entry(window, width=30)
nameE.grid(column=1, row=4, sticky='W')

#Data icnumber
icnumberlbl=Label(window, text="IC Number : ", font=("Arial Bold",11))
icnumberlbl.grid(column=0, row=5, sticky='W')
icnumberE=Entry(window, width=30)
icnumberE.grid(column=1, row=5, sticky='W')

#Data age
ageR = IntVar() 
agelbl=Label(window, text="Age : ", font=("Arial Bold",11))
agelbl.grid(column=0, row=6, sticky='W')
ageE=Entry(window, width=30, textvariable=ageR)
ageE.grid(column=1, row=6, sticky='W')

lbl2=Label(window, text="Do you have the following diseases :", font=("Arial Bold", 11))
lbl2.grid(columnspan=3, row=8, sticky='W')

#Data diseases
#checkbox
DiabetesC=StringVar(window)    
c1=Checkbutton(window,text='Diabetes Mellitus',onvalue="Yes", offvalue="No",variable=DiabetesC)
c1.grid(column=0, row=9, sticky='W')

HyperC=StringVar(window)
c2=Checkbutton(window,text='Hypertension',onvalue="Yes", offvalue="No",variable=HyperC)
c2.grid(column=0, row=10, sticky='W')

HeartC=StringVar(window)
c3=Checkbutton(window,text='Heart Disease',onvalue="Yes", offvalue="No",variable=HeartC)
c3.grid(column=0, row=11, sticky='W')

allC=IntVar(window)
c4=Checkbutton(window,text='Select All',variable=allC, command=selectAll)
c4.grid(column=0, row=12, sticky='W')

#Button to check status
btnCheck=Button(window, text="Check Status", fg="black", font=("Arial Bold",10), command=radio_sel)
btnCheck.grid(column=1, row=14)

lbl3=Label(window, text="Your Status :", font=("Arial Bold", 12))
lbl3.grid(column=0, row=16, sticky='W')

#Data category
categorylbl=Label(window, text="You are : ", font=("Arial Bold",11))
categorylbl.grid(column=0, row=17, sticky='W')
categoryE=Label(window, text='', width=25, font=("Arial Bold", 10), borderwidth=2, relief="groove")
categoryE.grid(column=1, row=17, sticky='W')

#Data vaccine status
vacStatuslbl=Label(window, text="Vaccine status : ", font=("Arial Bold",11))
vacStatuslbl.grid(column=0, row=18, sticky='W')
vacStatusE=Label(window, text='', width=25, font=("Arial Bold", 10), borderwidth=2, relief="groove")
vacStatusE.grid(column=1, row=18, sticky='W')

#Button to submit data
btnInsert=Button(window, text="Submit", fg="black", font=("Arial Bold",10), command=insert)
btnInsert.grid(column=1, row=20)

#Button to new window to view list data
btnView=Button(window, text="View", fg="black", font=("Arial Bold",10), command=viewdata.open)
btnView.grid(column=1, row=22)

window.geometry("400x450")
window.mainloop()