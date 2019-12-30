# -*- coding:utf-8 -*-
# coding=utf-8
# encoding=utf-8

print("hello world")


def practise():
    age = 20
    if age >= 18:
        print('your age is', age)
        print('adult')

    birth = input('input your birth:')
    if int(birth) < 2000:
        print('00前')
    else:
        print("00 后")


def whiledo():
    i = 1
    sumnum = 0
    while i <= 100:
        sumnum += i
        i += 1
    print("1-100的累加和为： %d" % sumnum)


def printAdd():
    i = 1
    while i < 10:
        j = 1
        while j <= i:
            print("%d*%d=%d  " % (j, i, j * i), end='')
            j += 1
        print()
        i += 1


def indexdo():
    mystr = 'hello world and bjsxt yunshuxueyuan sxt beijing'
    print(mystr.find("world"))
    print(mystr.count("world"))
    print(mystr.index("world"))
    f1 = mystr.replace("world", "wahaha")
    print(f1)
    print(mystr.capitalize())
    print(mystr.title())

    classmates = ['Michael', "bob", "Tracy"]
    print(classmates)
    print(len(classmates))
    classmates.append(["cehe", 'dbeb'])
    print(classmates)
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print(d["Michael"])
    info = {'name': '班长', 'id': 100, 'sex': 'f', 'address': '地球亚洲中国北京'}
    print(info.get("age", 18))
    del info['name']
    print(info)
    info.clear()
    print(info)


def add(a):
    a += 10
    print(a)
    return  a


if __name__ == '__main__':
    # import keyword
    #
    # print(keyword.kwlist)
    # print("%.2f" % 3.2235)
    # practise()
    # whiledo()
    # printAdd()
    # indexdo()

    a = 10
    b = add(a)
    print(b)
    print(a)
