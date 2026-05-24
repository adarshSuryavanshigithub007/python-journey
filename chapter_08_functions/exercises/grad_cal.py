# Refactor your grade calculator from chapter 06 into a function

def grade(marks):
    if marks>=90:
        print("A")
    elif marks>=80:
        print("B")
    elif marks>=70:
        print("C")
    elif marks>=60:
        print("D")
    else:
        print("F")
grade(95)