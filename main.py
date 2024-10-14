class Date:
    def __init__(self, Year = 1970, Month = 1, Day = 1) -> None:
        self.Year = 1970
        self.Month = 1
        self.Day = 1
        self.set_date(Year, Month, Day)
    
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

today = Date(2024, 10, 14)
print("today id: ", id(today))

tomorrow = Date(2024, 10, 15)
print("tomorrow id: ", id(tomorrow))

# everything is an object in Python
i = 4
# i = int(4)
print("type(i): ", type(i))
print("id(i): ", id(i))

f = 3.14
# f = float(3.14)
print("type(f): ", type(f))
print("id(f): ", id(f))

s = "hello, IE 201"
# s = str("hello, IE 201")
print("type(s): ", type(s))
print("id(s): ", id(s))

i2f = float(i)
print("type(i2f): ", type(i2f))
print("id(i2f): ", id(i2f))

# float has a number of functions
i2f.is_integer()

print(id(s))
print(id(s.capitalize()))


def g(value):
    print("within g() - before", value, id(value))
    value += 10
    print("within g() - after", value, id(value))

value = 5
print("outside g() - before", value, id(value))
g(value)
print("outside g() - after", value, id(value))


def f(date):
    print("within f() - before", id(date))
    date.print()
    date.set_date(2025, 10, 14)
    print("within f() - after", id(date))
    date.print()

date = Date(2024, 10, 14)
print("outside f() - before", id(date))
date.print()
f(date)
print("outside f() - after", id(date))
date.print()

# immutable
# int, float, str, tuple
# mutable
# set, dict, list

f = 3.14
print ("id(f): ", id(f))
f *= 2
print ("id(f): ", id(f))
t = (4, 2, 1)
# t[0] = 9

my_dict = {"IE 201": "Caner", 
           "IE 255": "Wolfgang"}

is_201_taught = "IE 201" in my_dict
if (is_201_taught):
    my_dict["IE 201"]

# don't use mutable types as dictionary keys
today = [Date(2024, 10, 14)]
republicDate = [Date(1923, 10, 29)]
my_events_dict = {today: "IE 201 was taught",
                  republicDate: "The republic was formed"}

if (today in my_events_dict):
    print(my_events_dict[today])
