# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn

n = int(input("Введите  число - "))
nn = str(n) + str(n)
nnn = str(n) + str(n) + str(n)
result = n + int(nn) + int(nnn)
print(result)