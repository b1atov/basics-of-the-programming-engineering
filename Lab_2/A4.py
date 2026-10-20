# A4. Наибольшее из двух чисел без ветвлений, циклов и функций
a = int(input("Введите A: "))
b = int(input("Введите B: "))

result = [a, b][a <= b]
print(result)
