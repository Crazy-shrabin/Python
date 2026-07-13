# i = 1
# while i <= 8:
#     if (i%2 == 0):
#         print("This number is even: ",i)        
#     else:
#         print("This number is odd:  ",i)
#     i += 1

# i = 0
# while i <= 10:
#     if (i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1


# nums = "bibek"
# for val in nums:
#     if( val == 'e'):
#         print("e found")
#         break
#     print(val)
# else:
#     print("parajuli")


# nums = [1,4,9,16,25,36,49,64,81,100]
# for el in nums:
#     print(el)


# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 16)
# x = 16
# idx = 0
# for tup in nums:
#     if (tup == x):
#         print("this num has been found at idx: ",idx)
#     idx += 1



# for el in range(1, 101, 1):
#     print(el)
   
# n = int(input("Enter the number: "))
# for e in range(1, 11):
#     print(n * e)

n = 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum= ", sum) 