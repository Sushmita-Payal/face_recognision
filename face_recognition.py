from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2 
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Easy Attendance System")

        bg_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="blue",fg="white")
        bg_lbl.place(x=0,y=0,width=1530,height=55)

        img_1 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\face2.jpg")
        img_1 = img_1.resize((650, 740))
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        first_label_1= Label(self.root, image=self.photoimg_1)
        first_label_1.place(x=0, y=55, width=650, height=740)


        img_2 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\facial-recognition.png")
        img_2 = img_2.resize((950, 740))
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        first_label_2= Label(self.root, image=self.photoimg_2)
        first_label_2.place(x=650, y=55, width=950, height=740)
        

        #button
        b11=Button(first_label_2,text="CLICK HERE FOR FACE RECOGNITION",cursor="hand2",command=self.recognition,font=("times new roman",18,"bold"),bg="blue",fg="white")
        b11.place(x=150,y=400,width=600,height=40)
    
    ############ attendacne ###################
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    ##### face recognition #######
    def recognition(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Payal@123",database="face_recognision")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT name FROM student WHERE Adm="+str(id))
                n=my_cursor.fetchone()
                #n="+".join(n)
                print(n)

                my_cursor.execute("SELECT roll_no FROM student WHERE Adm="+str(id))
                r=my_cursor.fetchone()
                #r="+".join(r)
                print(r)


                my_cursor.execute("SELECT dep FROM student WHERE Adm="+str(id))
                d=my_cursor.fetchone()
                #d="+".join(d)
                print(d)

                my_cursor.execute("SELECT Student_id FROM student WHERE Adm="+str(id))
                i=my_cursor.fetchone()
                #i="+".join(d)
                print(i)


                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)     

                coord=[x,y,w,h]
            return coord
        def recog(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recog(img,clf,faceCascade)
            cv2.imshow("Welcome to face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release
        cv2.destroyAllWindows()








if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()        