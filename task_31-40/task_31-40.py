def number_31(word1,word2):
    len1 = len(word1)
    len2 = len(word2)
    if len1 > len2:
        print(word1)
    elif len1 < len2:
        print(word2)
    else:
        print(word1)
        print(word2)
#word1,word2=input().split()
#number_31(word1,word2)

def number_32(a):
    if a % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
#a = int(input("Number: "))
#number_32(a)

def number_33():
    d = dict()
    for i in range(1, 4):
        d[i] = i ** 2
    print(d)
#number_33()

def number_34():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    print(d)
#number_34()

def number_35():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    for x in d.values():
        print(x)
#number_35()

def number_36():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    for x in d.keys():
        print(x)
#number_36()

def number_37():
    lst = list()
    for i in range(1, 21):
        lst.append(i ** 2)
    print(lst)
#number_37()

def number_38():
    lst = list()
    for i in range(1, 21):
        lst.append(i ** 2)
    for i in range(5):
        print(lst[i])
#number_38()

def number_39():
    lst = list()
    for i in range(1, 21):
        lst.append(i ** 2)
    for i in range(19, 14, -1):
        print(lst[i])
#number_39()

def number_40():
    lst = list()
    for i in range(1, 21):
        lst.append(i ** 2)
    for i in range(5,20):
        print(lst[i])
#number_40()
