from datetime import datetime

def get_days_from_today(date): #створюємо ф-цію
    
    current_date = datetime.today() #поточна дата
    current_date = current_date.replace(hour=0, minute=0, second=0, microsecond=0) #встановлюємо час "= 0", оскільки нам не потрібно його враховувати
    
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")  #форматуємо дату в рядок
    except BaseException: # виключаємо всі помилки, та пишемо що вивести
        print("Please input in format: yyyy-mm-dd") #просимо користувача ввести дату у форматі р/м/д
        return
    
    result = given_date - current_date #від поточної дати віднімаємо задану дату
   

    print(result.days) #виводимо результат
   
    
get_days_from_today('2024-03-15') #викликаємо ф-цію, "з.і: можемо змінювати дату"
