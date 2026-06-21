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






5.	Appending Elements:
Start with an empty list and append the numbers 1, 2, and 3. Print the list.



























