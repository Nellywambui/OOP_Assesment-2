class Staff:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school


class Teachers(Staff):
    def __init__(self, name, age, school, experience):
        super().__init__(name, age, school)
        self.experience = experience


Teacher1 = Teachers("Ruth",36,"Kagio", '5years')
print(f"{Teacher1.name} who is {Teacher1.age} years works in {Teacher1.school} school has {Teacher1.experience} teaching experience")
Teacher2 = Teachers("Joyce",54,"Waridi", '4years')
print(f"{Teacher2.name} is {Teacher2.age} years and works in {Teacher2.school} school has {Teacher2.experience} teaching experience" )
staff1 = Staff("Lewis",45,"Kilimani")
print(f"{staff1.name} who is {staff1.age} works in {staff1.school}")
staff2 = Staff("Antony",35,"Jikaze")
print(f"{staff2.name} who is {staff2.age} works in {staff2.school}")
