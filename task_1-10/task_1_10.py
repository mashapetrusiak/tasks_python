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
        print(self.string.upper())


# mystring = Mystring()
# mystring.getString()
# mystring.printString()

def number_6():
    C = 50
    H = 30
    val = []
    items = [x for x in input('D = ').split(',')]
    for D in items:
        val.append(str(int(round(math.sqrt(2 * C * float(D) / H)))))
    print(','.join(val))


# number_6()

def number_7():
    x, y = map(int, input().split(','))
    lst = []
    for i in range(x):
        tmp = []
        for j in range(y):
            tmp.append(i * j)
        lst.append(tmp)
    print(lst)


# number_7()

def number_8():
    text = str(input("Enter text: "))
    n = sorted(text.split(','))
    print(n)


# number_8()

def number_9():
    lst = []
    while True:
        x = input()
        if x == 'break':
            break
        lst.append(x.upper())
    for upp in lst:
        print(upp)


# number_9()

def number_10():
    text = sorted(list(set(input().split())))
    print(" ".join(text))
# number_10()
