# input: [1, 2, 4]
# output: [3]

# input: [1, 2, 4, 6, 9, 11, 12, 13, 15, 17, 20]
# output: [3, 5, 7, 8, 10, 14, 16, 18, 19]


def show_missing_elements(test_list):
    output_list = []
    min_element = min(test_list)
    max_element = max(test_list)

    for element in range(min_element, max_element+1):
        if element not in test_list:
            output_list.append(element)
    return output_list


input_list = [1, 2, 4, 6, 9, 11, 12, 13, 15, 17, 20]
result = show_missing_elements(input_list)
print(f'Result is: {result}')