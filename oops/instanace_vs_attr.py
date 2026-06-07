class Employee:
    salary = 1000 # this is class attribute, it is shared by all the instances of the class
    name = "harry"

result = Employee()

result.salary = 2000 # this is instance attribute, it is unique for each instance of the class 
print(result.salary)

# why salary 2000 is showing instead of 1000?
# because we have created a new instance of the class and assigned a new value to the salary attribute.
# so the instance attribute is overriding the class attribute.
# so the instance attribute is unique for each instance of the class.
# so the instance attribute is unique for each instance of the class.
