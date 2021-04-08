# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(a, b, c):
    sequince = [a, b, c]
    sequince.remove(min(sequince))
    print(sum(sequince))
my_func(10, -2, 20)

