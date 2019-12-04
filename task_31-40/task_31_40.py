def number_31(inp):
    word1, word2 = inp.split()
    len1 = len(word1)
    len2 = len(word2)
    if len1 > len2:
        return word1
    elif len1 < len2:
        return word2
    else:
        return word1 + '\n' + word2


# print(number_31(input()))


def number_32(a):
    if int(a) % 2 == 0:
        return "It is an even number"
    else:
        return "It is an odd number"


# a = int(input("Number: "))
# number_32(a)

def number_33():
    d = dict()
    for i in range(1, 4):
        d[i] = i ** 2
    return d


# print(number_33())

def number_34():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    return d


# print(number_34())

def number_35():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    return d.values()


# print(number_35())

def number_36():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    return d.keys()


# print(number_36())

def number_37():
    lst = list()
    for i in range(1, 21):
        lst.append(i ** 2)
    return lst


# print(number_37())

def number_38():
    lst = list()
    for i in range(1, 21):
        lst.append(i ** 2)
    return lst[:5]


# print(number_38())

def number_39():
    lst = list()
    for i in range(1, 21):
        lst.append(i ** 2)
    return lst[-5:]


# print(number_39())

def number_40():
    lst = list()
    for i in range(1, 21):
        lst.append(i ** 2)
    return lst[5:]


print(number_40())
