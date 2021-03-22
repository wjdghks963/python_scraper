a = "like this"  # string
b = 3  # int
b = 3.12  # float
c = True  # boolean

days = ["Mon", "Tue", "Wed", "Thur", "Fri"]  # list
print("Mon" in days)  # True

days = ("Mon", "Tue", "Wed", "Thur", "Fri")  # tuple

person = {"age": 28, "korean": True,  # dic
          "fav_food": ["tomato"],
          "name": "jung"}

print(person)

# function

age = "26"
print(type(age))
n_age = int(age)
print(type(n_age))


def say_hello(who="anyone"):
    print("hello", who)


say_hello()
say_hello("jung")

# fsting

def say_hello_old(name, old_age):
    return f"Hello {name} you're {old_age} years old"


hello = say_hello_old("jung", 12)
print(hello)


def plus(a, b):
    if type(b) is not int:
        return None
    else:
        return a + b

print(plus(12, "12"))


# for in

days = ("Mon", "Tue", "Wed", "Thur", "Fri")

for d in days:
    if d == "Wed":
        break
    else:
        print(d)


# module

# from math import ceil
# print(math.ceil(1.2455))