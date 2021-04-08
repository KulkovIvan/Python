


my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list} ")
score = int(input("Введите значение рейтинга - "))
while True:
    for el in range(len(my_list)):
        if my_list[el] == score:
            my_list.insert(el + 1, score)
            break
        elif my_list[0] < score:
            my_list.insert(0, score)
        elif my_list[-1] > score:
            my_list.append(score)
        elif my_list[el] > score and my_list[el + 1] < score:
            my_list.insert(el + 1, score)
    print(f"текущий список - {my_list}")
    score = int(input("Введите число "))