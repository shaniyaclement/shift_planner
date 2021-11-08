from tkinter import *
from tkinter import ttk
from saveandload import load_data


def pop_up(days_week):
    days_week = load_data()
    # Create an instance of tkinter frame
    win = Tk()
    win.geometry("700x350")
    style = ttk.Style()
    style.theme_use('clam')

    wind = ttk.Treeview(win,
                        column=("Sunday", "Monday", "Tuesday", "Wednesday",
                                "Thursday", "Friday", "Saturday"),
                        show='headings',
                        height=10)

    wind.column("# 1", anchor=CENTER)
    wind.heading("# 1", text="Day")
    wind.column("# 2", anchor=CENTER)
    wind.heading("# 2", text="Shift")

    wind.insert('', 'end', text="1", values=('Sunday', days_week['Sunday']))
    wind.insert('', 'end', text="1", values=('Monday', days_week['Monday']))
    wind.insert('', 'end', text="1", values=('Tuesday', days_week['Tuesday']))
    wind.insert('',
                'end',
                text="1",
                values=('Wednesday', days_week['Wednesday']))
    wind.insert('',
                'end',
                text="1",
                values=('Thursday', days_week['Thursday']))
    wind.insert('', 'end', text="1", values=('Friday', days_week['Friday']))
    wind.insert('',
                'end',
                text="1",
                values=('Saturday', days_week['Saturday']))

    wind.pack()

    win.mainloop()
