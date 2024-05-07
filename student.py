from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Easy Attendance System")

        ####### Variables #####
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_adm=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_branch=StringVar()
        self.var_branch_code=StringVar()
        
        

        
        #collge image
        img = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\iitism.jpg")
        img = img.resize((550, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=550, height=130)
        

        
        img2 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\facedetector.jpeg")
        img2 = img2.resize((550, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=550, y=0, width=550, height=130)

        img3 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\maingate.jpeg")
        img3 = img3.resize((550, 130))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        first_label = Label(self.root, image=self.photoimg3)
        first_label.place(x=1100, y=0, width=480, height=130)

        #background image
        img4 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\bg.jpeg")
        img4 = img4.resize((1530, 710))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        #heading
        bg_lbl=Label(bg_img,text="Student Management System",font=("times new roman",35,"bold"),bg="blue",fg="white")
        bg_lbl.place(x=0,y=0,width=1530,height=50)
        
        #main frame
        frame= Frame(bg_img,bd=2)
        frame.place(x=50,y=80,width=1430,height=550)

        #left label frame
        left_frame= LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12))
        left_frame.place(x=10,y=10,width=720,height=580)
        
        img_left = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\student_management.jpeg")
        img_left = img_left.resize((550, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_label_left= Label(left_frame, image=self.photoimg_left)
        first_label_left.place(x=5, y=0, width=700, height=130)
         
         #current courses
        current_frame= LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Courses details",font=("times new roman",12))
        current_frame.place(x=5,y=135,width=710,height=150)
        
        #Department
        dep_label=Label(current_frame,text="Department",font=("times new roman",12),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_frame,textvariable=self.var_dep,font=("times new roman",12),state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","Electronics","Mechanical","Mining","Petroleum","Environmental","Chemical","Engneering Physics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Courses
        course_label=Label(current_frame,text="Course",font=("times new roman",12),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_frame,textvariable=self.var_course,font=("times new roman",12),state="readonly")
        course_combo["values"]=("Select Course","Computer Science","Electronics","Mechanical","Mining","Petroleum","Environmental","Chemical","Engneering Physics")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_frame,text="Year",font=("times new roman",12),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12),state="read only")
        year_combo["values"]=("Select Year","2023-2024","2024-2025","2025-2026","2026-2027","2027-2028")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

         #Semester
        sem_label=Label(current_frame,text="Semester",font=("times new roman",12),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_frame,textvariable=self.var_sem,font=("times new roman",12),state="read only")
        sem_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student details
        class_frame= LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student details",font=("times new roman",12))
        class_frame.place(x=5,y=250,width=710,height=300)

        #admission no
        studentId_label=Label(class_frame,text="Admission no:",font=("times new roman",12),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_frame,width=20,textvariable=self.var_adm,font=("times new roman", 12))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name
        name_label=Label(class_frame,text="Student name:",font=("times new roman",12),bg="white")
        name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(class_frame,width=20,textvariable=self.var_name,font=("times new roman", 12))
        name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #roll no
        roll_label=Label(class_frame,text="Roll no: ",font=("times new roman",12),bg="white")
        roll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(class_frame,width=20,textvariable=self.var_roll,font=("times new roman", 12))
        roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #student email id 
        email_label=Label(class_frame,text="Student Email Id: ",font=("times new roman",12),bg="white")
        email_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_frame,width=20,textvariable=self.var_email,font=("times new roman", 12))
        email_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #student phone no
        phone_label=Label(class_frame,text="Student phone no: ",font=("times new roman",12),bg="white")
        phone_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_frame,width=20,textvariable=self.var_phone,font=("times new roman", 12))
        phone_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Date of birth 
        dob_label=Label(class_frame,text="Date of Birth: ",font=("times new roman",12),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_frame,width=20,textvariable=self.var_dob,font=("times new roman", 12))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #branch
        branch_label=Label(class_frame,text="Branch: ",font=("times new roman",12),bg="white")
        branch_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        branch_entry=ttk.Entry(class_frame,width=20,textvariable=self.var_branch,font=("times new roman", 12))
        branch_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #branch code
        bc_label=Label(class_frame,text="Branch Code: ",font=("times new roman",12),bg="white")
        bc_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        bc_entry=ttk.Entry(class_frame,width=20,textvariable=self.var_branch_code,font=("times new roman", 12))
        bc_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #radio Buttons
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="Take Photo",value="Yes")
        radiobutton1.grid(row=4,column=1)
        
     
        radiobutton2=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="No Photo",value="No")
        radiobutton2.grid(row=4,column=3)

        
        #buttons frame
        btn_frame=Frame(class_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=170,width=683,height=40)

        save = Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",13,"bold"), bg="white",fg="black",width=16)
        save.grid(row=0,column=0)

        update = Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",13,"bold"), bg="white",fg="black",width=16)
        update.grid(row=0,column=1)

        delete = Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"), bg="white",fg="black",width=16)
        delete.grid(row=0,column=2)

        reset = Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"), bg="white",fg="black",width=16)
        reset.grid(row=0,column=3)

        
        btn_frame1=Frame(class_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=200,width=683,height=35)

        Take_photo = Button(btn_frame1,text="Take Photo",command=self.generate_dataset,font=("times new roman",13,"bold"), bg="white",fg="black",width=33)
        Take_photo.grid(row=0,column=0)

        update_photo = Button(btn_frame1,text="Update Photo",font=("times new roman",13,"bold"), bg="white",fg="black",width=33)
        update_photo.grid(row=0,column=1)


        #right label frame
        right_frame= LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12))
        right_frame.place(x=753,y=10,width=660,height=580)

        img_right = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\photos.jpeg")
        img_right = img_right.resize((550, 130))
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        first_label_right= Label(right_frame, image=self.photoimg_right)
        first_label_right.place(x=5, y=0, width=650, height=130)

        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12))
        search_frame.place(x=5,y=135,width=650,height=70)

        search_label=Label(search_frame,text="Search by:",font=("times new roman",12),bg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)


        search_combo=ttk.Combobox(search_frame,font=("times new roman",12),state="read only",width=12)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman", 12))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        search_btn = Button(search_frame,text="Search",font=("times new roman",12,"bold"), bg="white",fg="black",width=14)
        search_btn.grid(row=0,column=3,padx=4)

        ShowAll = Button(search_frame,text="Show All",font=("times new roman",12,"bold"), bg="white",fg="black",width=14)
        ShowAll.grid(row=0,column=4,padx=4)

        #-----table frame---------
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=650,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","Course","year","sem","Adm","name","Roll","Email","Phone_no","Dob","Branch","Branch_code","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("Adm",text="Admission No")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("Roll",text="Roll_No")
        self.student_table.heading("Email",text="Email Id")
        self.student_table.heading("Phone_no",text="Phone No")
        self.student_table.heading("Dob",text="Date of Birth")
        self.student_table.heading("Branch",text="Branch")
        self.student_table.heading("Branch_code",text="Branch Code")
        self.student_table.heading("photo",text="Photo_Sample_Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("Adm",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone_no",width=100)
        self.student_table.column("Dob",width=100)
        self.student_table.column("Branch",width=100)
        self.student_table.column("Branch_code",width=100)
        self.student_table.column("photo",width=130)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    ##### function decreation ##########
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_adm.get()=="":
             messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Payal@123",database="face_recognision")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_sem.get(),
                            self.var_adm.get(),
                            self.var_name.get(),
                            self.var_roll.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_dob.get(),
                            self.var_branch.get(),
                            self.var_branch_code.get(),
                            self.var_radio1.get()
                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   


    ### fetch data ####

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Payal@123",database="face_recognision")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    


    ######### get cursor ###########
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_adm.set(data[4]),
        self.var_name.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_email.set(data[7]), 
        self.var_phone.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_branch.set(data[10]),
        self.var_branch_code.set(data[11]),
        self.var_radio1.set(data[12])

    #update function   

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_adm.get()=="":
             messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Payal@123",database="face_recognision")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET dep=%s, course=%s, year=%s, semester=%s, name=%s, roll_no=%s , email=%s, phone_no=%s, dob=%s, branch=%s, branch_code=%s, photo_sample=%s WHERE Adm=%s",(
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_sem.get(),
                                                self.var_name.get(),
                                                self.var_roll.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_dob.get(),
                                                self.var_branch.get(),
                                                self.var_branch_code.get(),
                                                self.var_radio1.get(),
                                                self.var_adm.get()                                
                                            ))

                else:
                    if not Update:
                        return  
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)         


    #### delete function ####

    def delete_data(self):
        if self.var_adm.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Payal@123",database="face_recognision")
                    my_cursor=conn.cursor()
                    sql="delete from student where Adm=%s"
                    val=(self.var_adm.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully delted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 


    ### reset ####

    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_name.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_dob.set(""),
        self.var_branch.set(""),
        self.var_branch_code.set(""),
        self.var_radio1.set(""),
        self.var_adm.set("")

    #### Generate data set or take photo samples ######

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_adm.get()=="":
             messagebox.showerror("Error","All Fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Payal@123",database="face_recognision")
                my_cursor=conn.cursor()  
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("UPDATE student SET dep=%s, course=%s, year=%s,semester=%s,name=%s,roll_no=%s,email=%s,phone_no=%s,dob=%s,branch=%s,branch_code=%s,photo_sample=%s WHERE Adm=%s",(
                                                self.var_dep.get(),
                                                self.var_course.get(),
                                                self.var_year.get(),
                                                self.var_sem.get(),
                                                self.var_name.get(),
                                                self.var_roll.get(),
                                                self.var_email.get(),
                                                self.var_phone.get(),
                                                self.var_dob.get(),
                                                self.var_branch.get(),
                                                self.var_branch_code.get(),
                                                self.var_radio1.get(),
                                                self.var_adm.get()==id+1                                
                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 

                #### load predifined data on face frontals from opencv ####

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor =1.3
                    #Minimum Neighbor=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w] 
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   






                     
                 






        



        #----Search System-----







if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
