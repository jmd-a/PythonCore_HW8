from datetime import datetime, timedelta

users = [
    { 'name': "Andrii",
     'birthday': datetime(2003, 8, 2) },
    { 'name': "Vasia",
     'birthday': datetime(2003, 8, 7) },
    { 'name': "Vitalii",
     'birthday': datetime(2003, 7, 31) },
    { 'name': "Alina",
     'birthday': datetime(2003, 8, 6) },
]


def get_birthdays_per_week(users):
    weekdays = {'0': 'Monday', '1': 'Tuesday', '2': "Wednesday", '3': "Thursday", '4': "Friday", '5': "Saturday", '6': "Sunday"}
    birthday_list = []
    today = datetime.now()
    for user in users:
        userbirth = user.get('birthday')
        if userbirth.day - (today + timedelta(days=7)).day <=7:
            if userbirth.weekday() >= 5:
                birthday_list.append(f"{weekdays['0']}: {user.get('name')}")
            if userbirth.weekday() < 5:
                birthday_list.append(f"{weekdays[str(userbirth.weekday())]}: {user.get('name')}")
        
    for birthday in birthday_list:
        print(birthday)
    
                
            


get_birthdays_per_week(users)