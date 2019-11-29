import string
import itertools

def number_91():
    lst = [12, 24, 35, 70, 88, 120, 155]
    lst1 = [lst[i] for i in range(len(lst)) if i not in (0, 4, 5)]
    print(lst1)
#number_91()

def number_92():
    lst = [12, 24, 35, 24, 88, 120, 155]
    for x in range(lst.count(24)):
        lst.remove(24)
    print(lst)
#number_92()

def number_93():
    lst1 = [1, 3, 6, 78, 35, 55]
    lst2 = [12, 24, 35, 24, 88, 120, 155]
    set1 = set(lst1)
    set2 = set(lst2)
    intersection = set1 & set2
    print(intersection)
#number_93()

def number_94():
    def remove(lst):
        lst1 = []
        seen = set()
        for item in lst:
            if item not in seen:
                seen.add(item)
                lst1.append(item)
        return lst1
    lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
    print(remove(lst))
#number_94()

"""class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print(aMale.getGender())
print(aFemale.getGender())"""

def number_96():
    text = input()
    for letter in string.ascii_lowercase:
        cnt = text.count(letter)
        if cnt > 0:
            print("{},{}".format(letter, cnt))
#number_96()

def number_97():
    text = input()
    text = ''.join(reversed(text))
    print(text)
#number_97()

def number_98():
    text = "H1e2l3l4o5w6o7r8l9d"
    new = ''
    for i in range(len(text)):
        if i % 2 == 0:
            new += text[i]
    print(new)
#number_98()

def number_99():
    print(list(itertools.permutations([1, 2, 3])))
#number_99()

def number_100():
    def solve(numheads, numlegs):
        ns = 'No solutions!'
        for i in range(numheads + 1):
            j = numheads - i
            if 2 * i + 4 * j == numlegs:
                return i, j
        return ns, ns
    numheads = 35
    numlegs = 94
    solutions = solve(numheads, numlegs)
    print(solutions)
#number_100()