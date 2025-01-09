class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def show_detailes(self):
        print(f"The student's name is {self.name}")
        print(f"{self.name}'s age is {self.age}" )

    def grades_avg(self):

        subject = [ i[0] for i in self.grades ]       # The expression [ i[0] for i in self.grades ] is a list comprehension in Python, 
        marks = [ i[1] for i in self.grades ]         # used to create a new list by iterating over an existing one.

        print(f"The marks in {subject} are {marks}, respectively.")
        
        print(f"The average is { sum(marks)/len(marks)}")
        
        
        

Student_01 = Student("Jack", 21, [ ["Math", 75], ["Physics", 60], ["Chemistry", 60] ] )
Student_01.show_detailes()
Student_01.grades_avg()



'''
Output:
The student's name is Jack
Jack's age is 21
The marks in ['Math', 'Physics', 'Chemistry'] are [75, 60, 60], respectively.
The average is 65.0

'''