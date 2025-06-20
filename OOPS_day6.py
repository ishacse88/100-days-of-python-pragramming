
class Person:
    name="random/anonymous"
    # def changeName(self,name):
        # self.name=name
        # Person.name=name
        # self.__class__.name="rahul"


    @classmethod
    def changename(cls,name):
            cls.name=name

        
p1=Person()
p1.changename("isha kumari")
print(p1.name)
print(Person.name) 