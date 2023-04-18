# by default, a file is opened is read mode
readmeFile = open("readme.txt", "r") # gets loaded into the memory

print(readmeFile.readline(9))

# readmeFile.write("I appended something to this file")

readmeFile.close()

# readmeFile.write("I tried to do it after file is closed")

# Other lines of code