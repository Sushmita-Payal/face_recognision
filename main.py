from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from student import Student
import os
from time import strftime
from datetime import datetime
from train import train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Easy_Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Easy Attendance System")

        
        #college image
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

        #backgroung image
        img4 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\bg.jpeg")
        img4 = img4.resize((1530, 710))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        #heading
        bg_lbl=Label(bg_img,text="Easy Attendance",font=("times new roman",35,"bold"),bg="blue",fg="white")
        bg_lbl.place(x=0,y=0,width=1530,height=50)
        
        #======== time =============
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(bg_lbl,font = ('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #student button
        img5 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\student4.jpeg")
        img5 = img5.resize((220, 220))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.open_student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b11=Button(bg_img,text="Student Details",command=self.open_student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b11.place(x=200,y=300,width=220,height=40)

        #detect face button
        img6 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\face2.jpg")
        img6 = img6.resize((220, 220))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.open_face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b11=Button(bg_img,text="Face Detector",cursor="hand2",command=self.open_face_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b11.place(x=500,y=300,width=220,height=40)

        #attendance face button
        img7 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\attendance.jpeg")
        img7 = img7.resize((220, 220))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b11=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b11.place(x=800,y=300,width=220,height=40)
        
        # help face button
        img20 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\face1.jpg") #new photo tobe inserted
        img20 = img20.resize((220, 220))
        self.photoimg20 = ImageTk.PhotoImage(img20)

        b1=Button(bg_img,image=self.photoimg20,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b11=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b11.place(x=1100,y=300,width=220,height=40)
        

        #train data button
        img8 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\face1.jpg")
        img8 = img8.resize((220, 220))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.open_train_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b11=Button(bg_img,text="Train Data",cursor="hand2",command=self.open_train_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b11.place(x=1100,y=300,width=220,height=40)
        
        #photos face button
        img9 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\photos.jpeg")
        img9 = img9.resize((220, 220))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=370,width=220,height=220)

        b11=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b11.place(x=500,y=570,width=220,height=40)


        # developer face button
        img10 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\help.jpeg")
        img10 = img10.resize((220, 220))
        self.photoimg10= ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=370,width=220,height=220)

        b11=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="blue",fg="white")
        b11.place(x=800,y=570,width=220,height=40)

        #logoutbutton == Exit face button
        img11 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\logout.jpg")
        img11 = img11.resize((100, 100))
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1400,y=510,width=100,height=100)

        b11=Button(bg_img,text="Logout",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="white",fg="red")
        b11.place(x=1400,y=600,width=100,height=30)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","are you sure to exit this project?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()

    #========== FUNCTION BUTTONS =========

    # function to open student manangement over clicking in home
    def open_student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    #function to open train data upon clicking
    def open_train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)    

    def open_face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)   

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)  

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)   
        


        
        
        

        

        
if __name__ == "__main__":
    root = Tk()
    obj = Easy_Attendance(root)
    root.mainloop()
