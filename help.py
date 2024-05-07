from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Easy Attendance System")

        bg_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="blue",fg="blue")
        bg_lbl.place(x=0,y=0,width=1530,height=55)

        img_top = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\th.jpeg")
        img_top = img_top.resize((1530, 720))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label_top= Label(self.root, image=self.photoimg_top)
        first_label_top.place(x=0, y=55, width=1530, height=720)

        dev_label=Label(first_label_top,text="Email:20je0288@ece.iitism.ac.in",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=500,y=200)
        
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
