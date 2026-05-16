input_userName = input("Enter the user name: ")

if(len(input_userName) < 10):
    print("username is less than 10 characters please enter a username with more than 10 characters")
else:
    print("username is greater than 10 characters username is valid")