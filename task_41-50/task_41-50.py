def number_41():
    tup = list()
    for i in range(1, 21):
        tup.append(i ** 2)
    print(tuple(tup))
#number_41()

def number_42():
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    lst = int(len(tup) / 2)
    print(tup[:lst], "\n", tup[lst:])
#number_42()

def number_43():
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tup1 = tuple(i for i in tup if i % 2 == 0)
    print(tup1)
#number_43()

def number_44():
    word = input()
    if word.lower() == 'yes':
        print('Yes')
    else:
        print("No")
#number_44()

def number_45():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def even(x):
        return x % 2 == 0
    even = list(filter(even, lst))
    print(even)
#number_45()

def number_46():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squar = list(map(lambda x: x ** 2, lst))
    print(squar)
#number_46()

def number_47():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def even(x):
        return x % 2 == 0
    def squer(x):
        return x * x
    lst = map(squer, filter(even, lst))
    print(list(lst))
#number_47()

def number_48():
    even = list(filter(lambda x: x % 2 == 0, range(1, 21)))
    print(even)
#number_48()

def number_49():
    squar = list(map(lambda x: x ** 2, range(1, 21)))
    print(squar)
#number_49()

class American():
    @staticmethod
    def printNationality():
        print("I am American")
american = American()
american.printNationality()
American.printNationality()
