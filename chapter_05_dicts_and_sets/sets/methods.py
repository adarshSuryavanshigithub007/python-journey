# 1️⃣ add() — Add one element
# a={'a','b','c','d'}
# a.add('e')
# print(a)

# 2️⃣ update() — Add multiple elements
# a.update(['f','g'])
# print(a)

# remove
# a.remove('b')
# print(a)

# union() — Combine two sets
a = {1, 2, 3}
b = {3, 4, 5}
# print(a|b)

# intersection() — Common elements only
# print(a&b)

# 9️⃣ difference() — Elements in a but not in b
# print(a-b) #(a-b)
# print(b-a)

# symmetric difference Elements in A or B, but not in both.
# print(a^b)

# print(a.issubset(b))
# print(b.issubset(a))
# print(a.issuperset(b))
# # print(a.remove('b'))
# print(a.discard('b'))

#  keep only common
a.intersection_update(b)
print(a)
a.symmetric_difference_update(b)
print(a)
