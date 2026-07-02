# count = 1
# while count <=5 :
#     print("hello")
#     count = count + 1 #count +=1

# print(count)






# count = 10
# while count >= 0:
#     print ("laaa")
#     count -= 1







# a = 1
# while a <= 100:
#     print(a)
#     a += 1







# b = 100
# while b >= 1:
#     print(b)
#     b -= 1








# d = int(input("enter the number: "))
# c = 1
# while c <= 10:
#     print( d* c)
#     c += 1





# collection = set()

# collection.add(2)
# collection.add(1)
# collection.add(3)
# collection.add(5)
# collection.add(4)
# collection.add(6)


# collection.remove(6)


# print(collection)





# d=int(input("enter the number: "))
# c = 1000
# while c>=1:
#     print (c)
#     c -= 1
# print("loop ended")






# a = 100
# while a>=1:
#     print(a)
#     a -= 1



# a = int(input("Enter the number: "))
# b = 1
# while b <= 10:
#     print(a*b)
#     b += 1
# print("loop ended")



# num = [1,4,9,16,25,36,49,64,81,100]
# idx = 0

# while idx < len(num):
#     print(nums[idx])
#     idx += 1



# fru = ["apple", "banana", "cherry", "doe fruit", "Elichi", "fruits", "grapes"]
# idx = 0

# while idx < len(fru):
#     print(fru[idx])
#     idx += 1



# classes = ["ani", "bibek", "milan"]
# idx = 0
# while idx < len(classes):
#     print(classes[idx])
#     idx += 1
# print("loop ended")




# family = ["baba", "mummy", "didi", "ma"]
# idx = 0
# while idx < len(family):
#     print(family[idx])
#     idx += 1
# print("loop ended")




# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 36
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("found")
#     i += 1




# i = 1
# while i <= 10:
#     print(i)
#     if (i == 3):
#         break
#     i += 1
# print("end of loop!")



# num = (1,2,3,4,5,6,7,8,9,10)
# x = 6
# i = 0

# while i <= len(num):
#     if(num[i] == x):
#         print("Found at idx",i)
#         break
#     else:
#         print("finding...")
#     i += 1

# print("End of loop!")


# i = 0
# while i <= 10:
#     if(i == 5):
#         i += 1
#         continue
#     print(i)
#     i += 1


# i = int(input("enter the number: "))

# while i <= 10:
#     if(i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1



nums = (1,4,9,16,25,36,49,64,81,100,49)
x = 49

idx = 0

for el in nums:
    if (el == x):
        print("Found", idx) 
        break
    idx += 1
  