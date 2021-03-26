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




# class, *args, **kwargs, super


# def plus(*args):
#     result = 0
#     for number in args:
#         result += number
#     print(result)
#
# plus(1, 2, 1, 1, 1, 2, 1)


class Car:

    def __init__(self, *args, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):  # method
        return f"Car with {self.wheels} wheels"


class Convertible(Car):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # super == 부모로부터 상속
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):  # method
        return f"Car with no roof"


porche = Convertible(color="green", price="$40")  # porche = instance
porche.take_off
print(porche.color, porche.price, porche)

mini = Car()
print(mini.color, mini.price)


# module

# from math import ceil
# print(math.ceil(1.2455))