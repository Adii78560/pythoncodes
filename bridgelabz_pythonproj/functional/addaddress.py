from tkinter import *
import json

root = Tk()
root.geometry('500x500')


def store():
    f_name = entry_1.get("1.0", "end-1c")
    l_name = entry_2.get("1.0", "end-1c")
    a = entry_3.get("1.0", "end-1c")
    c = entry_4.get("1.0", "end-1c")
    s = entry_5.get("1.0", "end-1c")
    z = entry_6.get("1.0", "end-1c")
    p = entry_7.get("1.0", "end-1c")

    print(f_name, l_name, a, c, s, z, p)
    with open('../address.json', 'r') as f:
        strr = f.read()  # open and read file
        obj = json.loads(strr)  # read json file like object and parse to string

    with open('../address.json', 'w') as f:
        obj['address details'].append({  # open file in write mode and append values
            "first name": f_name,
            "last name": l_name,
            "address": a,
            "city": c,
            "state": s,
            "zip code": z,
            "phone no": p
        })
        f.write(json.dumps(obj, indent=2))  # json object to string
        f.close()


label_0 = Label(root, text="address book form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="first name", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Text(root, height=2, width=50)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="last name", width=20, font=("bold", 10))
label_2.place(x=68, y=180)

entry_2 = Text(root, height=2, width=50)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="address", width=20, font=("bold", 10))
label_3.place(x=70, y=230)

entry_3 = Text(root, height=2, width=50)
entry_3.place(x=240, y=230)

label_4 = Label(root, text="city", width=20, font=("bold", 10))
label_4.place(x=70, y=280)

entry_4 = Text(root, height=2, width=50)
entry_4.place(x=240, y=280)

label_5 = Label(root, text="state", width=20, font=("bold", 10))
label_5.place(x=85, y=330)

entry_5 = Text(root, height=2, width=50)
entry_5.place(x=240, y=330)

label_6 = Label(root, text="zip code", width=20, font=("bold", 10))
label_6.place(x=85, y=380)

entry_6 = Text(root, height=2, width=50)
entry_6.place(x=240, y=380)

label_7 = Label(root, text="phone number", width=20, font=("bold", 10))
label_7.place(x=85, y=430)

entry_7 = Text(root, height=2, width=50)
entry_7.place(x=240, y=430)

Button(root, text='submit', width=20, bg='brown', fg='white', command=lambda: store()).place(x=240, y=480)

root.mainloop()
