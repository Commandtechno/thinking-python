import datetime

now = datetime.datetime.now()

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

print("Weekday:", weekdays[now.weekday()])

birthday = datetime.datetime.strptime(
    input("Enter your birthday (dd/mm/yyyy): "), "%d/%m/%Y"
)

age = (now - birthday).days // 365

print("You are", age, "years old.")

if birthday.month == 2 and birthday.day == 29:
    birthday = birthday.replace(month=3, day=1)

next_birthday = birthday.replace(year=now.year)

if next_birthday < now:
    next_birthday = next_birthday.replace(year=now.year + 1)

print("Your next birthday is in", next_birthday - now)
