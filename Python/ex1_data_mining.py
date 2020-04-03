# -*- coding: utf-8 -*-

modules = {"maths", "Data Mining", "reseau", "android", "zythologie"}


class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def print_key_data(self):
        print("\n{} data: ".format(self.name))
        print("avg grade : {}".format(sum(self.grades.values())/len(self.grades.values())))
        print("max grade : {}".format(max(self.grades.values())))
        print("min grade : {}".format(min(self.grades.values())))


def get_int_input(label=""):
    readValue = "notDigit"
    while not readValue.isdigit():
        readValue = input("as integer - {}".format(label))
    return int(readValue)


def get_students(nb_students):
    StudentData = []
    print("you will now enter info for {} students".format(nb_students))
    for i in range(nb_students):
        print("\n\nstudent {}".format(i))
        name = input("name: ")
        age = get_int_input(label="enter age: ")
        mods = dict()
        for module in modules:
            readValue = get_int_input("{} grade as integer value: ".format(module))
            mods[module] = readValue
        StudentData.append(Student(name, age, mods))
    return StudentData


if __name__ == "__main__":
    students = get_students(5)
    print("\n\n")
    for student in students:
        student.print_key_data()
