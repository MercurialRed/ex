'''SUM OF LIST ELEMENTS
def sum_of_elements(data):
    return sum(test_subject)

input_list = [1, 2, 3, 4]
result = sum_of_elements(input_list)
print(result)'''

'''LIST REVERSED
def list_reversed(data):
    return test_subject[::-1]

input_list = [1, 2, 3, 4]
result = list_reversed(input_list)
print(result)'''

'''EVEN NUMBERS
def even_numbers(data):
    even_list = []
    for x in data:
        if x % 2 == 0:
            even_list.append(x)
    return even_list

input_list = [1, 2, 3, 4]
result = even_numbers(input_list)
print(result)'''

'''LIST COMPREHENSION
def list_comprehension(data):
    return [x**2 for x in data]

input_list = [1, 2, 3, 4]
result = list_comprehension(input_list)
print(result)'''

'''LIST MANIPUALTION
def list_manipulation(data1, data2):
    return list(set(data1 + data2))

input_list1 = [1, 2, 3, 4]
input_list2 = [1, 2, 5, 6]
result = list_manipulation(input_list1, input_list2)
print(result)'''

'''TUPLE UNPACKING
def tuple_unpacking(data):
    x, y, z = data
    return x, y, z

input_tuple = (1, 2, 3)
result = tuple_unpacking(input_tuple)
print(result)'''

'''IMMUTABLE OPERATIONS
def immutable_opperations(data):
    data[0] = 4
    return data

input_tuple = (1, 2, 3)
result = immutable_opperations(input_tuple)
print(result)'''

'''SET INTERSECTION
def set_intersection(data1, data2):
    return data1.intersection(data2)

input_set1 = {1, 2, 3, 4, 5}
input_set2 = {2, 1, 6, 8, 5}
result = set_intersection(input_set1, input_set2)
print(result)'''

'''SET OPERATIONS
def set_operations(data1, data2):
    set_union = data1.union(data2)
    set_intersection = data1.intersection(data2)
    set_difference = data1.difference(data2)
    return set_union, set_intersection, set_difference

input_set1 = {1, 2, 3, 4, 5}
input_set2 = {2, 1, 6, 8, 5}
result = set_operations(input_set1, input_set2)
print(result)'''


#
#  RETURN
#
'''SET COMPREHENSION
def set_comprehension(data):
        return data

input_set = {1, 2, 3, 4, 5}
result = set_comprehension(input_set)
print(result)

DICTIONARY CREATION
def dictionary_creation(data1, data2):
    a = {}
    b = []
    for value in data2:
        b.append(value)
        b.
    for key in data1:
        a[key] = b
    return a

input_keys = ("a", "b", "c", "d", "e")
input_values = (1, 2, 3, 4, 5)
result = dictionary_creation(input_keys, input_values)
print(result)

DICTIONARY MANIPULATION
def dictionary_manipulation(data1, data2):
    a = {}
    for key in data1:
        for value in data2:
            a[key] = value
    return a


input_keys = ("a", "b", "c", "d", "e")
input_values = (1, 2, 3, 4, 5)
result = dictionary_manipulation(input_keys, input_values)
print(result)'''