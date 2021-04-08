string = input("Введите несколько слов, разделенных пробелами : ")
my_word = []
num = 1
for i in range(string.count(' ') + 1):
    my_word = string.split()
    if len(str(my_word)) <= 10:
        print(f" {num}. {my_word [i]}")
        num += 1
    else:
        print(f" {num}. {my_word [i] [0:10]}")
        num += 1