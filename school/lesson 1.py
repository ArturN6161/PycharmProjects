# Необходимо определить:
# общее количество чисел
# количество положительных
# количество отрицательных
# количество нулей
#
# Результаты записать в report.txt


# with open("data.txt", "r", encoding="utf-8") as file:
#     text = file.read().split()
    # len_text = len(text)
    # positive_numbers = 0
    # negative_numbers = 0
    # zero_numbers = 0
    #
    # for number in text:
    #     if int(number) > 0:
    #         positive_numbers += 1
    #     elif int(number) < 0:
    #         negative_numbers += 1
    #     elif int(number) == 0:
    #         zero_numbers += 1
    #     else:
    #         pass

# with open("report.txt", "w", encoding="utf-8") as file:
#     file.write("общее количество чисел " + str(len(text)) + "\n")
#     file.write("количество положительных " + str(positive_numbers) + "\n")
#     file.write("количество отрицательных " + str(negative_numbers) + "\n")
#     file.write("количество нулей " + str(zero_numbers) + "\n")

#Посчитать и записать средне арифметическое значение, указать день с минимальной и максимальной температурой. Не использовать функции mix/max

print('Введите пороговые значения, которые будут включены в график погоды')
input_min = int(input("Введите нижний порог: "))
input_max = int(input("Введите верхний порог: "))

with open("data.txt", "r", encoding="utf-8") as file:
    numbers = [int(x) for x in file.read().split()]

    min_temp = numbers[0]
    max_temp = numbers[0]

    for i in numbers:
        if i <= min_temp:
            min_temp = i
        if i > max_temp:
            max_temp = i
        else:
            pass

    abs_temp = sum(numbers) / len(numbers)

    result_temp_list = []

    for i in numbers:
        if input_min < i < input_max:
            result_temp_list.append(i)

    print(result_temp_list)


    #print(f"Среднее арифметическое значение температуры в {numbers} равно {abs_temp:.2f}, минимальная температура в {numbers.index(min_temp)} равна {min_temp}, , максимальная температура в {numbers.index(max_temp)} равна {max_temp}")


with open("result.txt", "w", encoding="utf-8") as file:
    file.write(f"Среднее арифметическое значение температуры в {numbers} равно {abs_temp:.2f}, минимальная температура в {numbers.index(min_temp)} равна {min_temp}, максимальная температура в {numbers.index(max_temp)} равна {max_temp}")








