# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

N = int(input('Введите время в секундах - '))
min = 60
hour = 3600


HOURS = N // hour
MINUTS = (N - (HOURS * hour)) // min
SECONDS = N - ((HOURS * hour) + (MINUTS * min))

print(f'{HOURS}:{MINUTS}:{SECONDS}')