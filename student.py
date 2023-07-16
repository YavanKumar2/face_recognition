from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student details")


        #variables
        self.var_ID=StringVar()
        self.var_RollNo=StringVar()
        self.var_Name=StringVar()
        self.var_Year=StringVar()
        self.var_Branch=StringVar()
        self.var_Date=StringVar()
        self.var_Time=StringVar()
        self.var_PhoneNo=StringVar()
        # self.var_Photo=StringVar()


        img=Image.open(r'C:\Users\yavan\Desktop\face reco\image\kmitLogo.jpg')
        img=img.resize((450,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=450,height=130)

        # second image
        img1=Image.open(r'C:\Users\yavan\Desktop\face reco\image\FR-Scan-Featured-01-scaled.jpeg')
        img1=img1.resize((450,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=450,y=0,width=450,height=130)

        # third image 

        img2=Image.open(r'C:\Users\yavan\Desktop\face reco\image\kmit.jpeg')
        img2=img2.resize((450,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=900,y=0,width=450,height=130)

        #bg image
        img4=Image.open(r'C:\Users\yavan\Desktop\face reco\image\blueBG.jpg')
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM                             ",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=45,width=1500,height=650)

        # left label frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font="times")
        Left_frame.place(x=10,y=10,width=660,height=440)

        

        current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Course Details",font="times")
        current_course_frame.place(x=10,y=20,width=630,height=100)

        #Department
        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Branch,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","AIML-A","AIML-B","AIML-C","CSD","CSE-A","CSE-B","CSE-C","CSE-D","CSE-E","CSE-F","CSE-G","IT-A","IT-B","IT-C",)
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)


        #Year
        year_label=Label(current_course_frame,text="Year:",font=("times new roman",12,"bold"))
        year_label.grid(row=0,column=2,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","I","II","III","IV")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2,pady=10)

        #Student Info
        Student_Info_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Student Info",font="times")
        Student_Info_frame.place(x=10,y=130,width=630,height=270)

        #Roll No.
        studentId_label=Label(Student_Info_frame,text="Roll No:",font=("times new roman",13,"bold"))
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(Student_Info_frame,textvariable=self.var_RollNo,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #Student Name
        studentName_label=Label(Student_Info_frame,text="Name:",font=("times new roman",13,"bold"))
        studentName_label.grid(row=0,column=2,padx=10,sticky=W)

        studentName_entry=ttk.Entry(Student_Info_frame,textvariable=self.var_Name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)

        #Phone No.
        studentNo_label=Label(Student_Info_frame,text="Phone No:",font=("times new roman",13,"bold"))
        studentNo_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        studentNo_entry=ttk.Entry(Student_Info_frame,textvariable=self.var_PhoneNo,width=20,font=("times new roman",13,"bold"))
        studentNo_entry.grid(row=1,column=1,padx=10,pady=20,sticky=W)

        ID_label=Label(Student_Info_frame,text="Student ID:",font=("times new roman",13,"bold"))
        ID_label.grid(row=1,column=2,padx=7,pady=10,sticky=W)

        ID_entry=ttk.Entry(Student_Info_frame,textvariable=self.var_ID,width=20,font=("times new roman",13,"bold"))
        ID_entry.grid(row=1,column=3,padx=7,pady=20,sticky=W)

        #radio buttons
        self.var_radio=StringVar()
        radiobtn1=ttk.Radiobutton(Student_Info_frame,variable=self.var_radio,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=2,column=0)

        
        radiobtn2=ttk.Radiobutton(Student_Info_frame,variable=self.var_radio,text="No Photo Sample",value="No")
        radiobtn2.grid(row=2,column=1)

        #buttons frame
        btn_frame=LabelFrame(Student_Info_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=130,width=600,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=14,command=self.update_data,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=LabelFrame(Student_Info_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=10,y=175,width=600,height=35)

        Take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=30,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        Take_photo_btn.grid(row=1,column=0)

        Update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=30,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        Update_photo_btn.grid(row=1,column=1)








        # Right label frame 
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font="times")
        Right_frame.place(x=680,y=10,width=580,height=440)


        Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search",font="times")
        Search_frame.place(x=10,y=20,width=550,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,width=10,font=("times new roman",13,"bold"),state="readonly")
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,sticky=W)

        Search_btn=Button(Search_frame,text="Search",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        Search_btn.grid(row=0,column=3,padx=2)

        ShowAll_btn=Button(Search_frame,text="Show All",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        ShowAll_btn.grid(row=0,column=4)

        table_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,font="times")
        table_frame.place(x=10,y=100,width=550,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("ID","Roll No","Name","Year","Branch","Phone No","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Roll No",text="Roll No")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Branch",text="Branch")
        #self.student_table.heading("Date",text="Date")
        #self.student_table.heading("Time",text="Time")
        self.student_table.heading("Phone No",text="Phone No")
        self.student_table.heading("Photo",text="Photo Sample")
        self.student_table["show"]="headings"

        # self.student_table.column("Roll No",width=100)



        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #function declaration

    def add_data(self):
        if self.var_Branch.get()=="Select Department" or self.var_Name.get()=="" or self.var_RollNo.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Yavan252@@3",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student2 values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_ID.get(),
                                                                                                self.var_RollNo.get(),
                                                                                                self.var_Name.get(),
                                                                                                self.var_Year.get(),
                                                                                                self.var_Branch.get(),
                                                                                            
                                                                                                self.var_PhoneNo.get(),
                                                                                                self.var_radio.get()



                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Yavan252@@3",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student2")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_ID.set(data[0])
        self.var_RollNo.set(data[1])
        self.var_Name.set(data[2])
        self.var_Year.set(data[3])
        self.var_Branch.set(data[4])
        self.var_PhoneNo.set(data[5])
        self.var_radio.set(data[6])

    def update_data(self):
        if self.var_Branch.get()=="Select Department" or self.var_Name.get()=="" or self.var_RollNo.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if(Update>0):
                    conn=mysql.connector.connect(host="localhost",username="root",password="Yavan252@@3",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student2 set RollNo=%s,Name=%s,Year=%s,Branch=%s,PhoneNo=%s,PhotoSample=%s where ID=%s",(

                                                                                                                                    self.var_RollNo.get(),
                                                                                                                                    self.var_Name.get(),
                                                                                                                                    self.var_Year.get(),
                                                                                                                                    self.var_Branch.get(),
                                                                                                                                    self.var_PhoneNo.get(),
                                                                                                                                    self.var_radio.get(),
                                                                                                                                    self.var_ID.get()
                                                                                                                                ))
                else:
                    if  not Update:
                        return
                messagebox.showinfo("Success","Student Details Successfully Update",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Yavan252@@3",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student2 where ID=%s"
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                messagebox.showinfo("Delete","Successfull Deleted",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_Branch.set("Select Department")
        self.var_Year.set("Select Year")
        self.var_RollNo.set("")
        self.var_Name.set("")
        self.var_PhoneNo.set("")
        self.var_ID.set("")
        self.var_radio.set("")

    def generate_dataset(self):
        if self.var_Branch.get()=="Select Department" or self.var_Name.get()=="" or self.var_RollNo.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Yavan252@@3",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student2")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student2 set RollNo=%s,Name=%s,Year=%s,Branch=%s,PhoneNo=%s,PhotoSample=%s where ID=%s",(

                                                                                                                                    self.var_RollNo.get(),
                                                                                                                                    self.var_Name.get(),
                                                                                                                                    self.var_Year.get(),
                                                                                                                                    self.var_Branch.get(),
                                                                                                                                    self.var_PhoneNo.get(),
                                                                                                                                    self.var_radio.get(),
                                                                                                                                    self.var_ID.get()==id+1
                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbour=5

                    for (x,y,w,h) in faces:
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

                    if cv2.waitKey(1)==13 or int(img_id)==25:
                                
                        break
                                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Success","Generating Datasets Completed!",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                



       







if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()