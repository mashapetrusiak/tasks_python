import math
import random


def number_71():
    expression = input()
    result = eval(expression)
    print(result)


# number_71()

def number_72_73(lst, el):
    bottom = 0
    top = len(lst) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if lst[mid] == el:
            index = mid
        elif lst[mid] > el:
            top = mid - 1
        else:
            bottom = mid + 1
    return index


# lst=[2,5,7,9,11,17,222]
# print(number_72_73(lst,11))
# print(number_72_73(lst,12))

def number_74():
    rand_num = random.uniform(10, 100)
    print(rand_num)


# number_74()

def number_75():
    rand_num = random.uniform(5, 95)
    print(rand_num)


# number_75()

def number_76():
    result = [i for i in range(0, 11, 2)]
    print(random.choice(result))


# number_76()

def number_77():
    result = [i for i in range(0, 11) if i % 5 == 0 and i % 7 == 0]
    print(random.choice(result))


# number_77()

def number_78():
    result = random.sample(range(100, 201), 5)
    print(result)


# number_78()

def number_79():
    result = random.sample(range(100, 201, 2), 5)
    print(result)


# number_79()

def number_80():
    lst = [i for i in range(1, 1001) if i % 5 == 0 and i % 7 == 0]
    result = random.sample(lst, 5)
    print(result)
# number_80()
