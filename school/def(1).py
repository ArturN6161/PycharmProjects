#def open_file(file_name):
#    list = file_name.split('.')
#    if len(list) > 1:
#        ext = list[-1]
#        print(f'file extention {ext}')
#    else:
#        raise FileNotFoundError('Нет расширения')
#    with open(file_name, "r", encoding="utf-8") as file:
#        text = file.read()
#        print(text)
#    #return name, ext

#file_name = "school/text.1"

#print(f'Open the file {file_name}: file name {name}, file extention {ext}')
#open_file(file_name)

st="1. Дмитрий считает, что когда текст пишут в скобках (как вот тут, например), его читать не нужно. Вот и надумал он существенно укоротить время чтения, написав функцию, которая будет удалять все, что расположено внутри скобок. Помогите ленивому Диме разработать функцию shortener(st), которая будет удалять все, что внутри скобок и сами эти скобки, возвращая очищенный текст."


#with open("school/text.1", "r", encoding="utf-8") as file:
#    st = file.read()


# def shortener(st):
#     text = st.replace(")", "(").split("(")
#     text = text[::2]
#     return text


# string_text = ''.join(shortener(st))
# print(string_text)

# with open("school/text.1", "r", encoding="utf-8") as file:
#     st = file.read()


# def camel(st):
#     text = ""
#     counter = 0
#     for i in st:
#         if i.isalpha():
#             if counter % 2 == 0:
#                 #text.append(i.upper())
#                 text += i.upper()
#             else:
#                 #text.append(i.lower())
#                 text += i.lower()
#             n += 1
#         else:
#             text += i
#     print(text)


# camel(st)


# def is_prime(n):
#     count = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1
#     if count <= 2:   
#         return True
#     return False


# n = int(input('Enter natural number for ... :'))

# result = is_prime(n) 

# print(f'Number {n} {result} ')


# with open('school/text.1', 'r', encoding='utf-8') as file:
#     text = file.read()


# def count_alpha(text):
#     total_upper = 0
#     total_lower = 0
#     for i in text:
#         if i.isupper():
#             total_upper += 1
#         if i.islower():
#             total_lower += 1
#     return total_upper, total_lower


# total_upper, total_lower = count_alpha(text)

# print(f'Количество символов в верхнем регистре: {total_upper}')
# print(f'Количество строчных букв:  {total_lower}')


# numbers = [1,2,3,3,3,3,4,5]


# def unique(numbers):
#     unique_numbers = []
#     for i in numbers:
#         if i not in unique_numbers:
#             unique_numbers.append(i)
#     return unique_numbers

# unique_numbers = unique(numbers)

# print(unique_numbers)


# start = int(input('Enter number for start range: '))
# end = int(input('Enter number for end range: '))
# number = int(input(': '))


# def number_in_range(start, end, number):
#     if number in range(start, end):
#         return True
#     return False

# result = number_in_range(start, end, number)

# print(f'Number in range {start} - {end} is {result}')


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 


# def evan_num(numbers):
#     evan_numbers = []
#     for i in numbers:
#         if i % 2 == 0:
#             evan_numbers.append(i)
#     return evan_numbers


# evan_numbers = evan_num(numbers)
# print(evan_numbers)


# colors = 'зелёный-красный-жёлтый-чёрный-белый'

# def sortt(colors):
#     colors = colors.split("-")
#     colors.sort()
#     colors = "-".join(colors)
#     return colors


# sort_colors = sortt(colors)

# print(sort_colors)


from datetime import datetime


start_time = 100000#int(input('Enter number 1: '))
end_time = 1000000#int(input('Enter number 2: '))

def delta(start_time, end_time):
    delta_sec = 0
    start_time = datetime.timedelta(seconds=start_time)
    end_time = datetime.timedelta(seconds=end_time)

    if start_time < end_time:
        delta_sec = end_time - start_time
    
    else:
        delta_sec = star_time - end_time
    
    return days, hours, minutes, sec


delta_time = delta(start_time, end_time)

print(f'Разница между {start_time}, {end_time}: {delta_time}')