friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Harry")
print(friends)

l1 = [1, 34,62, 2, 6, 11]

l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
print(l1)

value = l1.pop(3)
print(value)
print(l1)

l1.remove(1) #1 in particular value not a index
print(l1)