import re


class American():
    pass


class NewYorker(American):
    pass


american = American()
newyorker = NewYorker()


# print(american)
# print(newyorker)

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return 3.1416 * (self.radius ** 2)


circle = Circle(10)


# print(int(circle.area()))

class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


rect = Rectangle(3, 7)


# print(rect.area())

class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length=0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length * self.length


Asqr = Square(16)
print(Asqr.area())
print(Square().area())


def number_55():
    try:
        5 / 0
    except:
        return "You are dividing a number by ZERO!"


print(number_55())
"""class CustomException(Exception):
    def __init__(self, message):
        self.message = message
num = str(input())
try:
    if len(num) < 10:
        raise CustomException("Input is less than 10")
    elif len(num) > 10:
        raise CustomException("Input is grater than 10")
    elif len(num) == 10:
        raise CustomException("Input is equal to 10")
except CustomException as ce:
    print("The error: " + ce.message)"""


def number_57(x):
    email = str(x.split())
    email = email.split('@')
    return email[0]


# print(number_57("john@google.com"))

def number_58(x):
    email = str(x.split())
    pattern = "\w+@(\w+).com"
    ans = re.findall(pattern, email)
    return ans


# number_58()

def number_59(x):
    words = x.split()
    lst = []
    for word in words:
        if word.isdigit():
            lst.append(word)
    return lst


# print(number_59("2 cats and 3 dogs"))

def number_60():
    unicode = u"hello world!"
    return unicode
print(number_60())
