"""
    Python makes performing file I/O simple. Take a look
    at how to read and write to files here:

    https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

"""
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
import os
import sys

with open(os.path.join(sys.path[0], "foo.txt"), "r") as f:
    print(f.read())
# f = open("foo.txt", "rt")
# print(f.read())
# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
f = open("bar.txt", 'w')

for num in range(3):
    f.write(f"some abbt content {num} \n")
# with open(os.path.join(sys.path[0], "bar.txt"), "w") as f:
#     f.write("Write three lines of arbitrary content to that file")
# YOUR CODE HERE
