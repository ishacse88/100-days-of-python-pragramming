
class Person:
    __name="isha" 
    def __hello(self):
        print("hello girl")
    def welcom(self):
        self.__hello()
p1=Person()
# print(p1.__name)
# print(p1.__hello())

print(p1.welcom())


# can only be accesed by internal method (__name="isha")

# inheritance-when oneclass(child/derived) derives the porperties $ methods of another class(parent/base).
