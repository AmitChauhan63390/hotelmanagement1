from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3
import random




class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1150x500+230+240")

        #====================var==============================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_cust_mname=StringVar()
        self.var_cust_gender=StringVar()
        self.var_cust_post=StringVar()
        self.var_cust_mobile=StringVar()
        self.var_cust_email=StringVar()
        self.var_cust_nat=StringVar()
        self.var_cust_address=StringVar()
        self.var_cust_idproof=StringVar()
        self.var_cust_idnumber=StringVar()




    #===================title==============================
        lbltitle=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold")
        lbltitle.place(x=0,y=0,width=1150,height=40)

        #=================logo==========================
        img3=Image.open("/home/amit/Desktop/HotelManagementSystem/taj.webp")
        img3=img3.resize((100,40),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=100,height=40)

        #=================labelframe=========================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,font=("times new roman",12,"bold"),text="Customer Details",padx=2)
        labelframeleft.place(x=5,y=40,width=450,height=450)

        #=================labels and entries=================

        #cust_ref
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=30,font=("arial",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        #cust_name

        lbl_cust_name=Label(labelframeleft,text="Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)
        entry_name=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=30,font=("arial",13,"bold"))
        entry_name.grid(row=1,column=1)

        #mother name
        lbl_cust_mname=Label(labelframeleft,text="Mother's Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_mname.grid(row=2,column=0,sticky=W)
        entry_mname=ttk.Entry(labelframeleft,textvariable=self.var_cust_mname,width=30,font=("arial",13,"bold"))
        entry_mname.grid(row=2,column=1)

        #gender
        lbl_cust_gender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_cust_gender,font=("arial",12,"bold"),width=32,state="readonly")
        combo_gender["values"]=("Male","Female","Others")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #postcode
        lbl_cust_postcode=Label(labelframeleft,text="Post Code:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_postcode.grid(row=4,column=0,sticky=W)
        entry_postcode=ttk.Entry(labelframeleft,textvariable=self.var_cust_post,width=30,font=("arial",13,"bold"))
        entry_postcode.grid(row=4,column=1)
        #email
        lbl_cust_email=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_email.grid(row=5,column=0,sticky=W)
        entry_email=ttk.Entry(labelframeleft,textvariable=self.var_cust_email,width=30,font=("arial",13,"bold"))
        entry_email.grid(row=5,column=1)
        #phone
        lbl_cust_phone=Label(labelframeleft,text="Phone:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_phone.grid(row=6,column=0,sticky=W)
        entry_phone=ttk.Entry(labelframeleft,textvariable=self.var_cust_mobile,width=30,font=("arial",13,"bold"))
        entry_phone.grid(row=6,column=1)
        #nationality

        lbl_cust_nat=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_nat.grid(row=7,column=0,sticky=W)
        combo_nat=ttk.Combobox(labelframeleft,textvariable=self.var_cust_nat,font=("arial",12,"bold"),width=32,state="readonly")
        combo_nat["values"]=("Indian","British","American")
        combo_nat.current(0)
        combo_nat.grid(row=7,column=1)

        #id type
        lbl_cust_idtype=Label(labelframeleft,text="idtype:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_idtype.grid(row=8,column=0,sticky=W)
        combo_idtype=ttk.Combobox(labelframeleft,textvariable=self.var_cust_idproof,font=("arial",12,"bold"),width=32,state="readonly")
        combo_idtype["values"]=("Aadhar Card","PAN","Voter id")
        combo_idtype.current(0)
        combo_idtype.grid(row=8,column=1)
        


        #id no
        lbl_cust_id=Label(labelframeleft,text="Identity No:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_id.grid(row=9,column=0,sticky=W)
        entry_id=ttk.Entry(labelframeleft,textvariable=self.var_cust_idnumber,width=30,font=("arial",13,"bold"))
        entry_id.grid(row=9,column=1)
        #address
        lbl_cust_address=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_address.grid(row=10,column=0,sticky=W)
        entry_address=ttk.Entry(labelframeleft,textvariable=self.var_cust_address,width=30,font=("arial",13,"bold"))
        entry_address.grid(row=10,column=1)

        #============================btns=============================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=380,width=443,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1,pady=1)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1,pady=1)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1,pady=1)

        btnReset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnReset.grid(row=0,column=3,padx=1,pady=1)

        #========================tableFrame==============================

        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"),padx=2)
        table_frame.place(x=455,y=40,width=690,height=450)

        lblsearchby=Label(table_frame,font=("arial",12,"bold"),text="Search",bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        combo_search=ttk.Combobox(table_frame,font=("arial",12,"bold"),width=20,state="readonly")
        combo_search["values"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        entry_search=ttk.Entry(table_frame,width=24,font=("arial",13,"bold"))
        entry_search.grid(row=0,column=2,padx=2)

        btnsearch=Button(table_frame,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=6)
        btnsearch.grid(row=0,column=3,padx=1,pady=1)

        btnshowall=Button(table_frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=6)
        btnshowall.grid(row=0,column=4,padx=1,pady=1)

        #======================show data table=============================

        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=683,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nat","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref",text="ref no.")
        self.cust_details_table.heading("name",text="name")
        self.cust_details_table.heading("mother",text="Mother Name")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("post",text="PostCode")
        self.cust_details_table.heading("mobile",text="Mobile")
        self.cust_details_table.heading("email",text="Email")
        self.cust_details_table.heading("nat",text="Nationality")
        self.cust_details_table.heading("idproof",text="ID Proof")
        self.cust_details_table.heading("idnumber",text="Id no.")
        self.cust_details_table.heading("address",text="Address")

        self.cust_details_table["show"]="headings"
        self.cust_details_table.pack(fill=BOTH,expand=1)


        




        
    

if __name__=="__main__":
    root=Tk()
    obj=cust_win(root)
    root.mainloop()