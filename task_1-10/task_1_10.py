import math


def number_1():
    list = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            list.append(i)

    return list


# print(number_1())

# n = int(input("n= "))
def number_2(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


# number_2(n)

# n = int(input("n= "))
def number_3(n):
    mydict = {}
    for i in range(1, n + 1):
        mydict[i] = i * i
    return mydict


# number_3(n)

def number_4(n):
    mylist = n.split(',')
    mytuple = tuple(mylist)
    return print(mylist), print(mytuple)

# number_4("1")


class Mystring:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input()

    def printString(self):
        return self.string.upper()


# mystring = Mystring()
# mystring.getString()
# mystring.printString()

def number_6(d):
    d = d.split(',')
    C = 50
    H = 30
    val = []
    items = [x for x in d]
    for D in items:
        val.append(str(int(round(math.sqrt(2 * C * float(D) / H)))))
    return ','.join(val)

# d = input()
# print(number_6(d))

def number_7(d):
    x, y = map(int, d.split(','))
    lst = []
    for i in range(x):
        tmp = []
        for j in range(y):
            tmp.append(i * j)
        lst.append(tmp)
    return lst

# d = input()
# print(number_7(d))

def number_8(text):
    n = sorted(text.split(','))
    return ','.join(n)


# print(number_8("without,hello,bag,world"))

def number_9(x):
    return x.upper()


# print(number_9(input()))

def number_10(x):
    text = sorted(list(set(x.split())))
    return " ".join(text)

# print(number_10(input()))
