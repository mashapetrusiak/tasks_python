def number_41():
    tup = list()
    for i in range(1, 21):
        tup.append(i ** 2)
    return tuple(tup)


# print(number_41())


def number_42():
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    lst = int(len(tup) / 2)
    common = [str(tup[:lst]), str(tup[lst:])]
    return '\n'.join(common)


# print(number_42())

def number_43():
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tup1 = tuple(i for i in tup if i % 2 == 0)
    return tup1


# print(number_43())

def number_44(word):
    if word.lower() == 'yes':
        return 'Yes'
    else:
        return "No"


# print(number_44("YES"))


def number_45():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def even(x):
        return x % 2 == 0

    even = list(filter(even, lst))
    return even


# print(number_45())

def number_46():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    square = list(map(lambda x: x ** 2, lst))
    return square

# print(number_46())

def number_47():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def even(x):
        return x % 2 == 0

    def squer(x):
        return x * x

    lst = map(squer, filter(even, lst))
    return list(lst)


# print(number_47())

def number_48():
    even = list(filter(lambda x: x % 2 == 0, range(1, 21)))
    return even


# print(number_48())

def number_49():
    squar = list(map(lambda x: x ** 2, range(1, 21)))
    return squar


# print(number_49())

class American():
    @staticmethod
    def printNationality():
        return "I am American"

# american = American()
# american.printNationality()
# American.printNationality()
