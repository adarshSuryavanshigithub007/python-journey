with open('write.txt','w') as file:
    file.write("hey adarsh how are you")
    file.close()

with open('write.txt','r') as file:
    print(file.read())