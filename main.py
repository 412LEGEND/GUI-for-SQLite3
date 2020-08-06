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

style = input("Customizable styling: ")

def l2s(lst):
    strings = []
    ls = list(lst)
    for col in ls:
        strings.append(col)
    return strings


def stylify(var):
    global style
    res = ""
    i = 0
    while i < len(style):
        if style[i] == "$":
            i += 1
            if style[i] == "{":
                temp = 0
                while style[i] != "}":
                    i += 1
                    if style[i].isnumeric():
                        temp = temp * 10 + int(style[i])
                    elif style[i] == "}":
                        break
                    else:
                        raise ValueError("Non-digit between '{' and '}'")
                res += str(var[temp])
                i += 1
            else:
                res += "$"
        elif style[i] == "\\":
            pass
        else:
            res += str(style[i])
            i += 1
    return res


def stylemethods(ls):
    global style
    if style == "separation_comma":
        return str(ls)
    elif style == "separation_space":
        temp = ""
        for elem in ls:
            temp += str(elem)
            temp += " "
        return temp
    elif style == "separation_semi":
        temp = ""
        for elem in ls:
            temp += str(elem)
            temp += "; "
        return temp
    elif style[1] == "\\":
        sep = style[1:]
        temp = ""
        for elem in ls:
            temp += str(elem)
            temp += sep
        return temp
    elif style == "order_num":
        temp = ""
        for i in range(0, len(ls)):
            temp += str(i) + ": " + str(ls[i]) + "; "
        return temp
    elif style == "order_hex":
        temp = ""
        for i in range(0, len(ls)):
            temp += str(hex(i)) + ": " + str(ls[i]) + "; "
        return temp
    elif style == "order_alpha":
        temp = ""
        alnum = "abcdefghijklmnopqrstuvwxyz"
        for i in range(0, len(ls)):
            temp += alnum[i % len(alnum)] + ": " + str(ls[i]) + "; "
        return temp
    elif style == "order_alnum":
        temp = ""
        alnum = "0123456789abcdefghijklmnopqrstuvwxyz"
        for i in range(0, len(ls)):
            temp += alnum[i % len(alnum)] + ": " + str(ls[i]) + "; "
        return temp
    elif style[0] == ":":
        temp = ""
        orders = style[1:].split()
        for i in range(0, len(ls)):
            temp += orders[i % len(orders)] + ": " + str(ls[i]) + "; "
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
