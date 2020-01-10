# coding= utf-8


def sum_test():
    num1 = input("输入第一个数： ")
    num2 = input("输入第二个数： ")
    print(f'{num1} + {num2} = %f' % (float(num1) + float(num2)))


def sqr_test():
    num1 = input("输入数字：")
    print(float(num1) ** 0.5)
    import math
    print(math.sqrt(float(num1)))


import random


def random_test():
    print(random.randint(0, 9))


def num_test():
    import unicodedata
    while 1:
        num = input("请输入：")
        try:
            print(unicodedata.numeric(num))
        except Exception as err:
            print(err)
            break


def print_multi():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{j} * {i} = {i * j}\t', end='')
        print()


def print_fei():
    num1 = 0
    num2 = 1
    count = int(input("输入数量"))
    while count >= 0:
        print(num1, end=",  ")
        num1, num2 = num2, num1 + num2
        count = count - 1


def print_am():
    count = int(input("输入数量："))
    start = 0
    while count > 0:
        lenth = len(str(start))
        tmp = start
        sum1 = 0
        while tmp > 0:
            sum1 = sum1 + (tmp % 10) ** lenth
            tmp = tmp // 10

        if sum1 == start:
            print(start)
            count += 1

        start = start + 1


def oct_hex_bin_test():
    dec = int(input("输入数字："))
    print("十进制数为：", dec)
    print("转换为二进制为：", bin(dec))
    print("转换为八进制为：", oct(dec))
    print("转换为十六进制为：", hex(dec))


def ascii_test():
    # 用户输入字符
    c = input("请输入一个字符: ")

    # 用户输入ASCII码，并将输入的数字转为整型
    a = int(input("请输入一个ASCII码: "))

    print(c + " 的ASCII 码为", ord(c))
    print(a, " 对应的字符为", chr(a))


def hcf():
    a = int(input("第一个数： "))
    b = int(input("第二个数： "))

    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if (a % i == 0) and (b % i == 0):
            hec = i
    print("最大公约数为： ", hec)


def lcm():
    a = int(input("第一个数： "))
    b = int(input("第二个数： "))

    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break
        greater += 1

    print("最小公倍数为：", lcm)


import calendar
import datetime


def calend():
    yy = int(input("输入年份："))
    mm = int(input("输入月份："))
    print(calendar.month(yy, mm))
    mothRange = calendar.monthrange(2019, 10)
    print(mothRange)
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    print(yesterday)


def file_io():
    with open("123.txt", "wt") as out_file:
        out_file.write("该文本会写入到文件中\n看到我了吧！")

    with open("123.txt", "rt") as in_file:
        text = in_file.read()
    print(text)


def str_test():
    print("测试实例一")
    str = "runob.com"
    print(str.isalnum())
    print(str.isalpha())
    print(str.isdigit())
    print(str.islower())
    print(str.isupper())
    print(str.istitle())
    print(str.isspace())

    print("测试实例二")
    str = "runob"
    print(str.isalnum())
    print(str.isalpha())
    print(str.isdigit())
    print(str.islower())
    print(str.isupper())
    print(str.istitle())
    print(str.isspace())
    print(str.upper())
    print(str.lower())
    print(str.capitalize())
    print(str.title())


def list_test():
    li = ["a", "b", "mpilgrim", "z", "example"]
    print(li[1])
    print(li[-1])
    print(li[-3])
    print(li[1:3])
    print(li[1:-1])
    print(li[1:])
    print(li[0:3])
    li.append("new")
    li.insert(2, "new")
    li.extend(["two", "elements"])
    print(li)
    print(li.index("example"))
    print(li.index("new"))
    print(li.index("a"))
    print("c" in li)
    li.remove("z")
    li.remove("new")
    li.pop()
    li += ["example", "new"]
    li = li * 3
    print(li)
    params = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
    lii = ["%s=%s" % (k, v) for k, v in params.items()]
    print(lii)
    print(":".join(["%s=%s" % (k, v) for k, v in params.items()]))


def fish_test():
    fish = 1
    while True:
        total, enough = fish, True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
        if enough:
            print(f'总共{fish}条鱼')
            break
        fish += 1


from functools import reduce


def red_test():
    list = [1, 3, 5, 7, 9, 34]
    print(reduce(lambda x, y: x + y, list))


def binarySearch(arr, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1


def search():
    arr = [2, 3, 4, 10, 40]
    while True:
        x = int(input("请输入"))
        result = binarySearch(arr, 0, len(arr) - 1, x)
        if result != -1:
            print("元素索引为： ", result)
        else:
            print("不在数组中")


if __name__ == '__main__':
    # hcf()
    # sum_test()
    # sqr_test()
    # random_test()
    # num_test()
    # print_multi()
    # print_fei()
    # print_am()
    # oct_hex_bin_test()
    # ascii_test()
    # lcm()
    # calend()
    # file_io()
    # str_test()
    # calend()
    # list_test()
    # fish_test()
    # red_test()
    search()
