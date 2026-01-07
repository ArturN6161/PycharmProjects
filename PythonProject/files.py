# with open("text.txt", "r", encoding="utf-8") as file:
#     lines = int(input("Vvod: "))
#     if lines > 0:
#         text = file.read().split("\n")
#         for i in text[::-1]:
#             if lines != 0:
#                 break
#             lines -= 1
#             print(i)
#     else:
#         print("")

# with open("words.txt", "r") as file:
#     text = file.read().split("\n")
#     for i in text:
#         if i.lower() == i[::-1].lower():
#             print(i, "- True")
#         else:
#             print(i, "- False")
# with open("words.txt", "r", encoding="utf-8") as file:
#     text = file.read()
#     count_words = 0
#     search_word = input("==========: ")
#
#     for word in text.split():
#         if search_word == word:
#             count_words += 1
#
# print(f"{count_words} find words, {len(text)} symbols")

# with open("words.txt", "r", encoding="utf-8") as file:
#     words = file.read().split()
#     max_len_word = 0
#     list_words = []
#     for word in words:
#         if len(word) > max_len_word:
#             max_len_word = len(word)
#     for word in words:
#         if len(word) == max_len_word:
#             list_words.append(word)
#     print(f"Список длинных слов: {', '.join(list_words)}")
#     print(f"Длина самого длинного слова: {max_len_word}")

# with open("words.txt", "r", encoding="utf-8") as file:
#     line_of_text = file.read().split("\n")
    
    
#     while True:
#         try:
#             count_lines = int(input("Insert number of lines: "))
#             if count_lines > 0:
#                 break
#             else:
#                 print("Number must be greater than 0")
#         except ValueError:
#             print("Insert number")
#         except KeyboardInterrupt:
#             print("\nProgram was stopped by user")
#             break
#     try:
#         for i in line_of_text[:count_lines]:
#             print(f'{i}')
#     except NameError:
#         pass

# with open("words.txt", "r", encoding="utf-8") as file:
#     line_of_text = file.read().split("\n")
    
    
#     while True:
#         try:
#             count_lines = int(input("Insert number of lines: "))
#             if count_lines > 0:
#                 break
#             else:
#                 print("Number must be greater than 0")
#         except ValueError:
#             print("Insert number")
#         except KeyboardInterrupt:
#             print("\nProgram was stopped by user")
#             break
#     try:
#         for i in line_of_text[:count_lines]:
#             print(f'{i}')
#     except NameError:
#         pass

#alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#kworg = {}
#for i, symbol in enumerate(alphabet, 1):
 #   kworg[symbol] = i
#
#total = {}
#
#with open("words.txt", "r", encoding="utf-8") as file:
#    words = file.read().split()
#    for word in words:
#        word_sum = 0
#        for symbol in word.lower():
#            if symbol in kworg:
#                word_sum += kworg[symbol]
#        total[word] = word_sum
#    print(max(total.items()))

with open('ariphetic.txt', 'r', encoding='utf-8') as file:
    text = file.read().replace('\n', "")
    total = eval(text)
    print(total)

