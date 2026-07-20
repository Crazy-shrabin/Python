# dict = {
#     'table' :["a piece of furniture"," list of facts and figures"],
#     "cat" : "a small animal"
# }

# print(dict)







# subjects = {
#     "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
# }

# print(len(subjects))








# marks = {}
# p = int(input("enter the mark of phy:"))
# marks.update({"phy": p})
# m = int(input("enter the mark of mgmt:"))
# marks.update({"mgmt": m})
# c = int(input("enter the mark of che:"))
# marks.update({"che": c})

# print(marks)





#print the element if the following list using a loop:  [1,4,9,16,25,36,49,64,81,100]
# num = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx += 1
# print("Loop Ended!")




# Search for a number X in this tuple using loop:  (1,4,9,16,25,36,49,64,81,100)
# tup = (1,4,9,16,25,36,49,64,81,100)










#WAP to print numbers form 1 to 10 using a for loop.
# for en in range(1,11):
#     print(en)



#WAP to calculate the sum of all numbers between 1 to 20 using [while] loop.
# i = 1
# total = 0

# while i <= 20:  
#     total = total + i
#     i = i + 1
# print("The sum of numbers from 1 to 20 is: ",total)





#wap to print number from 1 to 100.
# i = 1
# while i <= 100:
#     print(i)
#     i+=1 


#wap to print number from 100 to 1.
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1


#wap to print the multiplication table of a number n
# n = int(input("Enter the num: "))
# i = 1
# m = 10
# while i <= m:
#     print(n * i)
#     i += 1


#Print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]
# numbers = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i <= len(numbers):
#     print(numbers[i])
#     i += 1



# wap to search for a number x in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)
# b = int(input("Enter the tuple number: "))
# a = (1,4,9,16,25,36,49,64,81,100)
# idx = 0
# while idx < len(a):
#     if(a[idx] == b):
#         print("found")
#     idx+=1
 


#WAF to print length of a list. (list is the parameter)
# cities = ["ktm", "ltr", "pkr", "bir"]
# def print_len(lists):
#     print(len(lists))

# print_len(cities)



#WAF to print the elements if a list in a single line. (list is the parameter)
# cities = ["ktm", "ltr", "pkr", "bir"]
# def print_elem():
#     i = 0
#     print(print_elem[i])
#     i+=1
#     print(print_elem)
#     return()

# print_elem(cities)










# 1. Variables & Data TypesQuestion: Create a variable for a store item's name (string),
# its price (float), and the quantity in stock (integer). Calculate the total value of
# the stock and print it.Hint: Total value = price $\times$ quantity.

# items_name = input("Enter the name of product: ")
# items_price = 20
# items_quantity = int(input("Enter the quantity of the product: "))

# total_value = items_price*items_quantity
# print("The total amount of", items_name,"is",total_value,"nrs")








# 2. Strings & Conditional Statements
# Question: Write a program that takes a user's input string. If the length of the string
# is greater than 5 characters, print "Long word!". Otherwise, print "Short word!".

# Hint: Use the len() function and an if-else block.
# user_input = input("Enter the words: ")
# word_len = len(user_input)
# if word_len <= 5:
#     print("Short Word")
# else:
#     print("Long word!")







# 3. Lists & Tuples
# Question: Create a list of three of your favorite fruits. Add a fourth fruit to the
# end of the list, and then print the second fruit in the list.

# Hint: Remember that Python lists use zero-based indexing ([0] is the first item).

# fruits = ["Strawberry", "Litchi", "Mango"]
# fruits.append("Grapes")

# print(fruits[-3])






# 4. Dictionaries & Sets
# Question: Create a dictionary representing a person with the keys "name" and "age".
# Print just the person's age. Then, create a set of numbers {1, 2, 3} and try adding
# the number 2 to it to see what happens.

# Hint: Sets do not allow duplicate values!
# person1 = { 
#     "name" : "Sajana Poudel",
#     "age" : '20'
# }
# print(person1["age"])

# s = set([1,2,3])
# s.add(2)
# print(s)


# 5. Loops (For & While)
# Question: * Part A: Use a for loop to print the numbers from 1 to 5.

# Part B: Use a while loop to print the numbers from 5 down to 1

# i = 1
# while i <= 5:
#     print(i)
#     i += 1



# j = 1
# while j <= 5:
#     print(j)
#     j += 1




# for j in range(1,6,1):
#     print(j)






# 6. Functions
# Question: Write a function called greet_user(name) that takes a name
# as an argument and prints "Hello, [name]!". Call the function with your own name.

# def greet_user(a):
#         print(f"Hello,{a}!")

# greet_user("bibek")



# with open("pratice.txt", "r") as a:
#     data = a.read()

# new_data = data.replace("java","python")
# print(new_data)

# with open("pratice.txt", "w") as a:
#     a.write(new_data)


# def check_for_word(word):
#     word = input("Enter the word:")
#     with open("pratice.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#           print("found")
#         else:
#             print("not found")

# check_for_word("everyone")


# f = open("Oops_lecture_8_.py", "w")
# f.write("#lecture_8")
# f.close()





























#------------------------------Level 1 - Basics------------------------------------

# #qn.1 
# print("Hello, World!")





# # qn.2
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"hello {name}, and your age is {age}")





# #qn.3
# a = 10
# b = 50

# a, b = b, a

# print("The value of a is ",a)
# print("The value of b is ",b)




#qn.4
# a = int(input("Enter the num: "))
# if a%2 == True:
#     print("Odd")
# else:
#     print("Even")





# qn.5
# a = int(input("Enter the 1st(a) number: "))
# b = int(input("Enter the 2nd(b) number: "))
# c = int(input("Enter the 3rd(c) number: "))

# if a >= b and a >= c:
#     print("A is greater")
# elif b >= a and b >= c:
#     print("B is greater")
# else:
#     print("C is greater.")





# qn.6
# num = int(input("enter the number: "))
# i = 1

# for j in range(1, num + 1):
#     i *= j
# print(i)





# qn.7
# n = input("Enter the string: ")

# j = n[::-1]

# print(f"original text: {n}")
# print(f"reversed text: {j}")




# qn.8
# Check if a string is a palindrome
# n = input("Enter the string: ")
# j = n[::-1]

# if n == j:
#     print("This string is palindrome: ", n)
# else:
#     print("This string is not palindrome: ", n)




#qn.9
#Count the vowels in a string
# string = input("Enter the sentence: ")
# vowel = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
# count = 0

# for char in string:
#     if char in vowel:
#         count += 1

# print(count)




#qn.10
#Print the multiplication table of a given number.
# num = int(input("Enter the number to multiply: "))
# for i in range(1,11):
#     result = num * i
#     print(f"{num} * {i} = {result}" )





#----------------------------Level 2 - Loops ------------------------------

#Print numbers from 1 to 100.
# i = 1
# while i <= 100:
#     print(i)
#     i += 1





#print only even numbers form 1 to 100.
# for i in range(1, 101):
#     if i%2 == 0:
#         print(i)






#Print the Fibonacci series up to n terms

# n = int(input("Enter the num: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a)

#     sum = a + b
#     a = b
#     b = sum






#Find the sum of numbers from 1 to n.

n = int(input("Enter the number: "))
total_sum = 0

for i in range(1, n+1):
    total_sum = total_sum + i

print(total_sum)















































































































































