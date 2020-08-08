from tkinter import *
from sqlite3 import *

db = connect(input("Create or connect SQLite3 database: "))
cursor = db.cursor()


style = input("Customizable styling (default: order_num):\n")


if style == "":
    style = "order_num"

    
window = Tk()
window.geometry("800x500")
window.title("Database Graphical User Controller")


entry = Entry(window, width=400)
output = Listbox(window, width=400)


entry.place(x=10, y=10, width=580, height=50)
output.place(x=10, y=60, width=780, height=430)


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
    commit()

    
def event_callback_execute(event):
    global cursor, entry, output
    output.delete(0, "end")
    cursor.execute(entry.get())
    for col in l2s(cursor.fetchall()):
        output.insert("end", stylemethods(col))
    commit()
    clear()
    

def clear():
    global entry
    entry.delete(0, "end")
    

def commit():
    global db
    db.commit()


exe = Button(window, text="Execute\ncommand", command=execute)
clr = Button(window, text="Clear input", command=clear)


exe.place(x=590, y=10, width=100, height=50)
clr.place(x=690, y=10, width=100, height=50)


window.bind("<Return>", event_callback_execute)


window.mainloop()
