
# 90-100 => EX
# 80-90 => A
# 70-80 => B
# 60-70 => C
# 50-60 => D
# <50 => F

subject1 = int(input("Enter the marks of subject 1: "))
subject2 = int(input("Enter the marks of subject 2: "))
subject3 = int(input("Enter the marks of subject 3: "))
subject4 = int(input("Enter the marks of subject 4: "))
subject5 = int(input("Enter the marks of subject 5: "))
subject6 = int(input("Enter the marks of subject 6: "))

total_marks = subject1 + subject2 + subject3 + subject4 + subject5 + subject6
percentage = (total_marks / 600) * 100

if percentage >= 90:
    print("Grade: EX your percentage is ", percentage)
elif percentage >= 80:
    print("Grade: A your percentage is ", percentage)
elif percentage >= 70:
    print("Grade: B your percentage is ", percentage)
elif percentage >= 60:
    print("Grade: C your percentage is ", percentage)
elif percentage >= 50:
    print("Grade: D your percentage is ", percentage)
else:
    print("Grade: F your percentage is ", percentage)