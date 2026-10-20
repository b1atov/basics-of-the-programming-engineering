# A6. Электронные часы: время через N секунд от начала суток
n = int(input("Введите N: "))

hours = n // 3600 % 24
minutes = n // 60 % 60
seconds = n % 60

print('{}:{:02}:{:02}'.format(hours, minutes, seconds))
