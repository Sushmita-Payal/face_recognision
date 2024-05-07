from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Easy Attendance System")

        # ============variables=============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #first image
        img = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\iitism.jpg")
        img = img.resize((800, 200))
        self.photoimg = ImageTk.PhotoImage(img)

        first_label = Label(self.root, image=self.photoimg)
        first_label.place(x=0, y=0, width=800, height=200)
        
        #second image
        img2 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\facedetector.jpeg")
        img2 = img2.resize((800, 200))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_label = Label(self.root, image=self.photoimg2)
        first_label.place(x=800, y=0, width=800, height=200)

        #background image
        img4 = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\bg.jpeg")
        img4 = img4.resize((1530, 710))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=200, width=1530, height=710)

        #heading
        bg_lbl=Label(bg_img,text="Attendance Management System",font=("times new roman",35,"bold"),bg="blue",fg="white")
        bg_lbl.place(x=0,y=0,width=1530,height=50)
        
        #main frame
        frame= Frame(bg_img,bd=2)
        frame.place(x=50,y=80,width=1430,height=550)

        #left label frame
        left_frame= LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12))
        left_frame.place(x=10,y=10,width=720,height=580)

        img_left = Image.open(r"C:\Users\ASUS\Desktop\Easy Attendance\New folder\student_management.jpeg")
        img_left = img_left.resize((550, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        first_label_left= Label(left_frame, image=self.photoimg_left)
        first_label_left.place(x=5, y=0, width=700, height=130)

        left_inside_frame= Frame(left_frame,bd=2,relief=RIDGE)
        left_inside_frame.place(x=0,y=180,width=720,height=370)

        #Label and entry
        #attendance id
        attendance_Id_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",12),bg="white")
        attendance_Id_label.grid(row=0,column=0,padx=10,sticky=W)

        attendance_Id_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman", 12))
        attendance_Id_entry.grid(row=0,column=1,padx=10,sticky=W)

        #Name
        rollLabel=Label(left_inside_frame,text="Roll:",bg="white",font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=3,pady=8)

        #date
        nameLabel=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 11 bold")
        nameLabel.grid(row=1,column=0)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_name.grid(row=1,column=1,pady=8)

        #department
        depLabel=Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        depLabel.grid(row=1,column=2)

        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=3,pady=8)

        #time
        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=2,column=0)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1,pady=8)

        # date
        dateLabel=Label(left_inside_frame,text="Date:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=2)

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=3,pady=8)

        # attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance status",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=683,height=40)

        save = Button(btn_frame,text="Import csv",command=self.importCsv,font=("times new roman",13,"bold"), bg="white",fg="black",width=16)
        save.grid(row=0,column=0)

        update = Button(btn_frame,text="Export csv",command=self.exportCsv,font=("times new roman",13,"bold"), bg="white",fg="black",width=16)
        update.grid(row=0,column=1)

        delete = Button(btn_frame,text="Update",font=("times new roman",13,"bold"), bg="white",fg="black",width=16)
        delete.grid(row=0,column=2)

        reset = Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"), bg="white",fg="black",width=16)
        reset.grid(row=0,column=3)


        #right label frame
        Right_frame= LabelFrame(frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12))
        Right_frame.place(x=753,y=10,width=660,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=683,height=455)

        ###########scroll bar table#########
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

########## fetch data #############
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)       

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


            


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()