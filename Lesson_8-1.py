# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        errors = []
        if not (1 <= day <= 31):
            errors.append('в месяце от 1 до 31 дней')


        if not (1 <= month <= 12):
            errors.append('всего 12 месяцев')

        if not (0 <= year <= 2021):
            errors.append('год от 0 по сейчас(2021)')

        if errors:
            for errors in errors:
                print(errors)



print(Data.valid(32, 13, 2199))
print(Data.valid(28, 4, 2021))
print(Data.extract('28 - 04 - 2021'))
