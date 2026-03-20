def n(chislo):
    if chislo % 3 == 0:
        return True
    else:
        return False

chislo = int(input("Введите число: "))
if n(chislo):
    print("Число делится на 3 без остатка")
else:
    print("Число не делится на 3 без остатка")