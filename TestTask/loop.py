import random

# Exercise 1: Print First 10 natural numbers using while loop
'''n = 1
while n <= 10:
    print(n)
    n += 1'''

# Exercise 2: Print the following pattern
'''for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()'''

# Exercise 3: Calculate the sum of all numbers from 1 to a given number
'''n = 10
s = 0
for x in range(n+1):
    s += x
print(s)'''

# Exercise 4: Write a program to print multiplication table of a given number
'''n = random.randint(1, 10)
for x in range(1, 11):
    print(n * x)'''

# Exercise 5: Display numbers from a list using loop
'''numbers = [12, 75, 150, 180, 145, 525, 50]
for x in numbers:
    if x > 500:
        break
    elif x > 150:
        continue
    elif x % 5 == 0:
        print(x)'''

# Exercise 6: Count the total number of digits in a number
'''num = 75869
count = 0
while num != 0:
    num = num // 10
    count += 1
print(count)'''

# Exercise 7: Print the following pattern
'''for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print('')'''

# Exercise 8: Print list in reverse order using a loop
'''list1 = [10, 20, 30, 40, 50]
z = len(list1) - 1
for x in list1[::1]:
    list1[z] = x
    z -= 1
print(list1)'''

#Exercise 9: Display numbers from -10 to -1 using for loop
'''for i in range(-10, 0, 1):
    print(i)'''

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
'''a = 4
for i in range(5):
    print(i)
    if a != 0:
        a -= 1
    else:
        print('Done')'''

# Exercise 11: Write a program to display all prime numbers within a range
'''start = 25
end = 50

for x in range(25, 51):
    if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0:
        print(x)'''

# Exercise 12: Display Fibonacci series up to 10 terms
'''f = [0, 1]
for x in range(11):
    f.insert(x+2, sum((f[x], f[x+1])))
for element in f:
    print(element, end=' ')'''

# Exercise 13: Find the factorial of a given number
'''n = random.randint(1, 10)
for i in range(n-1, 0, -1):
    n *= i
print(n)'''

# Exercise 14: Reverse a given integer number
'''num = 76542
result = 0
while num != 0:
    reminder = num % 10
    num = num // 10
    result = result * 10 + reminder
print(result)'''

# Exercise 15: Use a loop to display elements from a given list present at odd index positions
'''my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in my_list[1::2]:
        print(x, end=" ")'''

# Exercise 16: Calculate the cube of all numbers from 1 to a given number
'''n = random.randint(1, 10)
for x in range(n+1):
    print(f'{x}^3 = {x**3}')'''

# Exercise 17: Find the sum of the series upto n terms
'''n = 5
x = 0
s = 0
for i in range(n):
    x = x + 2*10**i
    s += x
print(s, end=' ')'''

# Exercise 18: Print the following pattern
'''for i in range(6):
    for j in range(i, i+1):
        print('* ' * i)
for i in range(4, 0, -1):
    for j in range(i-1, i):
        print('* ' * i)'''

