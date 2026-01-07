with open("text.txt", "r", encoding="utf-8") as file:
    total = {}
    words = file.read().split()
    for word in words:
        word_sum = 0
        for sym in word.lower():
            if sym in kworg:
                word_sum += kworg[sym]
        total[word] = word_sum
    for total in total.values():
        if total == max(total.values()):
            print(total)