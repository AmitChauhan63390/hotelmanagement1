from tkinter import*

from PIL import Image,ImageTk   

from git import RootModule
from customer import cust_win
from tkinter import ttk







class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        img1 = Image.open("hotel1.png")
        img1 = img1.resize((1550, 140), Image.LANCZOS)  # Use Image.LANCZOS for antialiasing
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=120)

        lbltitle = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold")
        lbltitle.place(x=0, y=120, width=1550, height=40)
        #===================frame==============================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=160,width=1550,height=620)

        #==================menu================================
        lblmenu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold")
        lblmenu.place(x=0,y=0,width=200,height=40)
        #==================buttonframe=========================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=200,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=19,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand2")
        cust_btn.grid(row=0,column=0)

        room_btn=Button(btn_frame,text="ROOMS",width=19,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0)

        details_btn=Button(btn_frame,text="DETAILS",width=19,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0)

        report_btn=Button(btn_frame,text="REPORT",width=19,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0)

        logout_btn=Button(btn_frame,text="LOGOUT",width=19,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0)

        #======================right image=========================
        img2 = Image.open("taj3.jpg")  # Assuming taj3.jpg is in the same directory as hotel.py
        img2 = img2.resize((1310, 590), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=200, y=160, width=1210, height=540)
        #======================================================

        img3 = Image.open("tajj.jpg")
        img3 = img3.resize((230, 210), Image.LANCZOS)  # Use Image.LANCZOS
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=380, width=200, height=210)


        img4=Image.open("tajj.jpg")
        img4=img4.resize((230,190),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg=Label(self.root,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=580,width=200,height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)



        
        


if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()

    


    