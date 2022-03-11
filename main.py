from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")


        img=Image.open(r"C:\Users\Shreeyash Pandey\Desktop\Face_Recognition_System\photos\School-Attendance-Systems.jpg")
        img=img.resize((500,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=150,y=50,width=1000,height=130)

        tittle_label=Label(self.root,text="Face Recognition Attendace System",font=("times new roman",35,"bold"),bg="white",fg="red")
        tittle_label.place(x=15,y=150,width=1530,height=45)

        b1=Button(self.root,text="Student Details",command=self.student_details,font=("times new roman",15,"bold"),bg="dark blue",fg="black")
        b1.place(x=300,y=200,width=150,height=150)

        b1_1= Button(self.root,text="Face Detector",font=("times new roman",15,"bold"),bg="dark blue",fg="black")
        b1_1.place(x=300, y=400, width=150, height=150)

        b1_2 = Button(self.root, text="Attendance", font=("times new roman", 15, "bold"), bg="dark blue", fg="black")
        b1_2.place(x=500, y=400, width=150, height=150)

        b1_3 = Button(self.root, text="Trainer", font=("times new roman", 15, "bold"), bg="dark blue", fg="black")
        b1_3.place(x=500, y=200, width=150, height=150)

        b1_4 = Button(self.root, text="Photos", font=("times new roman", 15, "bold"), bg="dark blue", fg="black")
        b1_4.place(x=700, y=200, width=150, height=150)

        b1_5 = Button(self.root, text="Exit", font=("times new roman", 15, "bold"), bg="dark blue", fg="black")
        b1_5.place(x=700, y=400, width=150, height=150)

        #function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)



if __name__=="__main__":    
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()