#lecture_8
#Oops in python
#To map with real world scenarios, we started using objects in code.
#This is called object oriented programming.

# class Student:
#     name = "Bibek parajuli"
#     age = "20"
#     collage = "NCMT"
#     address = "Gongabu"
#     relationship_status = "Not Married"

# s1 = Student

# print(s1.name)
# print(s1.relationship_status)


# class Student:

#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.mark = marks
#         print("Adding new student...")


# s1 = Student("karan", 93)
# print(s1.name, s1.mark)

# s2 = Student("arjun", 73)
# print(s2.name, s1.mark)



# class student:
#     def __init__(self, name, address, marks):
#         self.name = name
#         self.address = address
#         self.mark = marks

# s1 = student("Bibek Parajuli", "Katmnadu", 99)
# s2 = student("Sajana Poudel", "Baglung", "1")

# print(s1.name, s1.address, s1.mark)
# print(s2.name, s2.address, s2.mark)


class Car:
    def __init__(self, car_brand, car_price):
        self.brand = car_brand
        self.price = car_price

car1 = Car("Farari", "$250,000")
car2 = Car("Lamborgeni", "$350,000")

print(car1.car_brand, car1.car_price)
print(car2.car_brand, car2.car_price)










