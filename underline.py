from underline_var import *
import underline_var

# 注意在该程序中underline_var和underline需要在一个路径下

class MyClass(object):
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = "world!"

# print(_a) #NameError: name '_a' is not defined
print(underline_var._a)
print(b)
a = MyClass()
print(a._semiprivate)
print(a._MyClass__superprivate)
print(dir(a))
