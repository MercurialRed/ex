# Exercise 1: Create a list by picking an odd-index items from the first list
# and even index items from the second
'''l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

r1 = [x for x in l1 if l1.index(x)%2==1]
r2 = [x for x in l2 if l2.index(x)%2==0]
print(r1)
print(r2)'''

# Exercise 2: Remove and add item in a list
'''list1 = [54, 44, 27, 79, 91, 41]
idx = 4
num = list1[idx]
list1 = [x for x in list1 if list1.index(x)!=idx]
print(list1)
list1.insert(2, num)
print(list1)
list1.append(num)
print(list1)'''

# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
'''sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk1 = [i for i in sample_list[2::-1]]
chunk2 = [i for i in sample_list[5:2:-1]]
chunk3 = [i for i in sample_list[8:5:-1]]
print(chunk1, chunk2, chunk3)'''

# Exercise 4: Count the occurrence of each element from a list
'''sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

num = dict.fromkeys(set(sample_list))
num.update(map(lambda num: (num, sample_list.count(num)), num))
print(num)'''

# Exercise 5: Create a Python set such that it shows the element from both lists in a pair
'''first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
result = set(zip(first_list, second_list))
print(result)'''

# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
'''first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

intersection = first_set.intersection(second_set)
print(intersection)
first_set = first_set - intersection
print(first_set)'''

# Exercise 7: Checks if one set is a subset or superset of another set.
# If found, delete all elements from that set
'''first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
first_set = set([first_set.clear() if first_set.issubset(second_set) else first_set])
second_set = second_set.clear() if second_set.issubset(first_set) else second_set
print(first_set, second_set)'''

# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary.
# If not, delete it from the list
'''roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
result = [i for i in roll_number if i not in sample_dict.values()]
print(result)'''

# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
'''speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52,
         'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
result = list(set(speed.values()))
print(result)'''

# Exercise 10: Remove duplicates from a list and create a tuple
# and find the minimum and maximum number
'''sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
result = tuple(set(sample_list))
min = min(result)
max = max(result)
print(result, min, max)'''


