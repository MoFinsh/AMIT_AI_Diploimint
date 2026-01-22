from abc import ABC, abstractmethod

class Person (ABC) :
    def __init__(self,name, age, email, address, national_ID):
        self.name = name
        self.age = age
        self.email = email
        self.address = address
        self.national_ID = national_ID
    
    def get_info(self):
        return f"hello {self.name} your age is {self.age} \n you lives in {self.address} and your national id is {self.national_ID} \n "

class Student(Person):
    number_of_students = 0
    def __init__(self, name, age, email, address, national_ID):
        super().__init__(name, age, email, address, national_ID)
        self.courses = []
        self.grades = {}
        Student.number_of_students += 1
        self.student_id = self.set_student_id()
        self.educational_mail = self.set_educational_mail()

    def set_student_id (self):
        student_id = str(Student.number_of_students).zfill(4)
        return student_id

    def set_educational_mail(self):
        educational_mail = f"{self.name}{self.national_ID}.edu"
        return educational_mail
    
    def add_course(self,course,teacher):
        self.courses.append(course)
        return f"you add {course} course and your teacher is {teacher} "

    def remove_course(self,course):
        self.courses.remove(course)

    def get_grade(self):
        for key, value in self.grades.items():
            print(f"{key} ==> {value}")

    def get_info(self):
        Student_info = super().get_info()
        return Student_info + f"you are student your student id is {self.student_id} and your educational mail is{self.educational_mail} \n your courses is {self.courses}"
        
class teacher(Person):
    def __init__(self, name, age, email, address, national_ID):
        super().__init__(name, age, email, address, national_ID) 
        self.hours = 8
        self.courses = []
        self.salary = self.get_salary

    def add_course(self,course):
        self.courses.append(course)
        return f"you can teach {course} as a course "

    def remove_course(self,course):
        self.courses.remove(course)
    
    def get_salary(self):
        salary = self.courses.count()*600
        return salary

    def get_info(self):
        teacher_info = super().get_info()
        return teacher_info + f"you are a teacher your salary is {self.salary} and your courses which you teach it is {self.courses}"
    
class Course:
    def __init__(self,name, teacher):
        self.name = name
        self.Course_credits = 150
        self.teacher = teacher
        self.students = []
        self.teachers = []

    def add_student(self,name):
        self.students.append(name)
        return f"you add {name} to students "

    def remove_student(self,name):
        self.teachers.remove(name)

    def add_teacher(self,name):
        self.teachers.append(name)
        return f"you add {name} to teacher "

    def remove_teacher(self,name):
        self.teachers.remove(name)

    def course_info(self):
        return f"you enrolled to {self.name} course with teacher {self.teacher}"
