from ntpath import join
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from datetime import datetime



import mysql.connector
import tkinter
import os
import numpy as np


class Journal:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Accounting System")

        ## variables #####################
        self.var_date=StringVar()
        self.var_particular=StringVar()
        self.var_lf=StringVar()
        self.var_debit=StringVar()
        self.var_credit=StringVar()
        self.var_searchtxt=StringVar()
        self.var_search=StringVar()


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
        title_lbl=Label(self.root,text="Journal Enteries",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=130,width=1530,height=35)

        # Frame
        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=5,y=40,width=1500,height=650)

        #left side label frame
        left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Journal Enteries Details',font=('times new roman',12,"bold"))
        left_frame.place(x=10,y=10,width=550,height=510)

        #### image for left frame
        img_left=Image.open(os.path.join("account_images","left_journal_enteries.jpeg"))
        img_left=img_left.resize((540, 120),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=540,height=120)

        ### journal enteries frame
        journal_frame=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text='Journal Enteries',font=('times new roman',12,"bold"))
        journal_frame.place(x=5,y=125,width=540,height=360)


        # Date Labels
        date_label=Label(journal_frame,text='Date:',font=('times new roman',13,"bold"),bg='white')
        date_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        date_entry=ttk.Entry(journal_frame,textvariable=self.var_date,width=30,font=('times new roman',13,"bold"))
        date_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)


        # particulars Labels
        particular_label=Label(journal_frame,text='Particulars:',font=('times new roman',13,"bold"),bg='white')
        particular_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        particular_entry=ttk.Entry(journal_frame,textvariable=self.var_particular,width=30,font=('times new roman',13,"bold"))
        particular_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        # LF Labels
        lf_label=Label(journal_frame,text='L.F:',font=('times new roman',13,"bold"),bg='white')
        lf_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        lf_entry=ttk.Entry(journal_frame,textvariable=self.var_lf,width=30,font=('times new roman',13,"bold"))
        lf_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        # debit labels
        dr_label=Label(journal_frame,text='Debit:',font=('times new roman',13,"bold"),bg='white')
        dr_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        dr_entry=ttk.Entry(journal_frame,textvariable=self.var_debit,width=30,font=('times new roman',13,"bold"))
        dr_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        # credit Labels
        cr_label=Label(journal_frame,text='Credit:',font=('times new roman',13,"bold"),bg='white')
        cr_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        cr_entry=ttk.Entry(journal_frame,textvariable=self.var_credit,width=30,font=('times new roman',13,"bold"))
        cr_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)



        ### frames for left side button
        btn_frame=Frame(journal_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=5,y=240,width=528,height=60)

        ## save button
        save_btn=Button(btn_frame,text='Save',command=self.add_data,width=26,font=('times new roman',13,"bold"),bg='blue',fg='white')
        save_btn.grid(row=0,column=0,pady=10)

        #Reset Button
        reset_btn=Button(btn_frame,text='Reset',command=self.reset_data,width=26,font=('times new roman',13,"bold"),bg='blue',fg='white')
        reset_btn.grid(row=0,column=1,pady=10)
         
################################################################################################
################################################################################################
        #right side label frame
        right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Journal Enteries Details',font=('times new roman',12,"bold"))
        right_frame.place(x=580,y=10,width=730,height=510)

        ### image for right frame
        img_right=Image.open(os.path.join("account_images","right_journal_enteries.jpg"))
        img_right=img_right.resize((720, 120),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=3,y=0,width=720,height=120)


        #Search system
        search_frame=LabelFrame(right_frame,bd=2,bg='white',relief=RIDGE,text='Search System',font=('times new roman',12,"bold"))
        search_frame.place(x=5,y=125,width=720,height=60)

        search_label=Label(search_frame,text='Search By:',font=('times new roman',13,"bold"),bg='red',fg='white')
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #search combo-box
        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search,font=("times new roman",13,"bold"),state="readonly",width=10)
        search_combo['values']=("select","Date","particulars")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        search_entry=ttk.Entry(search_frame,textvariable=self.var_searchtxt,width=28,font=('times new roman',12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #buttons
        search_btn=Button(search_frame,text='Search',command=self.search_data,width=10,font=('times new roman',13,"bold"),bg='blue',fg='white')
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text='Show All',command=self.show_all_data,width=10,font=('times new roman',13,"bold"),bg='blue',fg='white')
        showAll_btn.grid(row=0,column=4,padx=4)

######################################### Table for data show ############################################


        table_frame=LabelFrame(right_frame,bd=2,bg='white',relief=RIDGE)
        table_frame.place(x=5,y=190,width=720,height=292)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.journal_table=ttk.Treeview(table_frame,column=('date',"particulars",'lf','debit','credit'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.journal_table.xview)
        scroll_y.config(command=self.journal_table.yview)


        # for table header
        self.journal_table.heading('date',text="Date")
        self.journal_table.heading('particulars',text="Particulars")
        self.journal_table.heading('lf',text="L.F")
        self.journal_table.heading('debit',text="Debit")
        self.journal_table.heading('credit',text="Credit")
        self.journal_table['show']='headings'

        #setting with for column
        self.journal_table.column('date',width=160)
        self.journal_table.column('particulars',width=350)
        self.journal_table.column('lf',width=120)
        self.journal_table.column('debit',width=280)
        self.journal_table.column('credit',width=280)

        #packing table
        self.journal_table.pack(fill=BOTH,expand=1)

        self.fetch_data()

### function for save data ###########
    def add_data(self):
        if self.var_date.get()=="" or self.var_particular.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="accounting_software")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into journal values(%s,%s,%s,%s,%s)",(
                                                                                self.var_date.get(),
                                                                                self.var_particular.get(),
                                                                                self.var_lf.get(),
                                                                                self.var_debit.get(),
                                                                                self.var_credit.get()
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Journal details has been added Sucessfully",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


###  fetch data from database ###########
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="accounting_software")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from journal")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.journal_table.delete(*self.journal_table.get_children())
            for i in data:
                self.journal_table.insert('',END,values=i)
            conn.commit()
        conn.close()

######    Reset data from form #################

    def reset_data(self):
        self.var_date.set("")
        self.var_particular.set("")
        self.var_lf.set("")
        self.var_debit.set("")
        self.var_credit.set("")


######################   Search data ###################################


    def search_data(self):
        if self.var_searchtxt.get()=="" or self.var_search.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password="root",database="accounting_software")
                my_cursor=conn.cursor()
                query = f"SELECT * FROM journal WHERE {self.var_search.get().lower()} LIKE '%{self.var_searchtxt.get().lower()}%'"
                my_cursor.execute(query)
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.journal_table.delete(*self.journal_table.get_children())
                    for i in rows:
                        self.journal_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


##################  show all data  #######################

    def show_all_data(self):
        self.var_search.set("select")
        self.var_searchtxt.set("")
        self.fetch_data()


if __name__ == "__main__":
    root=Tk()
    obj=Journal(root)
    root.mainloop()
        