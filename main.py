def evk(a, b):
    while b:
        a, b = b, a % b
    return a


a = int(input("Введите первое число: "))
b = int(input("Введите первое число: "))
result = evk(a, b)
print("НОД:", result)