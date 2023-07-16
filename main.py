from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from student import Student
import os
import cv2
import numpy as np


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # first image
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
        img3=Image.open(r'C:\Users\yavan\Desktop\face reco\image\blueBG.jpg')
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM                             ",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # student button
        img4=Image.open(r'C:\Users\yavan\Desktop\face reco\image\studentDetail.jpg')
        img4=img4.resize((120,120),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=300,y=100,width=120,height=120)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=300,y=200,width=120,height=40)

        #Attendance details
        img5=Image.open(r'C:\Users\yavan\Desktop\face reco\image\Attendance.jpg')
        img5=img5.resize((120,120),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=600,y=100,width=120,height=120)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=600,y=200,width=120,height=40)

        #Train Data
        img6=Image.open(r'C:\Users\yavan\Desktop\face reco\image\TrainData.png')
        img6=img6.resize((120,120),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.train_classifier)
        b1.place(x=900,y=100,width=120,height=120)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_classifier,font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=900,y=200,width=120,height=40)

        #Photos
        img7=Image.open(r'C:\Users\yavan\Desktop\face reco\image\photos.jpg')
        img7=img7.resize((120,120),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.open_img)
        b1.place(x=300,y=300,width=120,height=120)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=300,y=400,width=120,height=40)

        #Help
        img8=Image.open(r'C:\Users\yavan\Desktop\face reco\image\help.jpg')
        img8=img8.resize((120,120),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=600,y=300,width=120,height=120)

        b1_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=600,y=400,width=120,height=40)

        #Exit
        img9=Image.open(r'C:\Users\yavan\Desktop\face reco\image\Exit.jpg')
        img9=img9.resize((120,120),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=900,y=300,width=120,height=120)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",10,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=900,y=400,width=120,height=40)

    def open_img(self):
        os.startfile("data")

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
    
        ids=np.array(ids)

        #Train classifier and save

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Training Complete",parent=self.root)






if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

    
