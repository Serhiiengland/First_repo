from datetime import datetime

def get_days_from_today(date):
    
    current_date = datetime.today()
    current_date = current_date.replace(hour=0, minute=0, second=0, microsecond=0)
    
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
    except BaseException:
        print("Please input in format: yyyy-mm-dd")
        return
    
    result = given_date - current_date
   

    print(result.days)
    
get_days_from_today('')
