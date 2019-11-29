import math


def number_21():
    x, y = 0, 0
    while True:
        step = input("Type in UP/DOWN/LEFT/RIGHT #step number: ")
        if step == "":
            break
        else:
            step = step.split(" ")
            if step[0] == "UP":
                y = y + int(step[1])
            elif step[0] == "DOWN":
                y = y - int(step[1])
            elif step[0] == "LEFT":
                x = x - int(step[1])
            elif step[0] == "RIGHT":
                x = x + int(step[1])
    c = int(math.sqrt(x ** 2 + y ** 2))
    print("Distance:", c)


# number_21()

def number_22():
    sort = input().split()
    dict = {i: sort.count(i) for i in sort}
    dict = sorted(dict.items())
    for i in dict:
        print("%s:%d" % (i[0], i[1]))


# number_22()

def number_23():
    n = int(input("n= "))
    print(n ** 2)


# number_23()

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
    b = str(a)
    print(b)
    print(type(b))


# number_27_28(5)

def number_29(a, b):
    print(int(a) + int(b))


# number_29("3","4")

def number_30(a, b):
    print(a + b)
# number_30("12","9")
