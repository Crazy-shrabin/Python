# Oops in python:
# To map with real scenarios, we started using onject in code.
# This is called object oriented progeamming.
# -----------------------------------------
def calc_sum(a, b):
    sum = a + b
    return sum;
def calc_diff(a, b):
    diff = a - b
    return diff

# -----------------------------------------
# a = calc_sum(8, 23)
# print(a)
# -----------------------------------------


class Student:
       collage_name = "Nist collage"
      
       
       #default constructors
    #    def __init__(self):
    #         print("Creating new student slot in Database...")

       #parameterized constructors
       def __init__(self,fullname, marks):
        self.name = fullname
        self.marks = marks
        print("Creating new student slot in Database...")
        
   
s1 = Student("Karan", 89,)
print(s1.name, s1.marks,Student.collage_name)

s2 = Student("Arjun", 74)
print(s2.name, s2.marks)

print(Student.collage_name)




# ---------------------------------------------








# Class & instance attribute

# class.attr
# obj.attr

# Student(class)