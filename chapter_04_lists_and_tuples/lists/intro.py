# A list stores multiple values in one variable.
# Python Lists vs Tuples
# List: ordered, mutable (can change)
# Tuple: ordered, immutable (cannot change)

friends = ["harry", "orange", 5, 0.5 , False, 'Adarsh']
friends.reverse()
print('friends',friends)
# friends[0] = "rohan"
print(friends[0])
print(friends[1:4])

# friends.append('apple')
print(friends)
friends.pop(1)
print(friends)
print(friends.count('Adarsh'))
print(friends.index('Adarsh'))



list = [1,2,3,4,5,6,7,8,9,10]

list.sort()
print('list',list)