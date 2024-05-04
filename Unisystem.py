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
3) Main system
4) Student
4) Admin / Database?

Main system will need to be linked to both function views

This is to trigger the code
if __name__ == "__main__":
    bank = Bank()
    bank.menu()
"""

class Account:
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
        return input('System menu (L/A/X): ').upper()

    def student(self, name):
        for c in self.students:
            if c.match(name):
                return c
        return None

    def read_name(self):
        return input('Enter student Name: ')

    def show(self):
        student = self.student(self.read_name())
        if student is not None:
            print(student)
        else:
            print("\033[31m Student does not exist \033[0m")

    def view(self):
        for student in self.students:
            print(student)

    def add(self):
        name = self.read_name()
        student = self.customer(name)
        if student is None:
            self.students.append(Student(name))
            Database.write(self.students)
        else:
            print("\033[31m Student already exists \033[0m")

    def remove(self):
        student = self.student(self.read_name())
        if student is not None:
            self.students.remove(student)
            Database.write(self.students)
        else:
            print("\033[31m Student does not exist \033[0m")

    def customer_login(self):
        c = self.customer(self.read_name())
        if c is not None:
            index = self.customers.index(c)
            c.use()
            self.customers[index] = c
            Database.write(self.customers)
        else:
            print("\033[31m Student does not exist \033[0m")

    def admin_login(self):
        self.admin.use(self)

    ### Bank Class/Main Class
    def menu(self):
        print(f'Univserity menu: {self.NOW.strftime(self.DTF)}')
        while True:
            choice = self.read_choice()
            if choice == 'L':
                self.customer_login()
            
            elif choice == 'A':
                self.admin_login()

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

    pass


## This is for the random number ID generator
import random

class Student: 
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        ## Assigning both subjects and grade
        ## self.account = [Account("Enrolment"), Account("Grades")]

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

## Not sure if this entire section is correctly done, this is more by eyes
## Think of this as a mix of pusedocode and code, not the best at python so excuse me on this part

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
            """
            set grades as 
             grades = random.randrange(24, 101)
             if grades <= 25 = fail
             if grades <= 50 = pass
             if grades <= 75 = high distinction
             if grades <= 100 = perfect
            """
        else:
            print("No such enrolment")

## Menu selection student view

    def read_choice(self):
        return input('Customer menu (d/w/t/s/x): ').lower()

    def use(self):
        print(f'{self.name} Student menu:') ## {Bank.NOW.strftime(Bank.DTF)}
        while True:
            choice = self.read_choice()
            if choice == 'c':
                self.change()
            elif choice == 'w':
                self.withdraw()
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




