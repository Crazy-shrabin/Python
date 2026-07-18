# class car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car has been started.")

#     @staticmethod
#     def stop():
#         print("Car has been stopped.")

# class ToyotaCar(car):
#     def __init__(self, name, type):       
#         super().__init__(type)
#         self.name = name
#         super().start()


# car1 = ToyotaCar("fortuner", "disel")

# car1.start()
# print("the vechile type is:",car1.type)  



class Person:
    name  = "ananymous"

    def changeName(self, name):
        self.name = name

p1 = Person()
p1.changeName("rahul kunwar")
print(p1.name)
print(Person.name)




