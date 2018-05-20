def foo(x):
    print("executing foo(%s)" % (x))


class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()  # 类的实例化
foo(3)  # 普通方法
a.foo(3)  # 实例方法
a.class_foo(3)  # 类方法
a.static_foo(3)  # 静态方法
A.class_foo(3)  # 类调用类方法
print(A.class_foo(3) is a.class_foo(4))  # 注意不管是在类中还是在实例中，都是用相同的地址
A.static_foo(3) # 类里面也可以用静态方法
