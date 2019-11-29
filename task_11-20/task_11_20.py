import re

def number_11():
    items = []
    num = [x for x in input().split(',')]
    for p in num:
        x = int(p, 2)
        if not x % 5:
            items.append(p)
    print(','.join(items))
#number_11()

def number_12():
    items = []
    for i in range(1000, 3001):
        s = str(i)
        if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
            items.append(s)
    print(",".join(items))
#number_12()

def number_13():
    s = input("Input a string ")
    n = l = 0
    for i in s:
        if i.isdigit():
            n = n + 1
        elif i.isalpha():
            l = l + 1
        else:
            pass
    print("Letters", l)
    print("Numbers", n)
#number_13()

def number_14():
    phrase = input("Input: ")
    phrase = list(phrase)
    u, l = 0, 0
    for i in phrase:
        if i.isupper():
            u = u + 1
        if i.islower():
            l = l + 1
        else:
            pass
    print("UPPER:", u)
    print("lower:", l)
#number_14()

def number_15():
    a = input("Input:")
    value = int(a) + int(2 * a) + int(3 * a) + int(4 * a)
    print(value)
#number_15()

def number_16():
    lst = [str(int(i) ** 2) for i in input().split(',') if int(i) % 2]
    print(",".join(lst))
#number_16()

def number_17():
    result = 0
    while True:
        s = input().split()
        if not s:
            break
        sum, num = map(str, s)
        if sum == 'D':
            result += int(num)
        if sum == 'W':
            result -= int(num)
    print(result)
#number_17()

def number_18():
    val = []
    items = [x for x in input().split(',')]
    for p in items:
        if len(p) < 6 or len(p) > 12:
            continue
        else:
            pass
        if not re.search("[a-z]", p):
            continue
        elif not re.search("[0-9]", p):
            continue
        elif not re.search("[A-Z]", p):
            continue
        elif not re.search("[$#@]", p):
            continue
        elif re.search("\s", p):
            continue
        else:
            pass
        val.append(p)
    print(",".join(val))
#number_18()

def number_19():
    info = input()
    info_list = (case.split(',') for case in info.split(' '))
    print(sorted(info_list))
#number_19()

class Twenty:
    def number_20(self,n):
        return [i for i in range(n+1) if i%7==0]
n = int(input())
num = Twenty()
lst = num.number_20(n)
print(lst)
