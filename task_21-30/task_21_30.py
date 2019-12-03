import math


def number_21(x):
    s = x.split(" ")
    x, y = 0, 0
    for i in range(0, len(s)-1):
        if s[i] == 'RIGHT':
            x = x + int(s[i+1])
        elif s[i] == 'LEFT':
            x = x - int(s[i+1])
        elif s[i] == "UP":
            y = y + int(s[i+1])
        elif s[i] == "DOWN":
                y = y - int(s[i+1])
    return int(math.sqrt(x ** 2 + y ** 2))


# print(number_21(input()))

def number_22(x):
    sort = x.split()
    dict = {i: sort.count(i) for i in sort}
    dict = sorted(dict.items())
    return dict


# print(number_22(input()))

def number_23(n):
    return int(n) ** 2


# print(number_23(input()))

# print(str.__doc__)
# print(abs.__doc__)
# print(int.__doc__)
def pow(n, p):
    '''
       param n: This is any integer number
       param p: This is power over n
       return:  n to the power p = n^p
       '''
    return n ** p


# print(pow(2, 8))
# print(pow.__doc__)

class Student:
    name = "Student"

    def __init__(self, name=None):
        self.name = name


Masha = Student("Masha")
# print("%s name is %s"%(Student.name,Masha.name))

Sasha = Student()
Sasha.name = "Sasha"


# print("%s name is %s"%(Student.name,Sasha.name))

def number_26(a, b):
    return a + b


# print(number_26(9,15))

def number_27_28(a):
    return str(a)


# number_27_28(5)

def number_29(a, b):
    return int(a) + int(b)


# number_29("3","4")

def number_30(a, b):
    return a + b
# print(number_30("12","9"))
