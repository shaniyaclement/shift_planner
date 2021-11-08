'''Functions used to begin the planner or load the save data from the existing file containing the planner and its user's input. Function used to save and store the user input data to their planner.'''

import json
from pathlib import Path


def load_data():
    filename = 'storedSchedule'
    days_week = {}
    path_to_file = filename
    MVP = Path(path_to_file)

    if MVP.is_file():
        with open(filename, 'r') as file_object:
            days_week = json.load(file_object)
    else:
        days_week = {
            'Sunday': [],
            'Monday': [],
            'Tuesday': [],
            'Wednesday': [],
            'Thursday': [],
            'Friday': [],
            'Saturday': []
        }
    return days_week


def save_data(days_week):
    filename = 'storedSchedule'
    with open(filename, 'w') as file_object:
        json.dump(days_week, file_object)
