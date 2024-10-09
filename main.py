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

def print_date(date):
    print("The date printed using print_date is {}/{}/{}".format(date.Day, date.Month, date.Year))

class Date:
    def __init__(self, Year = 1970, Month = 1, Day = 1) -> None:
        self.Year = 1970
        self.Month = 1
        self.Day = 1
        self.set_date(Year, Month, Day)
        # self.Year = Year
        # self.Month = Month
        # self.Day = Day
    
    def print(self):
        print("The date is {}/{}/{}".format(self.Day, self.Month, self.Year))

    def set_date(self, Year, Month, Day):
        if Month < 1 or Month > 12:
            print("Invalid month")
        elif Day < 1 or Day > 31:
            print("Invalid day")
        # additional validation rules
        else:
            self.Day = Day
            self.Month = Month
            self.Year = Year

today = Date()
today.Year = 2024
today.Month = 10
today.Day = 9

today.print()
# global functions can still be used, but may violate 
# data encapsulation principle in object-oriented design
print_date(today)

tomorrow = Date()
# tomorrow.Year = 2024
# tomorrow.Month = 100
# tomorrow.Day = 10
tomorrow.set_date(2024, 10, 10)
tomorrow.print()

tomorrow.set_date(2024, -10, 10)
tomorrow.print()

next_wednesday = Date(2024, 10, 16)
next_wednesday.print()
# Date.print(next_wednesday)

next_tuesday = Date(-3424, 432, 324)
next_tuesday.print()