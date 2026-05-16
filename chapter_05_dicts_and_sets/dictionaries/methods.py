# update

marks={
    "key":'value',
    "adarsh":100,
    "harry":55,
    "rohan":23
}
#ITEM
# print(marks.items())

#KEY
# print(marks.keys())

#VALUE
# print(marks.values())

#UPDATE
# marks.update({'adarsh':80,"renuka":89})

# print(marks)

# get
# print(marks.get('harry'))

#POP
# print(marks.pop('rohan'))

# setdefault() ONLY IF KEY MISSING 
# print(marks.setdefault('adarh',100))
# print(marks.setdefault('satish',78))
# print(marks)

# copy
marks2=marks.copy()
marks2['adarsh']=5
print(marks2)
print(marks)

# in — Check if key exists

print('goa' in marks)


