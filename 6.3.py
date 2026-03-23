def magicheskaya_data(data):
    den = int(data[0:2])     
    mesyac = int(data[3:5])     
    god = int(data[6:10])    
    
    # Берем последние две цифры года
    poslednie_dve = god % 100
    
    # Проверяем условие: день * месяц = последние две цифры года
    if den * mesyac == poslednie_dve:
        return True
    else:
        return False

data = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if magicheskaya_data(data):
    print("Это МАГИЧЕСКАЯ дата!")
else:
    print("Это не магическая дата.")