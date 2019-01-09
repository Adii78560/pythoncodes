from tkinter import *
import json


# def filemenus():
#     pass
#
#
# def add():
#     pass


def find():
    with open('/home/admin1/bridgelabz_pythonproj/address.json', 'r') as f:
        a = f.read()
        o = json.loads(a)
        for i in o['address details']:
            nameorder.insert(0, i['first name'] + " " + i['last name'] + "\n")


def searching():
    with open('/home/admin1/bridgelabz_pythonproj/address.json', 'r') as f:
        a = f.read()
        o = json.loads(a)

        #print(r)
        for i in o['address details']:

            r = nameorder.curselection()
            print(r)
            # if r == i['first name']:
            #     detail.insert(INSERT, i['first name'] + " " + i['last name'] + "\n" + i['address'] + " " + i['city'])


root = Tk()
topframe = Frame(root)
topframe.pack()

middleframe = Frame(root)
middleframe.pack()
lable = Label(middleframe, text='hello')
lable.pack()
nameorder = Listbox(middleframe)
nameorder.pack()


# detail = Label(middleframe)
# detail.pack()

# addadrb = Button(middleframe, text="add address", command=addadr())
# addadrb.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
findb = Label(middleframe, text='address', command=find())
findb.pack()
detail = Text(middleframe,height=10,width = 20)

detail.pack()

addb = Button(bottomframe, text='add')
addb.grid(row=5, column=0)

editb = Button(bottomframe, text='edit')
editb.grid(row=5, column=2)

deleteb = Button(bottomframe, text='delete')
deleteb.grid(row=5, column=4)

sortbylnameb = Button(bottomframe, text='sort by last name')
sortbylnameb.grid(row=5, column=6)

sortbyzipb = Button(bottomframe, text='sort by zip')
sortbyzipb.grid(row=5, column=8)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=5)
filemenu.add_command(label="new")
filemenu.add_command(label="open")
filemenu.add_command(label="save")
filemenu.add_command(label="save as")
filemenu.add_separator()
filemenu.add_command(label="quit")
menubar.add_cascade(label="File")
root.config(menu=menubar)
root.mainloop()
