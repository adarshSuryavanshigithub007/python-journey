

a1=int(input("Enter the first number: "))
a2=int(input("Enter the second number: "))
a3=int(input("Enter the third number: "))

if(a1>a2 and a1>a3):
    print("a1 is the greatest number")
elif(a2>a1 and a2>a3):
    print("a2 is the greatest number")
elif(a3>a1 and a3>a2):
    print("a3 is the greatest number")
else:
    print("all the numbers are equal")