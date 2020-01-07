'''
Created on 2018年10月10日

@author: Administrator
'''


# coding=utf-8


class Person(object):
    def __init__(self, name):
        self.name = name

    def work(self, type_axe):
        print("%s开始工作了" % (self.name))
        #         axe=StoneAxe()
        #         axe=SteelAxe()
        axe = Factory.create_axe(type_axe)
        print(id(axe))
        axe.cut_tree()


class Axe(object):
    def cut_tree(self):
        print("正在砍树")


class StoneAxe(Axe):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def cut_tree(self):
        print("使用石头做的斧子砍树")


class SteelAxe(Axe):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def cut_tree(self):
        print("使用钢斧头砍树")


class WaterAxe(Axe):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def cut_tree(self):
        print("使用水砍树")


class Factory(object):
    @classmethod
    def create_axe(cls, type_axe):
        if type_axe == "stone":
            return StoneAxe()
        elif type_axe == "steel":
            return SteelAxe()
        elif type_axe == "water":
            return WaterAxe()
        else:
            print("传入的参数不对")


p = Person("张三")
p.work("water")
p.work("water")
p.work("steel")
p.work("steel")
p.work("water")

if __name__ == '__main__':
    pass
