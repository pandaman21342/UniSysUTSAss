########################################################
#32555 - Fundamentals of Software Development - AT 1.2 #
# Coded by Jacob Everson
# Word colour edited by Jonathan Hong 
########################################################

import re
import random
import os

class Utils:

    # Define REGEX rules for email and password formatting
    EMAIL_REGEX = r'\b[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com\b'
    PASSWORD_REGEX = r'\b^[A-Z][a-zA-Z]{5,}[0-9]{3,}\b'

class Student:

    # Creates a new student with subjects as an empty list
    def __init__(self, name, email, password, subjects=None):

        self.id = self.generate_id()
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects if subjects else []

    # Return a random 6 digit number for student ID
    def generate_id(self):
        return str(random.randint(1, 999999)).zfill(6)

    # Adds a new subject to the subject list if there are less than 4
    def add_subject(self, subject):
        
        if len(self.subjects) < 4:

            self.subjects.append(subject)
            print(f"\033[33m Enrolling in Subject-{subject.id} \033[0m")
            print(f"\033[33m You are now enrolled in {len(self.subjects)} out of 4 subjects \033[0m")

        else:
            print("\033[31m Students are allowed to enrol in 4 subjects only \033[0m")

    # Removes a subject if any exist
    def remove_subject(self, subject):

        if subject in self.subjects:
            self.subjects.remove(subject)
            print(f"\033[33m Dropping Subject-{subject} \033[0m")
            print(f"\033[33m You are now enrolled in {len} out of 4 subjects \033[0m")

        else:
            print("\033[31m Subject not found. \033[0m")

    # Changes the password
    def change_password(self, new_password):
        
        # Keep asking for the password until it meets regex formatting
        while True:

            # If the new password matches the correct regex formatting
            if re.match(Utils.PASSWORD_REGEX, new_password):
                
                # Keep asking for the confirmation password until it matches the new password
                while True:
                    
                    # Get a confirmation password
                    confirm_password = input("Confirm Password: ")

                    # Check to see if the confirmation password matches the new password
                    if confirm_password == new_password:
                        
                        # Assign the new password
                        self.password = new_password
                        break

                    else:

                        print("\033[31m Password does not match - try again \033[0m")
            
                break
                
    # Shows all enrolled subjects
    def show_enrollment(self):
        
        print(f"\033[33m Showing {len(self.subjects)} subjects \033[0m")

        # While more subjects in a record, print them out
        for subject in self.subjects:
            print("test")

class Subject:

    # Defines the subject ID and mark for a subject, randomly assigns mark
    def __init__(self, id, mark=None):

        self.id = str(id).zfill(3)
        self.mark = mark if mark else random.randint(25, 100)

    # Calculates the grade based on the assigned mark
    def calculate_grade(self):

        if self.mark >= 85:
            return 'HD'
        
        elif self.mark >= 75:
            return 'D'
        
        elif self.mark >= 65:
            return 'C'
        
        elif self.mark >= 50:
            return 'P'
        
        else:
            return 'F'

class Database:
    
    # Checks to see if the database 'students.data' exists in the default directory
    @staticmethod
    def check_file_exists():

        return os.path.exists("students.data")

    # Creates the database 'students.data' if it doesn't already exist
    @staticmethod
    def create_file_if_not_exists():

        if not Database.check_file_exists():
            with open("students.data", "w"):
                pass
    
    # Takes a new student and writes the data to the 'student.data' database
    @staticmethod
    def write_student_data(student):

        # Append the 'students.data' file with new student data 
        with open("students.data", "a") as file:

            file.write(f"{student.id},{student.name},{student.email},{student.password}")

            # While there are more subjects, add subjects information too
            for subject in student.subjects:

                file.write(f",{subject.id}:{subject.mark}")
            file.write("\n")

    # Retrieves student information from the database
    @staticmethod
    def read_student_data():
        
        # Creates a new empty list to store the student data
        students = []

        # Checks to make sure the database exists
        if Database.check_file_exists():

            # Opens the database to be read
            with open("students.data", "r") as file:
                
                # Checks over each line of the database
                for line in file:

                    # Split up the data save against each row, format should be 'ID', 'Name', 'Email', 'Password', and 'Subjects'
                    data = line.strip().split(",")

                    # Declares new student with 'Name', 'Email', and 'Passowrd'
                    student = Student(data[1], data[2], data[3])

                    # Loops for each subject in student record
                    for subject_data in data[4:]:
                                                
                        # Assigns subject ID and subject mark from the database
                        subject_id, mark = subject_data.split(":")
                        
                        # Creates a new subject for the student and assigns the provided ID and mark
                        student.subjects.append(Subject(subject_id, int(mark)))
                    
                    # Adds the new student information to the students list
                    students.append(student)

        return students

    # Used to clear all data from the 'students.data' file
    @staticmethod
    def clear_data():

        print("\033[33m Clearing students database \033[0m")

        # Confirm the user wants to clear the database
        choice = input("\033[31m Are you sure you want to clear the database (Y)ES/(N)O:\033[0m ").lower()

        if choice == "y":    
            
            # Open the file, then empty it
            with open("students.data", "w") as file:
                file.truncate()

            print("\033[33m Students data cleared \033[0m")

        else:
            return  

    # Check to see if the student already exists in the database
    @staticmethod
    def verify_credentials(email,password):
        
        students = Database.read_student_data()
        for student in students:

            if student.email == email and student.password == password:
                return student
        return None

# Starts the main menu, all others pull in from this class
class UniversitySystem:

    @staticmethod
    def start():
        # Creates the database if it doesn't exist
        Database.create_file_if_not_exists()

        # Loop for repeatedly displaying the menu
        while True:
            choice = input("\033[34m University System: (A)dmin, (S)tudent, or X : \033[0m").lower()

            if choice == 'a':
                AdminSystem.start()

            elif choice == 's':
                StudentSystem.start()

            elif choice == 'x':
                print("\033[33m Thank You \033[0m")
                break

            else:
                print("\033[31m Invalid option. Please try again. \033[0m")

# Starts the class for the admin menu
class AdminSystem:
    @staticmethod

    def start():
        
        # Loop for repeatedly displaying the menu
        while True:
            choice = input("\033[34m        Admin System (c/g/p/r/s/x): \033[0m").lower()

            if choice == 'c':
                Database.clear_data()

            elif choice == 'x':
                break

            else:
                print("\033[31m Invalid option. Please try again. \033[0m")

# Starts the class for the student menu
class StudentSystem:
    @staticmethod

    def start():

        # Creates a loop to run the student system
        while True:

            # Get a menu option from the user
            choice = input("\033[34m        Student System (l/r/x): \033[0m").lower()
            
            if choice == 'l':
                
                # Get the login credentials
                print("\033[32m Student Sign In \033[0m")

                # Creates a loop to continue prompting for credentials
                while True:

                    email = input("Email: ")
                    password = input("Password: ")

                    # Check the formatting of the credentials against regex format
                    if re.match(Utils.EMAIL_REGEX, email) and re.match(Utils.PASSWORD_REGEX, password):
                        
                        print("\033[33m email and password format acceptable \033[0m")

                        # Check to see if the student is in the database
                        student = Database.verify_credentials(email, password)

                        # Give access to student menu if they exist
                        if student:

                            StudentCourseSystem.start(student)
                            break

                        else:
                            print("\033[31m Student does not exist \033[0m")
                            break

                    else:
                        print("\033[31m Incorrect email or password format \033[0m")

            elif choice == 'r':

                print("\033[32m Student Sign Up \033[0m")

                # Creates a loop to continue prompting for credentials
                while True:
                    
                    # Get email and password
                    email = input("Email: ")
                    password = input("Password: ")
                    
                    # Check to see if the email and password match the required regex format
                    if re.match(Utils.EMAIL_REGEX, email) and re.match(Utils.PASSWORD_REGEX, password):

                        print("\033[33m email and password formats acceptable \033[0m")

                        # Check if the student exists
                        student = Database.verify_credentials(email, password)

                        if student:

                            print(f"\033[31m Student {student.name} already exists \033[0m")
                        
                        else:
                            
                            # ammend the database with the new student details
                            name = input("Name: ")
                            student = Student(name, email, password)
                            Database.write_student_data(student)

                            print(f"\033[33m Enrolling Student {name} \033[0m")
                        
                        break

                    else:
                        print("\033[31m Incorrect email or password format \033[0m")

            elif choice == 'x':
                break

            else:
                print("\033[31m Invalid option. Please try again. \033[0m")

# Starts the student course system
class StudentCourseSystem:
    @staticmethod 

    def start(student):

        while True:

            # Chose an option within the student menu
            choice = input("Student Course Menu (c/e/r/s/x): ").lower()

            # Change password
            if choice == 'c':
                print("\033[33m Updating Password \033[0m")
                new_password = input("New Password: ")
                student.change_password(new_password)

            # Enrol in subject
            elif choice == 'e':
                
                subject = random.randint(1, 999)
                student.add_subject(Subject(subject))

            # Remove subject
            elif choice == 'r':
                subject = input("Remove Subject by ID: ")
                student.remove_subject(subject)

            # Show Enrolment
            elif choice == 's':
                student.show_enrollment()

            # Exit the menu
            elif choice == 'x':
                break

            else:
                print("\033[31m Invalid option. Please try again. \033[0m")

# Runs an instance of the university system
UniversitySystem.start()
