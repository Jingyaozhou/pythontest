class Test(object):
    num_of_instance = 0

    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1


class Person:
    name = "aaa"


if __name__ == '__main__':
    print(Test.num_of_instance)  # 0
    t1 = Test('jack')
    print(Test.num_of_instance)  # 1
    t2 = Test('lucy')
    print(t1.name, t1.num_of_instance)  # jack 2
    print(t2.name, t2.num_of_instance)  # lucy 2

    p1 = Person()
    p2 = Person()
    p1.name = "bbb"
    print(p1.name)  # bbb
    print(p2.name)  # aaa
    print(Person.name)  # aaa
