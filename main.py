from datetime import datetime, date, timedelta


def get_birthdays_per_week(users):
    
    # беремо до уваги попередні вихідні дні, якщо тиждень починається з понеділка
    today = date(year=2023, month=8, day=28) 
    start_date =  today - timedelta(days=2) if today.weekday() == 0 else today
    end_date = today + timedelta(days=6)
    two_years = start_date.year != end_date.year
    birthday_people = {}
    
    for user in users:
        
        weekday = -1
        
        # визначаємо день народження в поточному році 
        birthday_in_current_year = date(year=start_date.year, month=user["birthday"].month, day=user["birthday"].day)
        if birthday_in_current_year >= start_date and birthday_in_current_year <= end_date:
            weekday = birthday_in_current_year.weekday()

        # також беремо до уваги що тиждень може починатись в одному році, а закінчуватись в наступному
        if two_years and weekday == -1:
            birthday_in_current_year = date(year=end_date.year, month=user["birthday"].month, day=user["birthday"].day)
            if birthday_in_current_year >= start_date and birthday_in_current_year <= end_date:
                weekday = birthday_in_current_year.weekday()

        if weekday == -1:
            continue

        # якщо вихідний - переносимо нагадування на понеділок (якщо це можливо)
        if weekday == 5 or weekday == 6:
            if birthday_in_current_year + timedelta(days=7-weekday) <= end_date:
                weekday = 0
            else:
                continue      

        list_of_name = birthday_people.get(weekday)
        if list_of_name != None:
            birthday_people[weekday].append(user["name"])
        else:
            birthday_people[weekday] = [user["name"]]

    current_date = start_date
    while current_date <= end_date:
        list_of_users = birthday_people.get(current_date.weekday())
        if list_of_users != None:
            print(current_date.strftime('%A') + ': ' + ', '.join(list_of_users))
        current_date += timedelta(days=1)


test_users = [
    {"name": "Jonh", "birthday": date(day=28, month=7, year=2023)},
    {"name": "Bill", "birthday": date(day=1, month=8, year=2023)},
    {"name": "Vasyl", "birthday": date(day=26, month=8, year=2023)},
    {"name": "Den", "birthday": date(day=27, month=8, year=2023)},
    {"name": "Max", "birthday": date(day=29, month=8, year=2023)},
    {"name": "Jack", "birthday": date(day=31, month=8, year=2023)},
    {"name": "Ben", "birthday": date(day=1, month=9, year=2023)},
    {"name": "Tom", "birthday": date(day=2, month=9, year=2023)},
    {"name": "Ivan", "birthday": date(day=3, month=9, year=2023)},
]
get_birthdays_per_week(test_users)
