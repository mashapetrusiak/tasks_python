import random
import zlib
import time

def number_81():
    print(random.randrange(7,16))
#number_81()

def number_82():
    text = 'hello world!hello world!hello world!hello world!'.encode()
    t = zlib.compress(text)
    print(t)
    print(zlib.decompress(t))
#number_82()

def number_83():
    before = time.time()
    for i in range(100):
        x = 1 + 1
    after = time.time()
    execution_time = after - before
    print(execution_time)
#number_83()

def number_84_85():
    lst = [3, 6, 7, 8]
    random.shuffle(lst)
    print(lst)
#number_84_85()

def number_86():
    sub = ["I", "You"]
    verb = ["Play", "Love"]
    obj = ["Hockey", "Football"]
    for s in sub:
        for v in verb:
            for o in obj:
                print("{} {} {}".format(s, v, o))
#number_86()

def number_87():
    lst1 = [5, 6, 77, 45, 22, 12, 24]
    lst = list(filter(lambda n: n % 2 != 0, lst1))
    print(lst)
#number_87()

def number_88():
    lst1 = [12, 24, 35, 70, 88, 120, 155]
    lst2 = [x for x in lst1 if x % 5 != 0 and x % 7 != 0]
    print(lst2)
#number_88()

def number_89():
    lst1 = [12, 24, 35, 70, 88, 120, 155]
    lst2 = [lst1[i] for i in range(len(lst1)) if i % 2 != 0]
    print(lst2)
#number_89()

def number_90():
    array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
    print(array)
#number_90()