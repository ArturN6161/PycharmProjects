n = int(input('Enter a number to determinate the best divisor: '))

divisors = []
numbers = {}

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
#print(numbers)
#print(divisors)

for i in divisors:
    total = 0
    for number in str(i):
        total += int(number)
        numbers[i] = total

#print(numbers)

max_devisor = 0

for i in numbers:
    if numbers[i] > max_devisor:
        max_devisor = numbers.get(i)

for i in numbers:
    if numbers[i] == max_devisor:
        print(f'The best divisor of {n}: {i}')
        break








# list_numbers = [-5, 1, 2, 3, 4, 5, 6, 7, 8, -3]
# max_number = 0
# min_number = 0
# sum_numbers = 0

# for i in list_numbers:
#     if i > max_number:
#         max_number = i
#     if i < min_number:
#         min_number = i
#     if i > 0:
#         sum_numbers += i

# product_of_numbers = 1

# i_min = list_numbers.index(min_number)
# i_max = list_numbers.index(max_number)

# numbers_for_product = []

# if i_min < i_max:
#     numbers_for_product = list_numbers[i_min + 1: i_max]
# elif i_min > i_max:
#     numbers_for_product = list_numbers[i_max + 1: i_min]

# for i in numbers_for_product:
#     product_of_numbers *= i  

# print(sum_numbers, product_of_numbers)
