#File input and output

#open() function
#read ,write ,append
#close() function

#synthax
# open('file','mode')

#mode
# r : read -open a file for reading - file must exist
# w : write -create a file if it does not exist,or overrides the content if it does exists
# a : append - create a file if it does not exist,or appends the content if it does exists to the end of the file
# r+ : read and write -open a file for reading and writing - file must exist
# w+ : write and read -create a file if it does not exist,or overrides the content if it does exists and open for reading
# b : binary -open a file in binary mode


# read mode
# f = open("test.txt","r")
# print(f.readline())
# print(f.read())
# f.close # read the entire file

# write mode
f = open("output.txt","w")
# f.write("this is a test file.")
f.write("this contents will overwrite the existing content.")

#  ***************append mode*************
# f = open("output.txt","a")
# f.write("this content will be added to the end of the file.")
# f.close

#binary mode
p = open('img3.jpg','rb')
# print(p)
#copy image
# for data in p:
#     open('copy.jpg','wb').write(data)
# p.close()

# import os

# if os.path.exists('img3.jpg'):
#     with open('img3.jpg', 'rb') as p:
#         with open('copied.jpg', 'wb') as k:
#             for data in p:
#                 k.write(data)
# else:
#     print("Error: 'img3.jpg' does not exist.")

# with open('img3.jpg','rb')as p:
#     for data in p:
#         with open('copied.jpg','wb')as k:
#             k.write(data)


