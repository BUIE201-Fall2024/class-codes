import sys
import gc

class Date:
    def __init__(self, Year = 1970, Month = 1, Day = 1) -> None:
        self.Year = 1970
        self.Month = 1
        self.Day = 1
        self.set_date(Year, Month, Day)
        self.prev_day = None
        self.next_day = None
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
    
    def set_next_day(self, date):
        self.next_day = date

    def set_prev_day(self, date):
        self.prev_day = date

today = Date(2024, 10, 21)
today.print()

tomorrow = Date(2024, 10, 22)
today.print()


today.set_next_day(tomorrow)
tomorrow.set_prev_day(today)

gc.collect()

del today
del tomorrow

gc.collect()

i = 5