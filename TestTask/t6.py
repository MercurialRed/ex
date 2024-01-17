# input: [1, 2, 4, 6, 9, 11, 12, 13, 15, 17, 20]
# output: [3, 5, 7, 8, 10, 14, 16, 18, 19]

def show_missing_elements(data):
    x = []
    for num in range(min(data), max(data)+1):
        x.append(num)
    return set(x).difference(data)


input_list = [1, 2, 4, 6, 9, 11, 12, 13, 15, 17, 20]
result = show_missing_elements(input_list)
print(f'Result is: {result}')