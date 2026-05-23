# python function 
def greeting():
    print("Hello, World!")

greeting() 

def greetings(name):
    print(f"Hello, {name}")

greetings("adarsh")

def greetings(name,age):
    return f"Hello, {name} and you are {age} years old"

_value =greetings("adarsh", 20)
print(_value)



def add(a,b,c):
    return a+b+c/3
  
_value =add(1,2,3)
print(_value)

def check_draving_age(age):
    if age>=18:
        print("yes you are eligible for driving license")
    else:
        print("no you are not eligible for driving license")
check_draving_age(15)

def show_numbers(numbers):
    for i in range(numbers):
        print(i)
show_numbers(10)


def total_sum(num):
    sum=0
    for i in num:
        sum+=i
        print(sum)
total_sum([1,2,3,4,5,6,7,8,9,10])


