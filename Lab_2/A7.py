# A7. Шахматная доска: одного ли цвета две клетки
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

color1 = (x1 + y1) % 2
color2 = (x2 + y2) % 2

if color1 == color2:
    print("YES")
    if color1 == 0:
        print("White")
    else:
        print("Black")
else:
    print("NO")
