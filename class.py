class students:
    def __init__(self, name, course, gender, age):
        self.name = name
        self.course = course
        self.gender = gender
        self.age = age

    def details(self):
        print(f"Name: %s \nCourse: %s \nGender: %s \nAge: %d"
              % (self.name, self.course, self.gender, self.age))


stud1 = students("Erick Were", "Computer Science", "Male", 25)
stud2 = students("Brenda Murugi", "Mechanical Engineering", "Female", 22)
stud3 = students("Aurelia Wambui", "Economics and Finance", "Female", 28)
stud4 = students("Ken Kibandi", "Military Science", "Male", 32)
stud5 = students("Grace Wambui", "Medical Surgery", "Female", 18)

stud1.details()
stud2.details()
stud3.details()
stud4.details()
stud5.details()
