def number_61_62():
    # -*- coding: utf-8 -*-
    s = input()
    u = s.encode('utf-8')
    print(u)
#number_61()

def number_63():
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
        sum += i / (i + 1)
    print(round(sum, 2))
#number_63()

def number_64(n):
    if n == 0:
        return 0
    return number_64(n-1) + 100
#n = int(input())
#print(number_64(n))

def number_65_66(n):
    if n < 2:
        return n
    return number_65_66(n-1) + number_65_66(n-2)
#n = int(input())
#print(number_65_66(n))

"""def number_67(n):
    if n < 2:
        fib[n] = n
        return fib[n]
    fib[n] = number_67(n-1) + number_67(n-2)
    return fib[n]

n = int(input())
fib = [0]*(n+1)
number_67(n)
fib = [str(i) for i in fib]
lst = ",".join(fib)
print(lst)"""

"""def number_68(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1
n=int(input())
val = []
for i in number_68(n):
    val.append(str(i))
print(",".join(val))"""

def number_69():
    n = int(input())
    val = []
    for i in range(n + 1):
        if i % 5 == 0 and i % 7 == 0:
            val.append(str(i))
    print(",".join(val))
#number_69()

def number_70():
    lst = [2, 4, 5, 6]
    for i in lst:
        assert i % 2 == 0, "{} is not an even number".format(i)
#number_70()


