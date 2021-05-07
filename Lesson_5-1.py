 # Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 # Об окончании ввода данных свидетельствует пустая строка.

list = []
while True:
    line = input('Введите текст \n')
    if line == '':
        exit()
    else:
        newline = line + '\n'
        list.append(newline)

    f = open('file_1.txt', 'w', encoding='utf-8')
    f.writelines(list)
    f.close()


