from tkinter import *
from sqlite3 import *

db = connect(input("Create or connect SQLite3 database:"))
cursor = db.cursor()

window = Tk()
window.geometry("500x500")
window.title("Database Graphical User Controller")

entry = Entry(window)
output = Listbox(window)

entry.grid(column=0, row=0)
output.grid(column=0, row=1)


def l2s(lst):
    strings = []
    ls = list(lst)
    for col in ls:
        strings.append(col)
    return strings


def execute():
    global cursor, entry, output
    output.delete(0, "end")
    cursor.execute(entry.get())
    for col in l2s(cursor.fetchall()):
        output.insert(col[0], str(col))


def clear():
    global entry
    entry.delete(0, "end")

def commit():
    global db
    db.commit()


exe = Button(window, text="Execute command", command=execute)
clr = Button(window, text="Clear input", command=clear)
com = Button(window, text="Commit changes", command=commit)

exe.grid(column=1, row=0)
clr.grid(column=2, row=0)
com.grid(column=3, row=0)


window.mainloop()
