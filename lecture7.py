# File i/o in python 
# python can be used to perform operations on a file ,( read & write data)

# Type of all files
# 1.text files: txt, docs, log etc.
# 2.Binary files: .mp4, .mov, .png, .jpeg etc.


# open read and close files
# we have to open a file before reading or white.
# f = open("file_name", "mode")

# sample.txt              r: read mode
# demo.docx               w: write mode

# data = f.read()
# f.close()

# f = open("demo.txt", "r")
# data1 = f.readline()
# print(data1)
# print(type(data1))
# f.close()

#reading a file 
# data = f.read()  --> reads entire file
# data = f.readline() --> reads one line at a time

# f = open("demo.txt", "a")
# f.write("\ni am 21")
# f.close()

# f = open("demo.txt", "r+")
# f.write("hello\n")
# print(f.read())
# f.close

# 'r' --> open for reading
# 'w' --> open for writing, trancating the file first
# 'x' --> create a new file and open it for writing
# 'a' --> open for writing, appending to the end of the file if it exists
# 'b' --> binary mode
# 't' --> text mode(default)
# '+' --> open a disk file for updating (reading and writing)

# with open("demo.txt", "r") as read:
#     data = read.read()
#     print(data)
   

# with open("demo.txt", "w") as writinggg:
#     writinggg.write("hello shaktiman")
#     print(writinggg)









# ------------------------------------------------------------
# Deleting the file
# using the os module
# Module(like a code library) is a file written by another programmer that generally has a function that we can use.UserWarning

# import os
# os.remove( filename )




# with open("removing.txt", "w") as removing:
#     removing.write("hello world!")

# import os
# os.remove("removing.txt")



# with open("pratice.txt", "r") as p:
#     data = p.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

    


with open("Oops_lecture_7.py", "w") as Oops:
    Oops.write("Oops")
    print(Oops)