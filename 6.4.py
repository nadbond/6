def proverka_bileta(nomer):
    dlina = len(nomer)
    polovina = dlina // 2
    
    summa1 = 0
    for i in range(polovina):
        summa1 = summa1 + int(nomer[i])
    
    summa2 = 0
    for i in range(polovina, dlina):
        summa2 = summa2 + int(nomer[i])
    
    if summa1 == summa2:
        return True
    else:
        return False


print("Проверка счастливого билета")
print("---------------------------")

nomer = input("Введите номер билета (чётное количество цифр): ")

if len(nomer) % 2 != 0:
    print("Ошибка! Количество цифр должно быть чётным")
else:
    if proverka_bileta(nomer):
        print("Поздравляю! Ваш билет СЧАСТЛИВЫЙ!")
    else:
        print("Этот билет НЕ счастливый.")