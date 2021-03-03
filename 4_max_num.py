# просим пользователя ввести число и записываем в переменную number
# также переводим введденное значение из формата строки в целочисленный формат
# проверяем, что пользователь ввел положительное целочисленное значение, а не другие символы.
# Выход из цикла, когда пользователь корректно ввел число
while True:
    try:
        number = int(input('Пожалуйста, введите число: '))
        if number < 0:
            print('Число должно быть положительным. Пожалуйста, повторите ввод.')
            continue
        break
    except ValueError:
        print("Это не целочисленное значение. Пожалуйста, повторите ввод.")

max_number = 0  # переменная для хранения максимального числа в цикле

while number > 0:
    if number % 10 > max_number:  # берем последнюю цифру в числе и сравниваем с текущим максимальным значением
        max_number = number % 10  # если последняя цифра больше, то перезаписываем текущее максимальное значение
    number = number // 10  # отсекаем последнюю цифру в числе для последующего цикла

print(f'Самая большая цифра в числе: {max_number}')
