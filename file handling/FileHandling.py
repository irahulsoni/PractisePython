
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     'U'       universal newline mode (deprecated)
#     'rb'      read binary (images)
#     'wb'      write binary (images)
#     ========= ===============================================================
#

file = open('MyData', 'r')

file2 = open('abc', 'w')

img = open('image.jpg','rb')

# read whole file
print(file.read())

# will only print the whole file if we use read and readline togrther
# read only one line
# print(file.readline(), end='#')

# to write the file
# file.write("Something to write in the File")

# using loop to write the data
for data in file:
    file2.write(data)

# working with the image, As we don't have data in image, we only have binary format
print(img.read())
