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


# class Car:
#     def __init__(self, car_brand, car_price):
#         self.brand = car_brand
#         self.price = car_price

# car1 = Car( "Farari", "$250,000")
# car2 = Car( "Lamborgeni", "$350,000")

# print( car1.brand, car1.price)
# print( car2.brand, car2.price )




#------------------Class and instance attributes-----------------
#class.attr
#obj.attr

 




class Student:
    collage_name = "NCMT"
    
    def __init__(self, name, roll_no, address):
        self.name = name
        self.roll_no = roll_no
        self.address = address

    def welcome(self):
        print("Welcome Student.", self.name)

    def get_address(self):
        return self.address
    
S1 = Student("Bibek Parajuli", "03", "kathmandu")

S1.welcome()

print(S1.get_address())


#--------------------------Satic Method----------------------
# example:
# class Student:
#     @staticmethod
#     def collage():
#         print("ABC Collage")







#Abstraction --- hiding the implementation details of a class and only shows the essential features to the user.
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started")

# car1 = Car()
# car1.start()



#Encaptulation --- Wrapping data and function into a single unit (object).

class bankacc1:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print("rs", amount , "was debited")
        print("total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("rs", amount , "has been credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = bankacc1(10000, "12345")
acc1.debit(1000)
acc1.credit(500) 