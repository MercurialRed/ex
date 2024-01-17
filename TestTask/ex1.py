# Task 1.
# input: [1, 2, 4]
# output [3]

# input [1, 2, 4, 6, 7, 8, 10, 12, 17, 20]
# output [3, 5, 9, 11, 13, 14, 15, 16, 18, 19]

def missing_numbers(input_num):
    output_num = []
    min_number = min(input_num)
    max_number = max(input_num)

    for number in range(min_number, max_number + 1):
        if number not in input_num:
            output_num.append(number)

    return output_num


#string = [1, 2, 4]
string = (1, 2, 4, 6, 7, 8, 10, 12, 17, 20)
missing_numbers(string)
result = missing_numbers(string)
print(result)
