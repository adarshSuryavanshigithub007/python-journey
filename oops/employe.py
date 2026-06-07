class Employee:
    salary = 1000 # this is class attribute, it is shared by all the instances of the class
    name = "harry"

result = Employee()
result.salary = 2000 # this is instance attribute, it is unique for each instance of the class
print(result.salary)
print(result.name)