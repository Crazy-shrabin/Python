# f = open("demo.txt", "a")

# data = f.write("I am gonna fuck every one of you.")
# print(data)

# f.close()

# f = open("demo.txt", "r+")
# f.write("boka")

# print(f.read())
# f.close()


#with syntax
# with open("demo.txt", "r") as a:
#     element = a.read()
#     print(element)

import os
os.remove("demo.txt")
