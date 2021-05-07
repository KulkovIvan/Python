# Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

with open('file_2.txt') as f_obj:
    f = len(open('file_2.txt').readlines())
    print(f'Количество строк в файле {f}')
    content = open('file_2.txt').readlines()
    words_n = 0
    lines = 0
    for line in f_obj:
        lines += 1
        words = line.split()
        words_n = len(words)
        print(f'Слов в строке {lines} -- {words_n}')




