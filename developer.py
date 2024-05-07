from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Easy Attendance System")

        bg_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="blue",fg="blue")
        bg_lbl.place(x=0,y=0,width=1530,height=55)

        img_top = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\th.jpeg")
        img_top = img_top.resize((1530, 720))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label_top= Label(self.root, image=self.photoimg_top)
        first_label_top.place(x=0, y=55, width=1530, height=720)
        
        # frame
        frame= Frame(first_label_top,bd=2,bg="white")
        frame.place(x=1000,y=0,width=500,height=550)

        img_top1 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\th.jpeg")
        img_top1 = img_top1.resize((1530, 720))
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        first_label_top= Label(frame, image=self.photoimg_top1)
        first_label_top.place(x=300, y=0, width=200, height=200)

        #Developer info
        dev_label=Label(frame,text="Hello from Sushmita,Palash,Ajinkya",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(frame,text="We are full stack developers",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        img3 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\maingate.jpeg")
        img3 = img3.resize((500, 390),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        first_label = Label(frame, image=self.photoimg3)
        first_label.place(x=0, y=210, width=480, height=390)


        


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
