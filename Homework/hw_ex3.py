import re

def normalize_phone(phone_numbers): #створюємо ф-цію, яка приймає один аргумент
    formated_numbers = []

    for phone_number in phone_numbers:
        cleaned_number = re.sub(r'[^0-9+]' , '', phone_number) #видаляємо всі символи зрядка
        if not cleaned_number.startswith('+'):                 #не видаляємо + 
            if cleaned_number.startswith('380'):               #задаємо параметр щоб всі номери починалися з 380
                cleaned_number = "+" + cleaned_number          #всі номери повинні починатися з +,+38
            else:
                cleaned_number = "+38" + cleaned_number
        formated_numbers.append(cleaned_number) #додаємо форматований номер до списку
    return formated_numbers #повертаємо відфоматований список

phone_numbers = ["067\\t123 4567", #створюємо список необроблених номерів телефонів
    "(095) 234-5678n\\",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "+447771776000 --= ",
    " 0-7-39-37-9-9-9-2"] 

result = normalize_phone(phone_numbers) #присвоюємо змінній result результат виконання ф-ції
#print(result)
 