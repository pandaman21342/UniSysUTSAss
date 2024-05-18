from tkinter import *

from tkinter import messagebox
import random
import os
import sys
# sys.path.insert(1,'C:\Users\subed\Desktop\PythonStuff\dsa\ASSIGNMENT2\Assignment_maincode')

from Assignment2 import Database
root = Tk()
root.title("Student Registration Login")
root.geometry('440x540')
root.configure(bg='steel blue')
selected_subejects = []
class Subject:
    def __init__(self):
        self.subject_choice = f"{random.randint(1,99):03}"




def login():
    
    username=username_entry.get()
    password=password_entry.get()
    student = Database.verify_cerendials(username,password)
    if student:
        messagebox.showinfo(title="Login Success",message="You are successfully logged in")
        enrollment_window()
      
      

    else:
        messagebox.showerror(title="Login Failed",message="Invalid username or password")  
def enrollment_window():
    def count_subject():
        selected_count = sum([var.get() for var in var_list])
        if selected_count == 0:
            messagebox.showerror(title="Selection Error", message="You must select at least one subject")
        elif selected_count>4:
            messagebox.showerror(title="Selection Error", message="You can select a maximum of 4 subjects")
            for var in var_list:
                if var.get() == 1:
                    var.set(0)
                    break

        update_selected_subjects()

    def update_selected_subjects():    

            global selected_subjects
            selected_subjects = []

            for i, var in enumerate(var_list):
                  if var.get():
                        selected_subjects.append(subjects_list[i])
            
            # subject_window()
                   
        


    top = Toplevel()
    top.title("Enrollment window")
    top.geometry('600x500')
    top.configure(bg='light grey')
    enrollment_label = Label(top,text = "LIST OF ENROLLMENT SUBJECT",bg='#333333',fg='#FF3399',font = ("Arial",15))
    enrollment_label.grid(row=0, column=0,columnspan=2, sticky="news", pady=40)

    subjects_list = []
    while len(subjects_list) < 10:
        new_subject = Subject()
        if new_subject.subject_choice not in [subject.subject_choice for subject in subjects_list]:
            subjects_list.append(new_subject)

    var_list = [IntVar() for _ in subjects_list]

    for i, subject in enumerate(subjects_list):
        Checkbutton(top, text=f"Subject {subject.subject_choice}", variable=var_list[i], command=count_subject).grid(row=i+1, column=0, sticky=W)

    button4 = Button(top, text="View your subject list", bg="#FF3399", fg="#FFFFFF", font=("Arial", 15), command=subject_window)
    button4.grid(row=len(subjects_list)+1, column=0, columnspan=2, pady=20)
   


def subject_window():
    subject_win =Toplevel()
    subject_win.title("Subject Window")

    subject_label = Label(subject_win,text="Enrolled Subjects",bg='pink',font=("Arial",19))
    subject_label.pack(pady=14)

    subjects_list = Listbox(subject_win,bg = 'white',font=("Arial",15),width=32,height = 6)

    for subject in selected_subjects:
        subjects_list.insert(END,f" Subject {subject.subject_choice}")
    subjects_list.pack(padx=22,pady=22)  

    button5 = Button(subject_win,text = "Thankyou for enrollment",command = subject_win.destroy)
    button5.pack(side='bottom',pady=20)

    # Button(subject_win,text="Thankyou for enrollment",command=subject_win.destroy).grid( column=0, columnspan=2, pady=20)  








#create widget

login_label = Label(
    root,text = "Login",bg='#333333',fg='#FF3399',font = ("Arial",30))

username_label = Label(
    root,text="username",bg='#333333',fg='#FFFFFF',font = ("Arial",15))
username_entry= Entry(root,font=("Arial",15))
password_entry=Entry(root,show="*",font=("Arial",15))
password_label = Label(
    root,text = "Password",bg='#333333',fg="#FFFFFF",font=("Arial",15))
login_button = Button(
    root,text="Login",bg="#FF3399",fg="#FFFFFF",font = ("Arial",15),command=login
)


#Placing widgets on the screen
login_label.grid(row=0, column=0,columnspan=2, sticky="news", pady=40)
username_label.grid(row=1,column=0)
username_entry.grid(row=1,column=1,pady=20)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1,pady=20)
login_button.grid(row=3,column=0,columnspan=2,pady=30)





root.mainloop()