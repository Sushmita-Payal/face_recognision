from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np


class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Easy Attendance System")
    
        bg_lbl=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="blue",fg="white")
        bg_lbl.place(x=0,y=0,width=1530,height=55)

        img_top = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\th.jpeg")
        img_top = img_top.resize((1530, 325))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        first_label_top= Label(self.root, image=self.photoimg_top)
        first_label_top.place(x=0, y=55, width=1530, height=328)
        
        #button
        b11=Button(self.root,text="TRAIN DATA",cursor="hand2",command=self.train_classifier,font=("times new roman",30,"bold"),bg="blue",fg="white")
        b11.place(x=0,y=380,width=1530,height=60)


        img_bottom = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\face1.jpg")
        img_bottom = img_bottom.resize((1530, 325))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        first_label_bottom = Label(self.root, image=self.photoimg_bottom)
        first_label_bottom.place(x=0, y=440, width=1530, height=325)
    
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        ###### Train the classifier and save #######
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed")


        
if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()        