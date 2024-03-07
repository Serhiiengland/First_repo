import random

    #min не < 1
    #max не > 1000
    #quantity = значення між min and max

def get_numbers_ticket(min, max, quantity): #створюємо ф-цію, яка приймає 3 аргументи
    num_list = []    #створємо порожній список
    if all(isinstance(variable, int) for variable in [min, max, quantity]) :
                             #if type(min) == int and type(max) == int and type(quantity) == int: --->"спочатку було так, поправив лектор"
        if min <1 or max > 1000 or max < min or quantity < 0 or quantity > (max-min): #перевіряємо параметри
            print("Input correct numbers (from 1min to 1000max)")
            return num_list 
    else:
        print("Invalid type")
        return num_list
        
    
    #генеруємо рандомне число в діапазоні та додаємо його у список, якщо його там немає 
    for i in range(quantity):
        num_rnd = random.randrange(min, max +1)
        if num_rnd in num_list:
            while num_rnd in num_list:
                num_rnd = random.randrange(min, max +1)            
            num_list.append(num_rnd)  #додаємо d                   
        else:
            num_list.append(num_rnd)
            
    num_list.sort() #сортуємо список
    #print(num_list)
    return num_list 
    
lottery_numbers = get_numbers_ticket(1, 49, 6) #виклик ф-ції та присвоєння результату змінній
print("Ваші лотерейні числа:", lottery_numbers) #виводимо результат функції
#get_numbers_ticket(1, 49, 6) #виклик ф-ції
