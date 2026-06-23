# Basic Arithmetic and Type Identification
# •	Create three variables: one integer, one float, and one complex number.
# •	Print each variable and use the type() function to confirm their data types.

a = int(44)
b = float(44.44)
c = complex(2 + 5j)

print(type(a))
print(type(b))
print(type(c))










# Arithmetic with Mixed Types
# •	Create one int variable (a) and one float variable (b).
# •	Print the sum, difference, product, and quotient of a and b.
# •	Print the type() of each result (notice how types may change).
sum = a + b
sum = print("the sum is:",sum,type(sum))
difference = a - b
difference = print("the difference is:",difference, type(difference))
product = a * b
product = print("the product is:",product,type(product))
quotient = a / b
quotient = print("the quotient is:",quotient,type(quotient))










# Comparison Operators
# •	Let x = 10 and y = 7.
# •	Print the results of x > y, x < y, x == y, and x != y.
# •	After observing the output, explain why each result is True or False in comments.
x = 10
y = 7

print((x>y),(x<y),(x == y),(x!=y))
#(x>y) = cames true, clz x is greater than y 
#(x < y)  =came false, clz x in not greater than y
#(x == y)  =came false, cuz x is not equal to y
#(x! == y) = came true, cuz x and y are not equal.







# Boolean Variables
# •	Define a variable status = True.
# •	Print the value of status and confirm it is a boolean using type(status).
# •	Reassign status to False and confirm its type again.
z = 10
status = True
print(type(status))
print (x == y)
print (x == z)








# String Creation and Length
# •	Create a string variable, for example text = "Hello World".
# •	Use len(text) to print its length.
# •	Use type(text) to verify it is a string.

str1 = "Bibek Parajuli"
print(len(str1))
print(type(str1))






# String Indexing
# •	With the string s = "Python", print each character. Then print just the first and last characters usingnegative indexing.
s = "Python"
print(s[-6]),print(s[-1])






# String Slicing
# •	Let lang = "Programming".
# •	Print the substring from index 0 to index 4.
# •	Print the substring from index 3 to the end.
# •	Print the substring that omits the first 2 and last 2 characters.
lang = "Programming"
print(lang[0:4])
print(lang[3:])
print(lang[2:-2])






# Exploring len() on Slices
# •	Continue using lang = "Programming".
# •	Slice lang to get "Program" and store it in a variable part1.
# •	Print len(part1) and comment how it differs from len(lang).
part1 = lang[0:7]
print(len(part1))







# String Methods – Case Conversion
# •	Let phrase = "Hello, Python!".
# •	Print phrase.upper() and phrase.lower().
# •	Print the original phrase to show it remains unchanged (strings are immutable).
phrase = "Hello, Python!"
print("Uppercase: ", phrase.upper())
print("Lowercase: ", phrase.lower())









# Combining Strings
# •	Create two strings, str1 = "Data" and str2 = "Science".
# •	Combine them into a single string with a space in between and print it.
# •	Print the length of the combined string.
str1 = "Data"
str2 = "Science"
print(str1,"",str2)







# In-Place vs. Reassignment with String Methods
# •	Let word = "example".
# •	Call word.upper() but do not store it, then print word.
# •	Now set word = word.upper(), then print word.
# •	Comment on why the second print is different from the first.
word = "example"
word.upper() #python creates neww string but i havent saved it anywhere.
print(word)

word = word.upper() #i said python to create the new string
print(word)










# Arithmetic Operator Precedence
# •	Define a = 5, b = 3, c = 2.
# •	Print the result of the expression a + b * c.
# •	Print the result of (a + b) * c.
# •	In comments, explain how operator precedence affects the outcome.
aa = 5
bb = 3
cc = 3
print(aa+bb*cc)
print((aa+bb)*cc)






# String Index Out of Range
# •	Let text = "Hello".
# •	Attempt to access an index that doesn’t exist, like text[10].
# •	Observe the error message (IndexError) and explain why it happens in comments.
text = "Hello"
# print(text[10]) #it says "string index out of range". text[10] doesnt exit so it cant reach it. Python stops you from accessing undefined memory.








# Equality vs. Identity Check (Conceptual Explanation)
# •	Create two variables with the same string value, s1 = "test" and s2 = "test".
# •	Use the == operator to compare them, then use the is operator.
# •	Explain in comments what each comparison checks
s1 = "test"
s2 = "test"

print(s1 == s2)







# Creating and Checking a Complex Number
# •	Define z = 3 + 4j.
# •	Print the real part (z.real) and the imaginary part (z.imag).
# •	Confirm that its type is complex using type(z).
z = 3 + 4j
print(z.real)
print(z.imag) 
print(type(z))






# Comparisons with Floats
# •	Let f1 = 0.1 + 0.2 and f2 = 0.3.
# •	Print f1 == f2.
# •	Print the actual values of f1 and f2 to explain any difference in the comparison outcome (floating-point precision).
f1 = 0.1 + 0.2
f2 = 0.3

print(f1 == f2)










#------------------------Assignment 2--------------------------------
#Python Data Structures Assignment 

# 1.	Create a List:
# Create a list containing the numbers 1 through 15. Print the list
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(num)







# 2.	List of Strings:
# Create a list of your five favorite fruits. Print the list.
fruits = ["apple", "banana", "cherry", "grapes", "gauva"]
print(fruits)







# 3.	Accessing Elements:
# Given the list [10, 20, 30, 40, 50], print the first and last element using positive and negative indexing.
list = [10, 20, 30, 40, 50]
print(list[0])
print(list[4])
print(list[-1])
print(list[-5])






# 4.    List Length:
# Create a list of any 5 items and print its length using the len() function.
list1 = ["apple", "chair", "table", "monitor", "mouse"]
print(len(list1))






# 5.	Appending Elements:
# Start with an empty list and append the numbers 1, 2, and 3. Print the list.
numbers = []

numbers.append(1)
numbers.append(2)
numbers.append(3)

print(numbers)







# 6.	Inserting an Element:
# Given a list [1, 3, 4], insert the number 2 at the correct position so that the list becomes [1, 2, 3, 4].
numbers1 = [1,3,4]
numbers1.insert(1,2)
print(numbers1)








# 7.	Removing an Element:
# Remove the number 3 from the list [1, 2, 3, 4, 5] using a list method and print the new list.
number2 = [1,2,3,4,5]
number2.remove(3)
print(number2)






# 8.	Popping an Element:
# Given the list [10, 20, 30, 40], pop the last element and print the element and the updated list.
number3 = [10,20,30,40]
number3.pop(-1)
number3 = number3
print(number3)





# 9.	Slicing a List:
# Given the list [0, 1, 2, 3, 4, 5], print a slice that contains the elements from index 2 to 4.
number4 = [0, 1, 2, 3, 4, 5]
print(number4[2:5])








# 10.	List Concatenation:
# Concatenate two lists, e.g., [1, 2, 3] and [4, 5, 6], and print the resulting list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
print(result)






# 11.	Repeating a List:
# Create a list [1, 2] and print the list repeated three times.
number5 = [1,2]
repeated_list = number5*3
print(repeated_list)



# 12.	Copying a List:
# Create a copy of a given list and print both the original and the copy.
number6 = [1,2]
number6_copy = number6
print(number6)
print(number6_copy)






# 13.	Clearing a List:
# Given any list, use a method to clear all its elements and then print the empty list.
list3 = ["hello", "cow", "hippo", "classroom","school"]
list3.clear()
print(list3)





#-------------------------------Section 2: Tuples--------------------------------
# 1.	Create a Tuple:
# Create a tuple containing the numbers 1, 2, and 3. Print the tuple.
tuple1 = (1,2,3)
print(tuple1)




# 2.	Tuple of Strings:
# Create a tuple of three different color names and print it.
tuple2 = ("car", "cat", "dog")
print(tuple2)





# 3.	Accessing Tuple Elements:
# Given the tuple (10, 20, 30, 40), print the second element.
tuple3 = (10,20,30,40)
print(tuple3[1])




# 4.	Tuple Slicing:
# Using the tuple (0, 1, 2, 3, 4), print a slice that contains elements from index 1 to 3.
tuple4 = (0, 1, 2, 3, 4)
print(tuple4[1:4])





# 5.	Concatenating Tuples:
# Concatenate two tuples, e.g., (1, 2) and (3, 4), and print the result.
tuple5 = (1,2)
tuple6 = (3,4)
print((tuple5)+(tuple6))






# 6.	Tuple Unpacking:
# Store the tuple ("Alice", 25, "New York") into three variables and print them.
tuple7 = ("Alice", 25, "New York")
name, age, city = tuple7
print(name, age, city)





# 7.	Convert List to Tuple:
# Convert the list [1, 2, 3, 4] into a tuple and print the tuple.
list4 = [1, 2, 3, 4]
tuple8 = tuple(list4)
print(type(tuple8))
print(tuple8)





# 8.	Counting Occurrences:
# Given the tuple (1, 2, 2, 3, 2), count how many times the number 2 appears.
tuple9 = (1, 2, 2, 3, 2)
tuple10 = num.count(2) 
print(tuple10)




# 9.	Finding an Index:
# In the tuple (10, 20, 30, 40), find the index of the element 30 and print it.
tuple11 = (10, 20, 30, 40)
tuple12 = tuple11.index(30)
print(tuple12)





#-----------------------------Assignment 3 --------------------------------------------------------------

# Integer & Float Mix
# •	Create an integer a and a float b.
# •	Perform addition, subtraction, multiplication, and division on them.
# •	Print the results and observe the type of each result with type().
aaa = int(20)
bbb = float(20)
print("addition:",aaa+bbb, "Subtraction:",aaa-bbb,"Multiplication:",aaa*bbb,"division:",aaa/bbb)







# Large Integers & Type
# •	Assign a very large integer to a variable (e.g., in the billions).
# •	Print it and confirm its type is still int in Python or not.
billion = 9999999999999999999999999999999999999999999
print(type(billion))







# Complex Number Basics
# •	Create a complex number z = 3 + 4j.
# •	Print its real part, imaginary part, and confirm its type is complex.
# •	Perform a basic arithmetic operation with another complex number (e.g., (3 + 4j) + (1 + 2j)).
z = 3+4j
print((4+4j)+(1+2j))






# Boolean from Comparisons
# •	Create two variables, m = 10 and n = 15.
# •	Define status = (m > n) and print status.
# •	Confirm type(status) is bool.
# •	Assign status = (m != n) and print again.
m = 10
n = 15
status = (m>n)
print(status)
print(type(status))
status = ( m != n)
print(status)




#String Creation & Indexing
# •	Create a string text = "HelloWorld".
# •	Print the first and last characters using positive and negative indexing.
# •	Comment on the total length of the string.
text1 = "helloworld"
firstp = text1[0]      
firstn = text1[-10]    

lastp = text1[9]      
lastn = text1[-1]     
print(f"First character (positive): {firstp}")
print(f"First character (negative): {firstn}")
print(f"Last character (positive): {lastp}")
print(f"Last character (negative): {lastn}")



# String Slicing
# •	With lang = "PythonProgramming", print the substring from index 2 to 8.
# •	Print the substring from the start up to index 5.
# •	Print the entire string in reverse using slicing.
lang2 = "PythonProgramming"
sub = lang2[2:8]
subb = lang[:5]
rever = lang[::-1]

print(f"Substring (2 to 8): {sub}")
print(f"Substring (start to 5): {subb}")
print(f"Reversed string: {rever}")








# String Methods
# •	Let phrase = " Hello, Python World! ".
# •	Demonstrate strip(), upper(), and replace() on this string.
# •	Print the results and comment on immutability of strings in Python.
phrase = "  Hello, Python World!  "
str77 = phrase.strip()
uppe = str77.upper()
replaced = uppe.replace("PYTHON", "CODING")

print(f"Original: '{phrase}'")
print(f"Stripped: '{str77}'")
print(f"Uppercase: '{uppe}'")
print(f"Replaced: '{replaced}'")










# String Formatting
# •	Create two variables: name = "Rajesh" and score = 95.
# •	Print: "Alice scored 95 points." using two methods (concatenation and an f-string or str.format()).
raje = "Rajesh"
score = 95
print(raje + " scored " + str(score) + " points.")
print(f"{raje} scored {score} points.")






# Boolean Operations in Expressions
# •	Write a small expression using and, or, and not with boolean values.
# •	Example: result = not(True and False) or (5 > 3).
# •	Print result and explain how Python evaluated the expression.
# Boolean expression
# Evaluates: not(True and False) or (5 > 3)
resultt = not(True and False) or (5 > 3)
print(f"The result of the expression is: {resultt}")







# List Creation & Access
# •	Create a list of 5 different integers.
# •	Print the first item, middle item, and last item using indexing.
 # Create a list of 5 integers
number7 = [10, 25, 40, 55, 70]
first_item = number7[0] 
middle_item = number7[2] 
last_item = number7[4]  

print(f"First item: {first_item}")
print(f"Middle item: {middle_item}")
print(f"Last item: {last_item}")







# List Slicing
# •	Given letters = ["a", "b", "c", "d", "e"], print the slice that contains only ["b", "c", "d"].
# •	Print the slice that omits the first and the last element.
letters = ["a", "b", "c", "d", "e"]
slice_bcd = letters[1:4]
slice_omitted = letters[1:-1]
print(f"Slice ['b', 'c', 'd']: {slice_bcd}")
print(f"Slice omitting first and last: {slice_omitted}")






# Sorting & Reversing
# •	Create a list of random integers.
# •	Sort the list in ascending order and print it.
# •	Reverse the sorted list and print again.
# Create a list of integers manually
numbers3 = [42, 7, 89, 15, 33]
print(f"Original list: {numbers3}")

numbers3.sort()
print(f"Sorted list: {numbers3}")

numbers3.reverse()
print(f"Reversed list: {numbers3}")







# Combining Lists
# •	Let list1 = [1, 2, 3] and list2 = [4, 5, 6].
# •	Combine them into a single list and print.
# •	Demonstrate two ways: using + and using .extend().
list5 = [1, 2, 3]
list6 = [4, 5, 6]

# Method 1: Using the '+' operator
# This creates a brand new list and leaves the originals unchanged
combined_plus = list5 + list6

# Method 2: Using the .extend() method
# This modifies 'list1' directly (in-place)
list5.extend(list6)

print(f"Result using +: {combined_plus}")
print(f"Result using .extend(): {list5}")






# # Aggregating List Values
# # •	Create a list of floats, e.g., [2.5, 3.6, 1.2, 5.0].
# # •	Print the sum, minimum, and maximum of that list using built-in functions.
# values8 = [2.5, 3.6, 1.2, 5.0]

# total_sum = sum(values8)
# min_val = min(values8)
# max_val = max(values8)

# print(f"List: {values8}")
# print(f"Sum: {total_sum}")
# print(f"Minimum: {min_val}")
# print(f"Maximum: {max_val}")







# Tuple Creation
# •	Create a tuple t = (10, 20, "Hello", True).
# •	Print the tuple and confirm its type with type(t).
# Create a tuple containing mixed data types
t = (10, 20, "Hello", True)
print(f"Tuple: {t}")
print(f"Type: {type(t)}")






# Tuple Indexing & Slicing
# •	Print the first two elements of t using slicing.
# •	Print the last element of t using negative indexing.
t1 = (10, 20, "Hello", True)
print(f"First two elements: {t1[:2]}")
print(f"Last element: {t1[-1]}")






# Tuple Unpacking
# •	Suppose t2 = ("Tom", 25, "Engineer").
# •	Unpack it into three separate variables: name, age, profession.
# •	Print these variables individually.
# Create the tuple
t2 = ("Tom", 25, "Engineer")
name, age, profession = t2
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")





# Attempt Tuple Mutation
# •	Try to change an element of t (t[0] = 999) and observe the error.
# •	In comments, explain why the error occurs.
tt = (10, 20, "Hello", True)
try:
    tt[0] = 999
except TypeError as ee:
    print(f"Error caught: {ee}")  #Error caught: 'tuple' object does not support item assignment






# Set Creation & Membership
# •	Create a set my_set = {1, 3, 5, 7}.
# •	Check if 5 is in my_set.
# •	Check if 2 is not in my_set.
# Create a set
my_set = {1, 3, 5, 7}
is_five_present = 5 in my_set
is_two_absent = 2 not in my_set
print(f"Set: {my_set}")
print(f"Is 5 in my_set? {is_five_present}")
print(f"Is 2 not in my_set? {is_two_absent}")






# Add & Remove Elements
# •	Add 9 to my_set.
# •	Remove 3 from my_set.
# •	Print the updated set.
# Create the set
my_set = {1, 3, 5, 7}
my_set.add(9)
my_set.remove(3)
print(f"Updated set: {my_set}")






# Set Operations
# •	Create two sets: setA = {1, 2, 3} and setB = {3, 4, 5}.
# •	Print the union, intersection, and difference (setA - setB).
setA = {1, 2, 3}
setB = {3, 4, 5}

union_set = setA | setB 
intersection_set = setA & setB  
difference_set = setA - setB  

print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference (setA - setB): {difference_set}")







# Check Unique Values
# •	Define a list vals = [1, 2, 2, 3, 3, 3, 4].
# •	Convert it to a set.
# •	Print both the list and the set to show how duplicates are removed.
# Define a list with duplicate values
vals = [1, 2, 2, 3, 3, 3, 4]
unique_vals = set(vals)
print(f"Original list: {vals}")
print(f"Converted set: {unique_vals}")







# Frozenset Creation
# •	Create a frozenset from a list [2, 4, 4, 6].
# •	Print it and observe whether duplicates are preserved.
# Create a list with duplicates
my_list = [2, 4, 4, 6]
frozen = frozenset(my_list)

print(f"Original list: {my_list}")
print(f"Frozenset: {frozen}")






# Operator Precedence
# •	Define a = 4, b = 2, c = 5.
# •	Print the result of a + b * c vs. (a + b) * c.
# •	Explain in comments how the result differs.
aaaa = 4
bbbb = 2
cccc = 5

# Expression 1: Standard precedence
# Multiplication (*) is performed before addition (+)
result1 = aaaa + bbbb * cccc

# Expression 2: Forced precedence
# Parentheses () are evaluated first, overriding standard rules
result2 = (aaaa + bbbb) * cccc

print(f"Result of a + b * c: {result1}")
print(f"Result of (a + b) * c: {result2}")







# Modulo & Floor Division
# •	Let x = 17 and y = 4.
# •	Print x % y and x // y.
# •	Explain the difference between these two operators in comments.
xx = 17
yy = 4

remainder = xx % yy

quotient = xx // yy

print(f"17 % 4 = {remainder}")
print(f"17 // 4 = {quotient}")
