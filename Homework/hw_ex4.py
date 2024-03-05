from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smity", "birthday": "1990.05.23"}
]
#first function
clean_users = []
for user in users:
    try:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date
        clean_users.append({"name": user['name'], "birthday": birthday})
    except ValueError:
        print(f'Impossible')

#second function
def find_next_weekday(d, weekday: int):
