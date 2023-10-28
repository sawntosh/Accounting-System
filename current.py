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


class Current:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Accounting System")

        ## variables #####################
        self.var_date1=StringVar()
        self.var_particular1=StringVar()
        self.var_partner1=StringVar()
        self.var_partner2=StringVar()

        self.var_date2=StringVar()
        self.var_particular2=StringVar()
        self.var_partner3=StringVar()
        self.var_partner4=StringVar()


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
        title_lbl=Label(self.root,text="Current Account",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=130,width=1530,height=35)

        # Frame
        main_frame=Frame(bg_img,bd=2,bg='white')
        main_frame.place(x=5,y=40,width=1500,height=650)

        #left side label frame
        left_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Current Account Details',font=('times new roman',12,"bold"))
        left_frame.place(x=10,y=10,width=550,height=510)

        #### image for left frame
        img_left=Image.open(os.path.join("account_images","current_left.jpg"))
        img_left=img_left.resize((540, 120),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=3,y=0,width=540,height=120)

        ### current account  frame
        current_frame=LabelFrame(left_frame,bd=2,bg='white',relief=RIDGE,text='Current Account Enteries',font=('times new roman',12,"bold"))
        current_frame.place(x=5,y=125,width=540,height=360)

############## frame and labels for debit side ######################
        debit_frame=LabelFrame(current_frame,bd=2,bg='white',relief=RIDGE,text='Debit Side',font=('times new roman',12,"bold"))
        debit_frame.place(x=5,y=7,width=530,height=120)

        # Date  Labels
        date1_label=Label(debit_frame,text='Date:',font=('times new roman',13,"bold"),bg='white')
        date1_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        date1_entry=ttk.Entry(debit_frame,textvariable=self.var_date1,width=15,font=('times new roman',13,"bold"))
        date1_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)


        # particulars Labels
        particular1_label=Label(debit_frame,text='Particulars:',font=('times new roman',13,"bold"),bg='white')
        particular1_label.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        particular1_entry=ttk.Entry(debit_frame,textvariable=self.var_particular1,width=18,font=('times new roman',13,"bold"))
        particular1_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        # Partner A Labels
        partner1_label=Label(debit_frame,text='Partner A:',font=('times new roman',13,"bold"),bg='white')
        partner1_label.grid(row=2,column=0,padx=5,pady=10,sticky=W)

        partner1_entry=ttk.Entry(debit_frame,textvariable=self.var_partner1,width=15,font=('times new roman',13,"bold"))
        partner1_entry.grid(row=2,column=1,padx=5,pady=10,sticky=W)

        # partner B labels
        partner2_label=Label(debit_frame,text='Partner B:',font=('times new roman',13,"bold"),bg='white')
        partner2_label.grid(row=2,column=2,padx=5,pady=10,sticky=W)

        partner2_entry=ttk.Entry(debit_frame,textvariable=self.var_partner2,width=18,font=('times new roman',13,"bold"))
        partner2_entry.grid(row=2,column=3,padx=5,pady=10,sticky=W)


# ############## frame and labels for credit side ##############
        credit_frame=LabelFrame(current_frame,bd=2,bg='white',relief=RIDGE,text='Credit Side',font=('times new roman',12,"bold"))
        credit_frame.place(x=5,y=142,width=530,height=120)

        # Date  Labels
        date2_label=Label(credit_frame,text='Date:',font=('times new roman',13,"bold"),bg='white')
        date2_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        date2_entry=ttk.Entry(credit_frame,textvariable=self.var_date2,width=15,font=('times new roman',13,"bold"))
        date2_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)


        # particulars Labels
        particular2_label=Label(credit_frame,text='Particulars:',font=('times new roman',13,"bold"),bg='white')
        particular2_label.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        particular2_entry=ttk.Entry(credit_frame,textvariable=self.var_particular2,width=18,font=('times new roman',13,"bold"))
        particular2_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        # Partner A Labels
        partner3_label=Label(credit_frame,text='Partner A:',font=('times new roman',13,"bold"),bg='white')
        partner3_label.grid(row=2,column=0,padx=5,pady=10,sticky=W)

        partner3_entry=ttk.Entry(credit_frame,textvariable=self.var_partner3,width=15,font=('times new roman',13,"bold"))
        partner3_entry.grid(row=2,column=1,padx=5,pady=10,sticky=W)

        # partner B labels
        partner4_label=Label(credit_frame,text='Partner B:',font=('times new roman',13,"bold"),bg='white')
        partner4_label.grid(row=2,column=2,padx=5,pady=10,sticky=W)

        partner4_entry=ttk.Entry(credit_frame,textvariable=self.var_partner4,width=18,font=('times new roman',13,"bold"))
        partner4_entry.grid(row=2,column=3,padx=5,pady=10,sticky=W)

        ### frames for left side button
        btn_frame=Frame(current_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=5,y=280,width=528,height=50)

        ## save button
        save_btn=Button(btn_frame,text='Save',command=self.add_data,width=26,font=('times new roman',13,"bold"),bg='blue',fg='white')
        save_btn.grid(row=0,column=0,pady=7)

        #Reset Button
        reset_btn=Button(btn_frame,text='Reset',command=self.reset_data,width=26,font=('times new roman',13,"bold"),bg='blue',fg='white')
        reset_btn.grid(row=0,column=1,pady=7)
         
################################################################################################
################################################################################################
        #right side label frame
        right_frame=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,text='Current Account enteries Details',font=('times new roman',12,"bold"))
        right_frame.place(x=580,y=10,width=730,height=510)

        ### image for right frame
        img_right=Image.open(os.path.join("account_images","current_right.jpg"))
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
        search_combo['values']=("select","date1","date2")
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

        self.current_table=ttk.Treeview(table_frame,column=('date1',"particulars1",'partner1','partner2','date2',"particulars2",'partner3','partner4'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.current_table.xview)
        scroll_y.config(command=self.current_table.yview)


        # for table header
        self.current_table.heading('date1',text="Date")
        self.current_table.heading('particulars1',text="Particulars")
        self.current_table.heading('partner1',text="Partner A")
        self.current_table.heading('partner2',text="Partner B")


        self.current_table.heading('date2',text="Date")
        self.current_table.heading('particulars2',text="Particulars")
        self.current_table.heading('partner3',text="Partner A")
        self.current_table.heading('partner4',text="Partner B")

        self.current_table['show']='headings'

        #setting width for column
        self.current_table.column('date1',width=100)
        self.current_table.column('particulars1',width=250)
        self.current_table.column('partner1',width=100)
        self.current_table.column('partner2',width=200)

        self.current_table.column('date2',width=100)
        self.current_table.column('particulars2',width=250)
        self.current_table.column('partner3',width=100)
        self.current_table.column('partner4',width=200)

        #packing table
        self.current_table.pack(fill=BOTH,expand=1)

        self.fetch_data()

### function for save data ###########
    def add_data(self):
        try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="accounting_software")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into current values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_date1.get(),
                                                                        self.var_particular1.get(),
                                                                                self.var_partner1.get(),
                                                                                self.var_partner2.get(),

                                                                                self.var_date2.get(),
                                                                        self.var_particular2.get(),
                                                                                self.var_partner3.get(),
                                                                                self.var_partner4.get()
                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","current Account details has been added Sucessfully",parent=self.root)
                
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


###  fetch data from database ###########
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="accounting_software")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from current")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.current_table.delete(*self.current_table.get_children())
            for i in data:
                self.current_table.insert('',END,values=i)
            conn.commit()
        conn.close()

######    Reset data from form #################

    def reset_data(self):
        self.var_date1.set("")
        self.var_particular1.set("")
        self.var_partner1.set("")
        self.var_partner2.set("")

        self.var_date2.set("")
        self.var_particular2.set("")
        self.var_partner3.set("")
        self.var_partner4.set("")


######################   Search data ###################################


    def search_data(self):
        if self.var_searchtxt.get()=="" or self.var_search.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password="root",database="accounting_software")
                my_cursor=conn.cursor()
                query = f"SELECT * FROM current WHERE {self.var_search.get().lower()} LIKE '%{self.var_searchtxt.get().lower()}%'"
                my_cursor.execute(query)
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.current_table.delete(*self.current_table.get_children())
                    for i in rows:
                        self.current_table.insert("",END,values=i)
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
    obj=Current(root)
    root.mainloop()
        