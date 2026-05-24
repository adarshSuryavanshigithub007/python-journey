file = open('chapter_09_file/read/example.txt','w')
print(file.read())
file.write("adarsh is good boy\n")
file.close()


# read and write 
file = open('chapter_09_file/read/example.txt','r+')
print(file.read())
file.write("adarsh is good boy\n")
file.close()

# read lines 
file = open('chapter_09_file/read/example.txt','r')
lines = file.readlines()
print(lines)
file.close()