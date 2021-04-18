#  Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#  Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#  Выполнить подсчет средней величины дохода сотрудников.

with open('file_3.txt', 'r', encoding='utf-8') as f:
    worker = []
    list = f.read().split('\n')
    salary = 0
    count = 0
    for el in list:
        el = el.split()
        if int(el[1]) < 20000:
            worker.append(el[0])
        salary += int(el[1])
        count +=1
    average_salary = salary / count
print(f'Средняя зарплата работников - {average_salary}')
print(f'Оклад меньше 20000 {worker}')