# write program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. assume 3 subjects and take marks as an input from the user.

subject1 = int(input("Enter the marks of subject mathematics: "))
subject2 = int(input("Enter the marks of subject physics: "))
subject3 = int(input("Enter the marks of subject chemistry: "))

total_marks = subject1 + subject2 + subject3
percentage = (total_marks / 300) * 100
print(percentage)

if(percentage >=40 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33):
    print("congratulations hurray you are passed with percentage of ",percentage)
else:
    print("You are failed with percentage of ",percentage," better luck next time")
