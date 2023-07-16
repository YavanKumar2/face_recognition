from PIL import Image,ImageTk
import cv2
import mysql.connector
from tkinter import *
from tkinter import ttk

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Take Attendance")
        take_attendance_btn=Button(text="Take Attendance",command=self.face_recog,width=14,font=("times new roman",13,"bold"),bg="darkblue",fg="white")
        take_attendance_btn.place(x=10,y=20)

        # ID_label=Label(parent=self.root,text="Enter StudentID:",font=("times new roman",13,"bold"))
        # ID_label.place(x=100,y=40)

        # ID_entry=ttk.Entry(width=20,font=("times new roman",13,"bold"))
        # ID_entry.place(x=65,y=40)

    def  face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Yavan252@@3",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student2 where ID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select RollNo from student2 where ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Branch from student2 where ID="+str(id))
                b=my_cursor.fetchone()
                b="+".join(b)
                

                if confidence>77:
                    cv2.putText(img,f"{confidence}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"RollNo:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Branch:{b}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"{confidence}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face recognition",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()


