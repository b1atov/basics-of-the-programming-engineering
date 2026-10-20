import sys

# ---------- A1 ----------
print("=== A1 ===")
width = 17
height = 12.0

print(width // 2, type(width // 2))
print(width / 2.0, type(width / 2.0))
print(height / 3, type(height / 3))
print(1 + 2 * 5, type(1 + 2 * 5))

# ---------- A2 ----------
print()
print("=== A2 ===")

try:
    print(int('123е'))
except Exception as e:
    print("1.", type(e).__name__, "-", e)

try:
    print(int('91.4'))
except Exception as e:
    print("2.", type(e).__name__, "-", e)

# число слишком большое
try:
    print(int(524.345 ** 435345345311145345))
except Exception as e:
    print("3.", type(e).__name__, "-", e)

try:
    print(int('7.1 + 4'))
except Exception as e:
    print("4.", type(e).__name__, "-", e)

# из числа нельзя вычитать строку
try:
    print(int('4' - 2))
except Exception as e:
    print("5.", type(e).__name__, "-", e)

try:
    print(int('4 - 2'))
except Exception as e:
    print("6.", type(e).__name__, "-", e)

try:
    print("7.", int('42'))
except Exception as e:
    print("7.", type(e).__name__, "-", e)

try:
    print("8.", int(-12.12))
except Exception as e:
    print("8.", type(e).__name__, "-", e)

# ---------- A3 ----------
print()
print("=== A3 ===")
size_bytes = 1921000
size_kb = size_bytes / 1024
size_mb = size_kb / 1024
print("Размер в мегабайтах:", size_mb)

number = 3 ** 9090001
print("getsizeof в мегабайтах:", sys.getsizeof(number) / 1024 / 1024)
