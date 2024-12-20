# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.height = 0
def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.height = 180
    student2.name = "Olivia"
    student2.age = 21
    student2.height = 160
    student3.name = "Martha"
    student3.age = 18
    student3.height = 170

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, {student1.height} cm')
    print(f'{student2.name}, {student2.age} years old, {student2.height} cm')
    print(f'{student3.name}, {student3.age} years old, {student3.height} cm')
if __name__ == "__main__":
    main()