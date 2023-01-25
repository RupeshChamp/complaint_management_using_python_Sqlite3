from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import ComplaintRegisterDatabase

db=ComplaintRegisterDatabase("complaintRegister.db")

root = Tk()
root.title("Complaint Management System")
root.geometry("1920x1080+0+0")
root.config(bg="#85adad")
root.state("zoomed")

name=StringVar()
age=StringVar()
email=StringVar()
gender=StringVar()
contact=StringVar()


# Entries Frame
entriesFrame = Frame(root,bg="#b3cccc")
entriesFrame.pack(side=TOP,fill=X)
title=Label(entriesFrame,text="Complaint Management System",font=("Calibri,18,Bold"),bg="#b3cccc",fg="white")
title.grid(row=0,columnspan=3,padx=10,pady=20,sticky="w")

lblName=Label(entriesFrame,text="Name",font=("Calibri",16),bg="#b3cccc",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName=Entry(entriesFrame,textvariable=name,font=("Calibri",16),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky="w")

lblAge=Label(entriesFrame,text="Age",font=("Calibri",16),bg="#b3cccc",fg="white")
lblAge.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtAge=Entry(entriesFrame,textvariable=age,font=("Calibri",16),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky="w")

lblEmail=Label(entriesFrame,text="Email",font=("Calibri",16),bg="#b3cccc",fg="white")
lblEmail.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtEmail=Entry(entriesFrame,textvariable=email,font=("Calibri",16),width=30)
txtEmail.grid(row=2,column=1,padx=10,pady=10,sticky="w")

lblGender=Label(entriesFrame,text="Gender",font=("Calibri",16),bg="#b3cccc",fg="white")
lblGender.grid(row=2,column=2,padx=10,pady=10,sticky="w")
comboGender=ttk.Combobox(entriesFrame,textvariable=gender,font=("Calibri",16),width=28,state="readonly")
comboGender['values'] = (" ","Male","Female")
comboGender.grid(row=2,column=3,padx=10,pady=10,sticky="w")

lblContact=Label(entriesFrame,text="Contact",font=("Calibri",16),bg="#b3cccc",fg="white")
lblContact.grid(row=3,column=0,padx=10,pady=10,sticky="w")
txtContact=Entry(entriesFrame,textvariable=contact,font=("Calibri",16),width=30)
txtContact.grid(row=3,column=1,padx=10,pady=10,sticky="w")

lblAddress=Label(entriesFrame,text="Address",font=("Calibri",16),bg="#b3cccc",fg="black")
lblAddress.grid(row=4,column=0,padx=10,pady=10,sticky="w")

txtAddress=Text(entriesFrame,font=("Calibri",16),width=85,height=2)
txtAddress.grid(row=4,column=1,columnspan=4,padx=10,pady=10,sticky="w")

lblComplaint=Label(entriesFrame,text="Complaint",font=("Calibri",16),bg="#b3cccc",fg="black")
lblComplaint.grid(row=6,column=0,padx=10,pady=10,sticky="w")

txtComplaint=Text(entriesFrame,font=("Calibri",16),width=85,height=5)
txtComplaint.grid(row=6,column=1,columnspan=4,padx=10,pady=10,sticky="w")

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    name.set(row[1])
    age.set(row[2])
    email.set(row[3])
    gender.set(row[4])
    contact.set(row[5])
    txtAddress.delete(1.0,END)
    txtAddress.insert(END,row[6])
    txtComplaint.delete(1.0,END)
    txtComplaint.insert(END,row[7])

def displayAll():
    tv.delete(*tv.get_children())
    for rows in db.fetch():
        tv.insert("", END, values=rows)

def add_complaint():
    if txtName.get()=="" or txtAge.get()=="" or txtEmail.get()=="" or comboGender.get()==""or txtContact.get()=="" or \
            txtAddress.get(1.0,END) =="" or txtComplaint.get(1.0,END)=="":
        messagebox.showerror("Error in input", "Please enter the details")
        return
    db.insert(txtName.get(),txtAge.get(),txtEmail.get(),comboGender.get(),txtContact.get(),txtAddress.get(1.0,END),
              txtComplaint.get(1.0,END))
    messagebox.showinfo("Success","Data inserted successfully")
    clearAll()
    displayAll()

def update_complaint():
    if txtName.get() == "" or txtAge.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or \
            txtContact.get() == ""or txtAddress.get(
            1.0, END) == "" or txtComplaint.get(1.0, END) == "":
        messagebox.showerror("Error in input", "Please enter the details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtEmail.get(), comboGender.get(), txtContact.get(),
              txtAddress.get(1.0, END),txtComplaint.get(1.0, END))
    messagebox.showinfo("Success", "Data updated successfully")
    clearAll()
    displayAll()


def delete_complaint():
    db.remove(row[0])
    clearAll()
    displayAll()


def clearAll():
    name.set("")
    age.set("")
    email.set("")
    gender.set("")
    contact.set("")
    txtAddress.delete(1.0,END)
    txtComplaint.delete(1.0,END)

btnFrame = Frame(entriesFrame,bg="#b3cccc")
btnFrame.grid(row=7,column=0,columnspan=4,padx=10,pady=10,sticky="w")

btnAdd=Button(btnFrame,command=add_complaint,text="Add Details", font=("Calibri",16,"bold"),fg="white",width=15,bd=0,bg="#006080")
btnAdd.grid(row=0,column=0)

btnUpdate=Button(btnFrame,command=update_complaint,text="Update Details", font=("Calibri",16,"bold"),fg="white",width=15,bd=0,bg="#007399")
btnUpdate.grid(row=0,column=1,padx=10)

btnDelete=Button(btnFrame,command=delete_complaint,text="Delete Details", font=("Calibri",16,"bold"),fg="white",width=15,bd=0,bg="#0099cc")
btnDelete.grid(row=0,column=2,padx=10)

btnClear=Button(btnFrame,command=clearAll,text="Clear Details", font=("Calibri",16,"bold"),fg="white",width=15,bd=0,bg="#1ac6ff")
btnClear.grid(row=0,column=3,padx=10)

# Table Frame

treeFrame=Frame(root,bg="#ecf0f1")
treeFrame.place(x=0,y=520,width=1535,height=520)
style=ttk.Style()
style.configure("mystyle.Treeview",font=("Calibri",12),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=("Calibri",14,"bold"))

tv=ttk.Treeview(treeFrame,columns=("1","2","3","4","5","6","7","8"),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=5)
tv.heading("2",text="Name")
tv.heading("3",text="Age")
tv.column("3",width=5)
tv.heading("4",text="Email")
tv.heading("5",text="Gender")
tv.column("5",width=5)
tv.heading("6",text="Contact")
tv.heading("7",text="Address")
tv.heading("8",text="Complaint")

tv['show'] = "headings"
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)


displayAll()
root.mainloop()
