#!/usr/bin/env python
# coding: utf-8

# In[12]:


from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        #self.val=StringVar()
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        
        
        img=Image.open(r"C:\Users\hp\Desktop\image\bg.jpeg")
        img=img.resize((1390,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1390,height=750) 
        
        
        title_lbl=Label(bg_img,text="SMART ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=0,y=0,width=1390,height=60)
        
        img1=Image.open(r"C:\Users\hp\Desktop\image\s1.jpeg")
        img1=img1.resize((220,220),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        b1=Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        
        
        img2=Image.open(r"C:\Users\hp\Desktop\image\att.jpeg")
        img2=img2.resize((220,220),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        b2=Button(bg_img,image=self.photoimg2,cursor="hand2")
        b2.place(x=600,y=100,width=220,height=220)
        
        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        b2_1.place(x=600,y=300,width=220,height=40)
        
        
        
        img3=Image.open(r"C:\Users\hp\Desktop\image\att2.jpeg")
        img3=img3.resize((220,220),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b3=Button(bg_img,image=self.photoimg3,cursor="hand2")
        b3.place(x=1000,y=100,width=220,height=220)
        
        b3_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        b3_1.place(x=1000,y=300,width=220,height=40)
        
        
        
        img4=Image.open(r"C:\Users\hp\Desktop\image\td.jpeg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b4=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b4.place(x=200,y=400,width=220,height=220)
        
        b4_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        b4_1.place(x=200,y=600,width=220,height=40)
        
        
        
        img5=Image.open(r"C:\Users\hp\Desktop\image\ph.jpeg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b5=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b5.place(x=600,y=400,width=220,height=220)
        
        b5_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        b5_1.place(x=600,y=600,width=220,height=40)
        
        
        
        img6=Image.open(r"C:\Users\hp\Desktop\image\exit.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b6=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b6.place(x=1000,y=400,width=220,height=220)
        
        b6_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="yellow")
        b6_1.place(x=1000,y=600,width=220,height=40)
        
        
        
        
        #===========functions buttons==========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
        
       
    
    
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        
       # ==========================variables=========================
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
        
        img=Image.open(r"C:\Users\hp\Desktop\image\bg.jpeg")
        img=img.resize((1390,790),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1390,height=750) 
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=0,y=0,width=1390,height=60)
        
        
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=80,width=1320,height=630)
        
        
        # left
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=20,y=10,width=630,height=600)
        
        #curent course
        current_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Current Course information",font=("times new roman",12,"bold"))
        current_frame.place(x=30,y=50,width=610,height=120)
        
        
        #department
        
        dep_label=Label(current_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select department","CSE","Mechanical","Civil","Agriculture")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=3,pady=10)
        
        #course
        
        course_label=Label(current_frame,text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10)
        
        course_combo=ttk.Combobox(current_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","Btech","Mtech","MBA","BA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=3,pady=10,sticky=W)
        
        
        #year
        
        year_label=Label(current_frame,text="Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10)
        
        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=3,pady=10,sticky=W)
        
        
        #semester
        semester_label=Label(current_frame,text="Semester",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=10)
        
        semester_combo=ttk.Combobox(current_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","First","Second")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=3,pady=10,sticky=W)
        
        
        #class student info
        class_student_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=30,y=175,width=610,height=420)
        
        #student id
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"))
        studentId_label.grid(row=0,column=0,padx=10)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"))
        studentName_label.grid(row=0,column=2,padx=10)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=18,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"))
        class_div_label.grid(row=1,column=0,padx=10)
        
        #class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        class_div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        class_div_combo["values"]=("A","B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #roll no
        roll_no_label=Label(class_student_frame,text="Roll Number:",font=("times new roman",12,"bold"))
        roll_no_label.grid(row=1,column=2,padx=10)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=18,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        #Gender
        
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=10)
        
        #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        
        #dob
        
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column=2,padx=10)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=18,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        #email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"))
        email_label.grid(row=4,column=2,padx=10)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=18,font=("times new roman",12,"bold"))
        email_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        
        #phone
        phone_label=Label(class_student_frame,text="Phone:",font=("times new roman",12,"bold"))
        phone_label.grid(row=3,column=2,padx=10)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=18,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        #teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"))
        teacher_label.grid(row=3,column=0,padx=10)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"))
        address_label.grid(row=4,column=0,padx=10)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        
       # radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
    
        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
                                  
        radiobtn2.grid(row=5,column=1)
    
        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=240,width=600,height=35)
    
    
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        save_btn.grid(row=0,column=0,padx=2)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        update_btn.grid(row=0,column=1,padx=2)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        delete_btn.grid(row=0,column=2,padx=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        reset_btn.grid(row=0,column=3,padx=2)
        
        
        btn1_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=5,y=280,width=600,height=35)
    
        
        take_photo_btn=Button(btn1_frame,text="Take Photo Sample",width=32,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        take_photo_btn.grid(row=1,column=0)
        
        update_photo_btn=Button(btn1_frame,text="Update Photo Sample",width=32,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        update_photo_btn.grid(row=1,column=1,padx=2)
        
        
        
        
        # Right
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=660,y=10,width=630,height=600)
        
        #======search system========
        
                
        
        search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=20,width=600,height=80)
        
        
        search_label=Label(search_frame,text="Serach By:",font=("times new roman",12,"bold"),bg="yellow",fg="black")
        search_label.grid(row=0,column=0,padx=10)
        
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=8)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        search_btn.grid(row=0,column=3,padx=2)
        
        showAll_btn=Button(search_frame,text="show All",width=10,font=("times new roman",12,"bold"),bg="yellow",fg="black")
        showAll_btn.grid(row=0,column=4,padx=2)
        
        #====tablle frame=====
        table_frame=Frame(Right_frame,bd=3,relief=RIDGE)
        table_frame.place(x=10,y=120,width=600,height=400)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("roll",text="Roll_No")
        
        self.student_table["show"]="headings"
        
        
        self.student_table.column("dep",width=80)
        self.student_table.column("course",width=80)
        self.student_table.column("year",width=80)
        self.student_table.column("sem",width=80)
        self.student_table.column("id",width=80)
        self.student_table.column("name",width=80)
        self.student_table.column("div",width=80)
        self.student_table.column("dob",width=80)
        self.student_table.column("email",width=80)
        self.student_table.column("phone",width=80)
        self.student_table.column("address",width=80)
        self.student_table.column("teacher",width=80)
        self.student_table.column("photo",width=80)
        self.student_table.column("gender",width=80)
        self.student_table.column("roll",width=80)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
 #===========function declaration====================  
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","all Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Arun@2000",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_id.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
                
           
            ))
         
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student detail has been added successfully",parent=self.root)
            except Exception as es:
                    messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                
        
        
      #===================fetch data=====================  
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Arun@2000",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
            
            
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                    
            conn.commit()
        conn.close   
            

        
       #===================get cursor====================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
        
    #Update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","all Fields are required",parent=self.root)
    
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Arun@2000",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                    
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                    
                    
                     
                ))
                    
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
    
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                
                
                #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Arun@2000",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
                #reset
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(data[7]),
        self.var_gender.set("Male"),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
        
    #take photo sample    
        
        
                
                   
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


# In[ ]:




