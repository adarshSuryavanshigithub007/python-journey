def gretestNum(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print("num1 is the greatest number")
    elif(num2>num1 and num2>num3):
        print("num2 is the greatest number")
    elif(num3>num1 and num3>num2):
        print("num3 is the greatest number")
    else:
        print("all the numbers are equal")
gretestNum(1,2,3)
