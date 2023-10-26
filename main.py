from ntpath import join
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


import mysql.connector
import tkinter
import os
import numpy as np



from journal import Journal
from balance_sheet import BalanceSheet
from ledger import Ledger
from capital import Capital

class Account:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Accounting System")
        
        
        #first image for header
        # img=Image.open(r"college_images\eemc.jpg")
        img=Image.open(os.path.join("account_images", "istockphoto-1.jpg"))
        img=img.resize((500, 130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        # second image for header
        # img2=Image.open(r"college_images\face_re.jpg")
        img2=Image.open(os.path.join("account_images","istockphoto-2.jpg"))
        img2=img2.resize((500, 130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)    

        # third image for header
        # img3=Image.open(r"college_images\face_re.jpg")
        img3=Image.open(os.path.join("account_images","istockphoto-3.jpg"))
        img3=img3.resize((500, 130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #Background image
        img4=Image.open(os.path.join("account_images","back_ground.jpg"))
        img4=img4.resize((1530, 710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        ## Title
        title_lbl=Label(self.root,text="ACCOUNTING SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=130,width=1530,height=35)
        
        # Journal Enteries Button
        img5=Image.open(os.path.join("account_images","journal_enteries_button.jpeg"))
        img5=img5.resize((180,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        jb=Button(bg_img,image=self.photoimg5,command=self.journal_details,cursor='hand2')
        jb.place(x=200,y=80,width=180,height=180)

        jb_1=Button(bg_img,text="Journal Enteries",command=self.journal_details,cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        jb_1.place(x=200,y=240,width=180,height=40)


        # ledger Button
        img6=Image.open(os.path.join("account_images","ledger_enteries_button.jpeg"))
        img6=img6.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        lb=Button(bg_img,image=self.photoimg6,command=self.ledger_details,cursor='hand2')
        lb.place(x=500,y=80,width=180,height=180)

        lb_1=Button(bg_img,text="Ledger",command=self.ledger_details,cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        lb_1.place(x=500,y=240,width=180,height=40)



        # Balance Sheet Button
        img7=Image.open(os.path.join("account_images","balance_sheet_button.jpeg"))
        img7=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        bb=Button(bg_img,image=self.photoimg7,command=self.balance_sheet_details,cursor='hand2')
        bb.place(x=800,y=80,width=180,height=180)

        bb_1=Button(bg_img,text="Balance Sheet",command=self.balance_sheet_details,cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        bb_1.place(x=800,y=240,width=180,height=40)


        #  Capital Account Button
        img8=Image.open(os.path.join("account_images","capital_account_button.png"))
        img8=img8.resize((180,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        ca_b=Button(bg_img,image=self.photoimg8,command=self.capital_account_details,cursor='hand2')
        ca_b.place(x=1100,y=80,width=180,height=180)

        ca_b_1=Button(bg_img,text="Capital Account",command=self.capital_account_details,cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        ca_b_1.place(x=1100,y=240,width=180,height=40)

########################### Second row button####################################
        # Current Account Button
        img9=Image.open(os.path.join("account_images","current_account_button.jpeg"))
        img9=img9.resize((180,180),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        cu_b=Button(bg_img,image=self.photoimg9,cursor='hand2')
        cu_b.place(x=200,y=350,width=180,height=180)

        cu_b_1=Button(bg_img,text="Current Account",cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        cu_b_1.place(x=200,y=500,width=180,height=40)

        # Realisation Account Button
        img10=Image.open(os.path.join("account_images","realisation_acc_button.jpg"))
        img10=img10.resize((180,180),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        rb=Button(bg_img,image=self.photoimg10,cursor='hand2')
        rb.place(x=500,y=350,width=180,height=180)

        rb_1=Button(bg_img,text="Realisation Account",cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        rb_1.place(x=500,y=500,width=180,height=40)

        # Revaluation Account Button
        img11=Image.open(os.path.join("account_images","revaluation_acc_button.jpg"))
        img11=img11.resize((180,180),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        re_b=Button(bg_img,image=self.photoimg11,cursor='hand2')
        re_b.place(x=800,y=350,width=180,height=180)

        re_b_1=Button(bg_img,text="Revaluation Account",cursor='hand2',font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        re_b_1.place(x=800,y=500,width=180,height=40)


        # Exit Button
        img12=Image.open(os.path.join("account_images","exit_button.jpg"))
        img12=img12.resize((180,180),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        ex_b=Button(bg_img,image=self.photoimg12,command=self.iexit,cursor='hand2')
        ex_b.place(x=1100,y=350,width=180,height=180)

        ex_b_1=Button(bg_img,text="Exit",cursor='hand2',command=self.iexit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        ex_b_1.place(x=1100,y=500,width=180,height=40)


############################ functions button #####################################

    def journal_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Journal(self.new_window)



    def balance_sheet_details(self):
        self.new_window=Toplevel(self.root)
        self.app=BalanceSheet(self.new_window)


    def ledger_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Ledger(self.new_window)


    def capital_account_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Capital(self.new_window)

    


        





##########  exit button functions #############################

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Accounting System","Are you sure exit this system",parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return



if __name__ == "__main__":
    root=Tk()
    obj=Account(root)
    root.mainloop()