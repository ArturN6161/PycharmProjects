with open('data.txt', 'r', encoding='utf-8') as file:
    # file.write('ку\n')
    # text = file.readlines()  # ❌
    # text = file.read().split('\n')  # ✅
    # etalon = 'что делаешь'
    # for i in text:
    #     if i == etalon:
    #         print('Найдено!')
    #     else:
    #         print('Неа')

    # text = file.readline(3)  # ❌
    # print(text)

    # Файл можно прочитать только 1 раз
    text = file.read()
    print(text)
    print('-'*32)
    text2 = file.read()
    print(text2)
