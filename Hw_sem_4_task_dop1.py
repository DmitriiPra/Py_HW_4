"""
Напишите программу, которая получает целое число и возвращает его двоичное, 
восьмеричное строковое представление.
Функции bin и oct используйте для проверки своего результата.
*Дополнительно
Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
Избегайте магических чисел
Добавьте аннотацию типов где это возможно
Используйте функции
"""


def converter(decimal_input: int, n: int) -> str:
    converter_number: str = ""
    while decimal_input > 0:
        remainder: int = decimal_input % n
        converter_number = str(remainder) + converter_number
        decimal_input //= n
    return converter_number




decimal_input = int(input("Введите число в десятеричной системе: "))

if decimal_input < 0:
    print("Число должно быть неотрицательным.")

else:
    binary_output: str = converter(decimal_input, 2)
    print(f"В двоичной системе: {binary_output}")

    octal_output: str = converter(decimal_input, 8)
    print(f"В восьмеричной системе: {octal_output}")
