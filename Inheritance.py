class Person:
    def __init__(self,name ,age,weight):
        self.name = name
        self.age = age
        self.weight = weight

class Employee(Person):
    def __init__(self,name,age,weight,work):
        super().__init__(name,age,weight)
        self.work = work

class student(Person):
    def __init__(self,name,age,level,grade, weight):
        super().__init__(name,age,weight)
        self.grade = grade
        self.level = level


Stud1 = student("Kiptoo", "13 years", "Six","B+", 65)
print(f"{Stud1.name} in level {Stud1.level} scored a {Stud1.grade}")
Stud2 = student("Nellie", "16", "eight", "A-", 70)
print(f"{Stud2.name} scored a {Stud2.grade}")
Emp1 = Employee("Lucy","23years","56kgs","chef")
print(f"{Emp1.name} who is {Emp1.age} is a proffessional {Emp1.work}")
Emp2 = Employee("Vinnie","23 years","76kgs","dancer")
print(f"{Emp2.name} who is {Emp2.age} is a {Emp2.work}")
Per1 = Person("Terry","21 years","65kgs")
print(f"{Per1.name} is {Per1.age} with {Per1.weight}")
Per2 = Person("Nephat","23years","79kgs")
print(f"{Per2.name} is {Per2.age} with {Per2.weight}")