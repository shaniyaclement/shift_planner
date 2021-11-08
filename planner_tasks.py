'''Functions used to view, remove, and add when editing the planner; end the program; and share the user's choice about what way they would like to use the program.'''
from saveandload import save_data


def view_shifts(days_week):
    save_data(days_week)
    print(days_week)
    intent = input(
        "Would you like to make further edits to your schedule? ('Yes' or 'No') "
    )
    restart_program(intent, days_week)


def user_decide_task():
    user_intent = input(
        "To add to your schedule type 'add'. To view you schedule type 'view'. To remove from your schedule type 'remove'.: "
    )
    while user_intent not in {'add', 'remove', 'view'}:
        user_intent = input(
            "Invalid entry, to add to your schedule type 'add'. To view you schedule type 'view'. To remove from your schedule type 'remove'.: "
        )
    return user_intent


def invalid_day(day):
    while day not in {
            'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday'
    }:
        day = input(
            "Input invalid, What day are you scheduling? (Ex: 'Monday') ")
    return day


def add_shift(user_intent, days_week):
    while user_intent == 'add':
        day = input("What day are you scheduling? (Ex: 'Monday') ")
        invalid_day(day)
        if day in {
                'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday'
        }:
            shift = input("What is your shift? (Ex: Greeter 7:00 - 17:00) ")
            days_week[day].append(shift)
            view_shifts(days_week)
            user_intent = ''


def remove_shift(user_intent, days_week):
    while user_intent == 'remove':
        day = input("What day are you editing? (Ex: 'Monday') ")
        invalid_day(day)
        if day in {
                'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday'
        }:
            shift = input("What is your shift? (Ex: Greeter 7:00 - 17:00) ")
            while shift not in days_week[day]:
                shift = input(
                    "Invalid entry, what is your shift? (Ex: Greeter 7:00 - 17:00) "
                )
            if shift in days_week[day]:
                days_week[day].remove(shift)
            view_shifts(days_week)
            user_intent = ''


def restart_program(intent, days_week):
    while intent not in {'Yes', 'No'}:
        intent = input(
            "Invalid entry, Would you like to make further edits to your schedule? ('Yes' or 'No') "
        )
    if intent == 'No':
        print("Have a great day!")

    if intent == 'Yes':
        user_intent = input(
            "To remove from your schedule type 'remove'. To add to your schedule type 'add'.: "
        )
        if user_intent == 'add':
            add_shift(user_intent, days_week)
        elif user_intent == 'remove':
            remove_shift(user_intent, days_week)
