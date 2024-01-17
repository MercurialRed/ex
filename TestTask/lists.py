# Exercise 1: Reverse a list in Python
'''list1 = [100, 200, 300, 400, 500]
print(list1[::-1])'''

# Exercise 2: Concatenate two lists index-wise
'''list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

result = [i + j for i, j in zip(list1, list2)]
print(result)'''

# Exercise 3: Turn every item of a list into its square
'''numbers = [1, 2, 3, 4, 5, 6, 7]
result = [i*i for i in numbers]
print(result)'''

# Exercise 4: Concatenate two lists in the following order
'''list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = [i + j for i in list1 for j in list2]
print(result)'''

# Exercise 5: Iterate both lists simultaneously
'''list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)'''

# Exercise 6: Remove empty strings from the list of strings
'''list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list1 = [x for x in list1 if x != ""]
print(list1)'''

# Exercise 7: Add new item to list after a specified item
'''list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2, 7000)
print(list1)'''

# Exercise 8: Extend nested list by adding the sublist
'''list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
for i in sub_list:
    list1[2][1][2].append(i)
print(list1)'''

# Exercise 9: Replace list’s item with new value if found
'''list1 = [5, 10, 15, 20, 25, 50, 20]
for i in list1:
    if i == 20:
        idx = list1.index(i)
        list1[idx] = 200
        break
print(list1)'''

# Exercise 10: Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]
list1 = [x for x in list1 if x != 20]
print(list1)