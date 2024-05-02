## This is for the file creation
import pickle
from datetime import datetime
import os

"""
The Student Class
• The Student class has the fields:
o ID randomly generated 1 <= ID <= 999999, unique and formatted as 6-digits width. IDs less than 6-digits width should be completed with zeroes from the left.
o name, email, password, and a list of subjects
• A student can only enrol in 4 subject maximum (A course of 4 subjects).
• A student can enrol/drop a subject at any time.
• Upon enrolment in a subject a random mark is generated for this subject 25<= mark <= 100
• Upon enrolment in a subject, the grade of that subject is calculated based on the mark
• A student pass/fail a course if the average mark of the subjects is greater or equal to 50
• A student can change their password at any time.
"""

## This is for the random number generator
import random

class Student:
    def __init__(self, name, email, password, subjects):
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects
        
        ## Assigning both subjects and grade
        ## self.account = [Account("Enrolment"), Account("Grades")]

    @classmethod
    def create(cls):
        name = input('Create account for Student: ')
        id = random.randrange(0, 999999)
        ## Not sure how to populate the rest with 0, eg 0000001
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

    def enrolment(self):
        subject = self.subjects("subjects")
        if subject is not None:
            subject = self.read("enrolment")
            subject.enrolment(subject)
        else:
            """
            Conditional for subject enrolement
            """
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

## Above this line, not sure if done correctly

"""
Not sure how to refurbish this section

    def read_amount(self, action):
        return float(input(f"Amount to {action}: $"))

    def show(self):
        ## print(f"{self.name} bank statement: {Bank.NOW.strftime(Bank.DTF)}")
        for account in self.accounts:
            print(account)

    def __str__(self):
        accounts_info = ' | '.join(str(account) for account in self.accounts)
        return f'{self.name}\t--> {accounts_info}'
"""

## menu selection student view
"""

    def read_choice(self):
        return input('Customer menu (d/w/t/s/x): ').lower()

    def use(self):
        print(f'{self.name} Student menu:') ## {Bank.NOW.strftime(Bank.DTF)}
        while True:
            choice = self.read_choice()
            if choice == 'e':
                self.enrolment()
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
        print('e = enrolement')
        print('w = withdraw')
        print('s = grades')
        print('x = exit')
"""

## This is the backup / student file creator, uses the pickle import

class BackUp:
    filename = 'student.data'

    @staticmethod
    def initialize():
        try:
            students = []
            if not os.path.exists(BackUp.filename):
                with open(BackUp.filename, 'wb') as file:
                    pickle.dump(students, file)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
        except IOError as e:
            print(f'Reading Error: {e}')

    @staticmethod
    def read():
        try:
            with open(BackUp.filename, 'rb') as file:
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
            with open(BackUp.filename, 'wb') as file:
                pickle.dump(students, file)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')
        except IOError as e:
            print(f'Reading Error: {e}')


BackUp.initialize()
BackUp.read()


