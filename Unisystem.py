## This is for the file creation
import pickle
from datetime import datetime
import os

"""
From looking at the assignment theres a couple of things I can confidently point out

Two main classes established so far
Student: 
    Account
    Subject
    Enrolment

Admin: Auto login established
    Database functions: done

Now the way which it has been formatted is more then following lab 9 in the sense of 
1) Account 
2) Backup / Database?
3) Main system: Being worked on, need to try and fix things here and there 
4) Student: Being worked on, genuinely hard
This is to trigger the code
if __name__ == "__main__":
    bank = Bank()
    bank.menu()
"""

class Account:

    """
    ## Password checker
    ## Reg ex: /^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$/gm 
    
        password must contain 1 number (0-9)
        password must contain 1 uppercase letters
        password must contain 1 lowercase letters
        password must contain 1 non-alpha numeric number
        password is 8-16 characters with no space
    """

    def __init__(self, type):
        self.type = type
        self.enrolment = self.read_enrolment()

    def read_enrolment(self):
        return float(input(f'Initial {self.type} subjects enroled'))

    def has_type(self, type):
        return self.type == type

    ## Subject enrolment
    def has(self, subject):
        pass

    def change(self, subject):
        pass
    
    def enrol(self, subject):
        pass
    
    def remove(self, subject, target):
        pass

    def show(self, subject, target):
        pass

    def __str__(self):
        return f'{self.type} account has ${self.enrolment:}'

## This is the backup / student file creator, uses the pickle import
class Database:
    filename = 'student.data'

    @staticmethod
    def initialize():
        try:
            students = []
            if not os.path.exists(Database.filename):
                with open(Database.filename, 'wb') as file:
                    pickle.dump(students, file)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
        except IOError as e:
            print(f'Reading Error: {e}')

    @staticmethod
    def read():
        try:
            with open(Database.filename, 'rb') as file:
                students = pickle.load(file)
            return students
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
            return []
        except IOError as e:
            print(f'Reading Error: {e}')
            return []

    @staticmethod
    def write(students):
        try:
            with open(Database.filename, 'wb') as file:
                pickle.dump(students, file)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
        except IOError as e:
            print(f'Reading Error: {e}')

class main:
    DTF = '%d/%m/%Y - %H:%M:%S'
    NOW = datetime.now()

    def __init__(self):
        self.admin = Admin()
        Database.initialize()
        self.students = Database.read()

    def read_choice(self):
        return input("\033[34m University System: (A)dmin, (S)tudent or X: \033[0m").upper()

    def student(self, name):
        for c in self.students:
            if c.match(name):
                return c
        return None
    
    ## Need to get this to get to the CLI of the student class
    def read_name(self):
        return input('Enter Customer Name: ')
        
    def student_login(self):
        c = self.student(self.read_name())
        if c is not None:
            index = self.students.index(c)
            c.use()
            self.students[index] = c
            Database.write(self.students)
        else:
            print("\033[31m Student does not exist \033[0m")

    def admin_login(self):
        self.admin.use(self)

    ### Bank Class/Main Class
    def menu(self):
        print(f'Univserity menu: {self.NOW.strftime(self.DTF)}')
        while True:
            choice = self.read_choice()
            if choice == 'A':
                self.admin_login()

            elif choice == 'S':
                self.student_login()

            elif choice == 'X':
                print('Thank you')
                break
            else:
                self.help()

    def help(self):
        print('Menu options')
        print('L = Login into customer menu')
        print('A = Login to admin menu')
        print('X = exit')


## This is for the random number ID generator
import random

class Student: 
    """
        Classes needed: 
        ID assignemnt
        enrolment: 4 max and each one assigned a different grade, each one assigned a pass or fail
        enrol and withdrawl
        change password
    """

    def __init__(self, name, subjects):
        self.name = name
        self.subject = subjects

    ## @classmethod: define a method that is bound to the class and not the instance of the class    
    @classmethod
    def create(cls):
        name = input('Create account for Student: ')
        id = random.randrange(0, 999999)
        ## Not sure how to populate the rest with 0, eg 0000001 but will generate between the two 
        return cls(name)

    def match(self, name):
        return self.name == name

    def subjects(self, type):
        for a in self.subjects:
            if a.has_type(type):
                return a
        return None

    """
    def student_login(self):
        c = self.student(self.read_name())
        if c is not None:
            index = self.students.index(c)
            c.use()
            self.students[index] = c
            Database.write(self.students)
        else:
            print("\033[31m Student does not exist \033[0m")
    """

## Not sure if this entire section is correctly done, this is more by eyes
## Think of this as a mix of pusedocode and code, not the best at python so excuse me on this part

    """
    def change(self):
        ## password is changed
        pass

    def enrol(self):
        subject = self.subjects("subjects")
        if subject is not None:
            subject = self.read("enrol")
            subject.change(subject)
        else:
            print("No such enrolment")

    def withdrawl(self):
        subject = self.read("withdraw")
        subjects = self.subjects("subjects")
        if subjects is not None:
            if subjects.has(subject):
                subjects.withdraw(subject)
            else:
                print("Subject not found")

    def grades(self):
        subject = self.subjects("subjects")
        if subject is not None:
            grade = random.randrange(24, 101))
                if grade > 50
                    fail

                if grade < 50
                    85 - 100 HD
                    75 - 84 H
                    65 - 74 C
                    50 - 64 P
                    pass 

        else:
            print("No such enrolment")
    """
            
## Menu selection student view

    def read_choice(self):
        return input('Student course menu (d/w/t/s/x): ').lower()

    def use(self):
        print(f'{self.name} Student menu: {main.NOW.strftime(main.DTF)}')
        while True:
            choice = self.read_choice()
            if choice == 'c': 
                self.change()
            elif choice == 'w':
                self.withdrawl()
            elif choice == 't':
                self.grades()
            elif choice == 'x':
                print('Back to login')
                break
            else:
                self.help()

    def help(self):
        print('Menu options')
        print('c = change')
        print('w = withdraw')
        print('s = grades')
        print('x = exit')

class Admin:
    pass


Database.initialize()
Database.read()

if __name__ == "__main__":
    main = main()
    main.menu()

