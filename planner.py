'''
Shift Schedule Planner 
User should input their own schedule into the planner application- "Monday 9:00am- 5:00pm"
Application should take User input and display a full schedule with 
'''
from planner_tasks import add_shift, remove_shift, view_shifts, user_decide_task
from saveandload import save_data, load_data
from table_view import pop_up


def main():
    #loads stored planner data or makes a new planner for new user
    days_week = load_data()
    # stores which option the user wishs to input: 'add', 'view', or 'remove'
    user_intent = user_decide_task()
    # viewing planner
    if user_intent == 'view':
        intent = ''
        view_shifts(days_week, user_intent, intent)
    # adding to the planner
    elif user_intent == 'add':
        add_shift(user_intent, days_week)
    # removing from planner
    elif user_intent == 'remove':
        remove_shift(user_intent, days_week)
    # save data input while running program to a file
    save_data(days_week)
    # pop up window
    pop_up(days_week)


if __name__ == "__main__":
    main()
