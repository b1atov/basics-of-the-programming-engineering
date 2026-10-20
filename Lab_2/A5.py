# A5. Делится ли A на B нацело
a = int(input("Введите A: "))
b = int(input("Введите B: "))

print(["NO", "YES"][a % b == 0])
