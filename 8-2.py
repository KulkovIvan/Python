#Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.


class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def divide_by_null(a, b):
        try:
            return f'{a} / {b} = {a / b}'
        except:
            return (f"Делить на ноль нельзя !!!!!!")


div = Division(10, 100)
print(Division.divide_by_null(10, 0))
print(Division.divide_by_null(20, 10))
print(div.divide_by_null(3, 0))