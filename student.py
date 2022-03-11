from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

from detect import faceDetection

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management")

        self.var_dep=StringVar()
        self.var_year = StringVar()
        self.var_course= StringVar()
        self.var_semester = StringVar()
        self.var_id=StringVar()
        self.var_name= StringVar()
        self.var_rollno = StringVar()
        self.var_class_div=StringVar()


        tittle_label = Label(self.root, text="Student Management System", font=("times new roman", 35, "bold"),
                             bg="black", fg="dark blue")
        tittle_label.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=600,height=500)

        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"))
        right_frame.place(x=620, y=10, width=600, height=500)

        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current Course Details",
                                font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=10, width=580, height=150)

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox (current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computers","IT","Civil","Machanical","Chamical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2,padx=10)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course ,font=("times new roman", 12, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)

        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0,padx=10)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year ,font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2019-20", "2020-2021", "2021-22", "2022-2023")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        year_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=2, padx=10)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Semester", "Sem-1", "Sem-2", "Sem-3", "Sem-4")
        year_combo.current(0)
        year_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        Student_Id_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Class Student Information",
                                          font=("times new roman", 12, "bold"))
        Student_Id_frame.place(x=5, y=200, width=580, height=150)

        student_Id_label = Label(Student_Id_frame, text="Student Id:", font=("times new roman", 12, "bold"), bg="white")
        student_Id_label.grid(row=0, column=0, padx=10)

        student_id_entry=Entry(Student_Id_frame,textvariable=self.var_id,width=20,font=("times new roman", 12, "bold"))
        student_id_entry.grid(row=0, column=1, padx=10,sticky=W)

        student_name_label = Label(Student_Id_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=10,pady=5)

        student_name_entry = Entry(Student_Id_frame,textvariable=self.var_name, width=15, font=("times new roman", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=10,pady=5, sticky=W)

        class_div_label = Label(Student_Id_frame, text="Class Division:", font=("times new roman", 12, "bold"),
                                   bg="white")
        class_div_label.grid(row=1, column=0, padx=10,pady=5)

        class_div_entry = Entry(Student_Id_frame,textvariable=self.var_class_div,width=20, font=("times new roman", 12, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5,sticky=W)

        rollno_label = Label(Student_Id_frame, text="Roll No:", font=("times new roman", 12, "bold"),
                                bg="white")
        rollno_label.grid(row=1, column=2, padx=10, pady=5)

        rollno_entry = Entry(Student_Id_frame,textvariable=self.var_rollno, width=15, font=("times new roman", 12, "bold"))
        rollno_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        #button frame
        button_frame =Frame(left_frame, bd=2, relief=RIDGE,bg="white")
        button_frame.place(x=5, y=370, width=580, height=70)

        save_button=Button(button_frame,text="Save",command=self.add_data(),width=10,font=("times new roman", 12, "bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

        update_button = Button(button_frame, text="Update", width=10, font=("times new roman", 12, "bold"), bg="blue",
                             fg="white")
        update_button.grid(row=0, column=1)

        reset_button = Button(button_frame, text="Reset", width=10, font=("times new roman", 12, "bold"), bg="blue",
                             fg="white")
        reset_button.grid(row=0, column=2)

        delete_button = Button(button_frame, text="Delete", width=10, font=("times new roman", 12, "bold"), bg="blue",
                             fg="white")
        delete_button.grid(row=0, column=3)

        take_photo_button = Button(button_frame, text="Take Photo Sample", width=17, font=("times new roman", 12, "bold"), bg="blue",
                             fg="white")
        take_photo_button.grid(row=1, column=0)

        update_photo_button = Button(button_frame, text="Update Photo", width=17, font=("times new roman", 12, "bold"), bg="blue",
                                   fg="white")
        update_photo_button.grid(row=1, column=1)


        #search sytem

        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search System",
                                          font=("times new roman", 12, "bold"))
        search_frame.place(x=5, y=10, width=580, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="readonly")
        search_combo["values"] = ("Select", "Roll No.", "Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = Entry(search_frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_button = Button(search_frame, text="Search", width=5, font=("times new roman", 12, "bold"), bg="blue",
                               fg="white")
        search_button.grid(row=0, column=3,padx=4)

        showall_button = Button(search_frame, text="Show All:", width=5, font=("times new roman", 12, "bold"), bg="blue",
                               fg="white")
        showall_button.grid(row=0, column=4,padx=4)

        #table frame
        table_frame =Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=100, width=580, height=250)

        scrollx=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrolly =ttk.Scrollbar(table_frame, orient=VERTICAL)


        self.student_table=ttk.Treeview(table_frame,column=("Id","Name","Roll no.","Course Division"))

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.student_table.xview())
        scrolly.config(command=self.student_table.yview())

        self.student_table.heading("Id",text="Student Id")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll no.", text="Rollno.")
        self.student_table.heading("Course Division", text="Couse Division")
        self.student_table["show"]="headings"

        self.student_table.column("Id",width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Roll no.", width=100)
        self.student_table.column("Course Division", width=100)

        self.student_table.pack(fill=BOTH,expand=1)



        ##functionDetails
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Shreeyash@123",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute('insert into student values("'+self.var_dep.get()+'","'self.var_course.get()+'","2019","5",5,"shrey","2","2")')
        my_cursor.execute("commit")

    

    
    faceDetection















if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()