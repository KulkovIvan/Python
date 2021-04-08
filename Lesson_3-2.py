# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def data (name, surname, years, city, email, tel_number):
    return print(' '.join([name, surname, years, city, email, tel_number]))
data(name='Ivan', surname='Kulkov', years='1990', city='Moscow', email='example@mail.ru', tel_number='99912345678')