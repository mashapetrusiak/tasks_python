import re


def number_11(y):
    items = []
    num = [x for x in y.split(',')]
    for p in num:
        x = int(p, 2)
        if not x % 5:
            items.append(p)
    return items


# print(number_11(input()))

def number_12():
    items = []
    for i in range(1000, 3001):
        s = str(i)
        if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
            items.append(s)
    return ",".join(items)


# print(number_12())


def number_13(s):
    n = l = 0
    for i in s:
        if i.isdigit():
            n = n + 1
        elif i.isalpha():
            l = l + 1
        else:
            pass
    return "LETTER " + str(l) + "\n" + "NUMBERS " + str(n)


# input(number_13(input()))


def number_14(phrase):
    phrase = list(phrase)
    u, l = 0, 0
    for i in phrase:
        if i.isupper():
            u = u + 1
        if i.islower():
            l = l + 1
        else:
            pass
    return "upper: " + str(u) + "\n" + "lower: " + str(l)


# print(number_14(input()))


def number_15(a):
    value = int(a) + int(2 * a) + int(3 * a) + int(4 * a)
    return value


# print(number_15(input()))

def number_16(x):
    lst = [str(int(i) ** 2) for i in x.split(',') if int(i) % 2]
    return ",".join(lst)


# print(number_16(input()))


def number_17(x):
    result = 0
    while True:
        s = x.split()
        if not s:
            break
        sum, num = map(str, s)
        if sum == 'D':
            result += int(num)
        if sum == 'W':
            result -= int(num)
    print(result)


# print(number_17(input()))

def number_18(s):
    val = []
    items = [x for x in s.split(',')]
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
    return ",".join(val)


# print(number_18(input()))
#
def number_19(info):
    info_list = (case.split(',') for case in info.split(' '))
    return sorted(info_list)


# print(number_19(input()))

class Twenty:
    def number_20(self, n):
        return [i for i in range(n + 1) if i % 7 == 0]


# n = int(input())
# num = Twenty()
# lst = num.number_20(n)
# print(lst)
