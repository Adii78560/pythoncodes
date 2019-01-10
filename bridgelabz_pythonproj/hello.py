import tkinter
import json
F1 = tkinter.Frame()

L = tkinter.Listbox(F1)


L.pack(side=tkinter.LEFT)

with open('/home/admin1/bridgelabz_pythonproj/address.json', 'r') as f:
    a = f.read()
    o = json.loads(a)
    for i in o['address details']:
        L.insert(0, i['first name'] + " " + i['last name'] + "\n")


F1.pack(side=tkinter.TOP)

F2 = tkinter.Frame()
lab = tkinter.Label(F2)

def poll():
    with open('/home/admin1/bridgelabz_pythonproj/address.json', 'r') as f:
        a = f.read()
        o = json.loads(a)
        lab.after(200, poll)
        sel = L.curselection()
        #print(sel)
        #print(lab.config(text=sel))
        for i in o['address details']:
            if sel == i['first name']:
                print(sel)


lab.pack()
F2.pack(side=tkinter.TOP)

poll()
tkinter.mainloop()