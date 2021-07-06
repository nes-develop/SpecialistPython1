# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

# TODO: your code here

number1 = int(input())
number2 = int(input())
number3 = int(input())

if number1 == number2:
    print("Yes")
elif number2 == number3:
    print("Yes")
elif number1 == number3:
    print("Yes")
else:
    print("No")
