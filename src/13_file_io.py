"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# open() returns a file object, and is most commonly used with two arguments:
# open(filename, mode)
# ======== modes can be: ========
# "r" when the file will be only read
# "w" for only writing - an existing file with the same name will be erased
# "a" opens the file for appending and any data written to the file is automatically added to the end
# "r+" opens the file for both reading and writing

# adding with -> with open("filename", "mode") so that the file is properly closed when done.

# YOUR CODE HERE
f = open("foo.txt", "r")
for line in f:
    print(line, end="")

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
b = open("bar.txt", "w")
b.write("First line \n")
b.write("Second line \n")
b.write("Third line \n")