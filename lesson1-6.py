 #Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
 # Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
 # Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
 # Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Введите результат спортсмена в первый день пробежки в км - '))
b = int(input('Введите общий желаемый результат спортсмена в км - '))
days = 1
result_km = a
while result_km < b:
     a = a + a * 0.1
     days +=1
     result_km = a
print(f'Спортсмен достигнет результа %d км' % b,"на %d день" % days)