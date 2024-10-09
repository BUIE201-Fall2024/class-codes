class Student:
    def __init__(self) -> None:
        self.ID = 0
        self.Name = None

std1 = Student()
std1.ID = 34242
std1.Name = "caner"
print(std1.ID)
print(std1.Name)

std2 = Student()
std2.ID = 42453
std2.Name = "tamer"

# don't use attributes that are not defined in the class
# std2.Surname = "unal"

print(std2.ID)
print(std2.Name)


