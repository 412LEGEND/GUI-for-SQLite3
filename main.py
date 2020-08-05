from tkinter import *
from sqlite3 import *

db = connect(input("Create or connect SQLite3 database: "))
cursor = db.cursor()

window = Tk()
window.geometry("800x500")
window.title("Database Graphical User Controller")

entry = Entry(window, width=400)
output = Listbox(window, width=400)

entry.place(x=10, y=10, width=300, height=30)
output.place(x=10, y=40, width=780, height=400)

sty = input("Customizable styling: ")

def l2s(lst):
    strings = []
    ls = list(lst)
    for col in ls:
        strings.append(col)
    return strings


def stylify(var):
    global sty
    res = ""
    i = 0
    while i < len(sty):
        if sty[i] == "$":
            i += 1
            if sty[i] == "{":
                temp = 0
                while sty[i] != "}":
                    i += 1
                    if sty[i].isnumeric():
                        temp = temp * 10 + int(sty[i])
                        i += 1
                    elif sty[i] == "}":
                        i += 1
                        break
                    else:
                        raise ValueError("Non-digit between '{' and '}'")
                res += str(var[temp])
                i += 1
            else:
                res += "$"
        elif sty[i] == "\\":
            pass
        else:
            res += str(sty[i])
            i += 1
    return res


def stylemethods(ls):
    global sty
    if sty == "separation_comma":
        return str(ls)
    elif sty == "separation_space":
        temp = ""
        for elem in ls:
            temp += str(elem)
            temp += " "
        return temp
    elif sty == "separation_semi":
        temp = ""
        for elem in ls:
            temp += str(elem)
            temp += "; "
        return temp
    elif sty[1] == "\\":
        sep = sty[1:]
        temp = ""
        for elem in ls:
            temp += str(elem)
            temp += sep
        return temp
    else:
        return stylify(ls)
    


def execute():
    global cursor, entry, output
    output.delete(0, "end")
    cursor.execute(entry.get())
    for col in l2s(cursor.fetchall()):
        output.insert("end", stylemethods(col))


def clear():
    global entry
    entry.delete(0, "end")

def commit():
    global db
    db.commit()


exe = Button(window, text="Execute command", command=execute)
clr = Button(window, text="Clear input", command=clear)
com = Button(window, text="Commit changes", command=commit)

exe.place(x=300, y=10, width=150, height=30)
clr.place(x=450, y=10, width=150, height=30)
com.place(x=640, y=10, width=150, height=30)


window.mainloop()
