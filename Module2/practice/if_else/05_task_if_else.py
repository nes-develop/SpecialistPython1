# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here

m = int(input("Введите номер месяца:"))

if  3 <= m <= 5:
    print("Весна")
elif 6 <= m <= 8:
    print("Лето")
elif 9 <= m <= 11:
    print("Осень")
else:
    print("Зима")
