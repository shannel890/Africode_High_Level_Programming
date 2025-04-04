# with open("output.txt",'r') as h: # with ensure that the file is safely closed and opened after the execution is complete.
#     with open("kirui.txt",'w') as e:
#         for data in h:
#             e.write(data)

# with open("kirui.txt", "a") as e:# "a" for append has to be specified to ensure it is appended.
#     e.write("this is very important\n")# type write to append a statement to a text. 

# with open("kirui.txt", "r") as e:
#     for data in e:
#         print(data, end="")

# with open("output.txt", "r") as f:
#     print("File Descriptor:", f.fileno())#.is a unique integer that identifies an open file in the operating system.

# import os

# with open("kirui.txt", "rb") as f:
#     slr = f.fileno()
#     data = os.read(slr, 200)  # Read 200 bytes,contols the amount of bytes for the system to output.
#     print(data)

# with open("kirui.txt", "r") as f:# isatty is used to check if a file is connected to a file.zz
#     print(f.isatty())  # False → it's a file, not a terminal

#     f.truncate #is used to cut off a file at a certain point or clear a file by truncating it to size.

#     f.reconfigure # is used to change the file descriptor's configuration, such as changing the encoding or buffering settings.it is available on text-mode on file objects to dynamically change the file's encoding and buffering settings.

#write mode 
# with open("output.txt",'w') as f: 
#     f.write("this is a test")
#read mode
# with open("output.txt","r") as t:
#     print(t.read())

#create mode
# with open("time.txt","x") as d:
#     d.write("this is a test")
# append mode
with open("output.txt","a") as g:
    g.write("this is awesome")



