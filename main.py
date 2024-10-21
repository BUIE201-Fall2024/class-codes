import sys

class Date:
    def __init__(self, Year = 1970, Month = 1, Day = 1) -> None:
        self.Year = 1970
        self.Month = 1
        self.Day = 1
        self.set_date(Year, Month, Day)
        print("The date object just created is {}/{}/{}".format(self.Day, self.Month, self.Year))

    def __del__(self):
        print("The date object being deleted is {}/{}/{}".format(self.Day, self.Month, self.Year))
    
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

today = Date(2024, 10, 21)
print("today refcount: ", sys.getrefcount(today))
tomorrow = today
print("today refcount: ", sys.getrefcount(today))
today.print()

