from tkinter import *
from tkinter import filedialog
from tkinter.font  import Font
import pickle

root = Tk()
root.title('To Do List')
root.iconbitmap("D:\download 2nd\Yellowicon-Flat-Full-Trash.ico")
root.geometry('500x500')

fonts =  Font( 
    family="Bodoni MT",
    size=30,
    weight="normal"
)

frames = Frame(root)
frames.pack(pady=10)


lists  = Listbox(frames,
                font = fonts,
                width = 25,
                height=5,
                bg="SystemButtonFace",
                bd= 0,
                fg="#464646",
                highlightthickness=0,
                selectbackground='#a6a6a6',
                activestyle='none'
                )

lists.pack(side=LEFT,fill=BOTH)
  
todo = ['helo','check','buy','cap']


for items in todo:
    lists.insert(END,items)

 
scrolls =  Scrollbar(frames)
scrolls.pack(side=RIGHT,fill=BOTH)

lists.config(yscrollcommand=scrolls.set)
scrolls.config(command=lists.yview)


entries =  Entry(root,font=("Helvetica",24),width=24)
entries.pack(pady=20)

buttonn = Frame(root)
buttonn.pack(pady=20)

#functions

def delete_item():
    lists.delete(ANCHOR)

def add_item():
    lists.insert(END,entries.get())
    entries.delete(0,END)

def cross_item():
    lists.itemconfig(
        lists.curselection(),
        fg="#dedede",
    )
    lists.selection_clear(0,END)

def uncross_item():
     lists.itemconfig(lists.curselection(),
                      fg="#464646")
     lists.select_clear(0,END)

def del_cross_item():
    count=0
    while count <lists.size():
        if lists.itemcget(count,'fg') == '#dedede':
            lists.delete(lists.index(count))
        else:
            count+=1

def save_list():
    fileName = filedialog.asksaveasfilename(initialdir="E:\data",
                                            title="Saved file",
                                            filetypes=(("Dat Files",'*.dat'),
                                                       ('All Files','*.*'))
                                                       )
    
    if fileName:
        if fileName.endswith(".dat"): pass
        else:
            fileName= f'{fileName}.dat'

        count=0
        while count <lists.size():
            if lists.itemcget(count,'fg') == '#dedede':
                lists.delete(lists.index(count))
            else:
                count+=1

        stuff = lists.get(0,END)

        outputFile =  open(fileName,'wb')

        pickle.dump(stuff,outputFile)
        outputFile.close()


def open_list():
    fileName1 = filedialog.askopenfilenames(initialdir="E:\data",title="Open file",filetypes=(("Dat Files",'*.dat'), ('All Files','*.*')))
    if fileName1:
        lists.delete(0,END)

        inputFile = open(fileName1 , "rb")

        stuff = pickle.load(inputFile)

        for items in stuff:
            lists.insert(END,items)

def clear_list():
    lists.delete(0,END)

menuu = Menu(root)
root.config(menu = menuu)

file_menu=  Menu(menuu,tearoff=False)
menuu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="Save list", command=save_list)
file_menu.add_command(label="Open list", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear list", command=clear_list)

delbuttom =  Button(buttonn,text="Delete item", command=delete_item)
addbuttom =  Button(buttonn,text="Add item", command=add_item)
crossbuttom =  Button(buttonn,text="Cross item", command=cross_item)
uncrossbuttom =  Button(buttonn,text="UnCross item", command=uncross_item)
del_crossbuttom =  Button(buttonn,text="Delete Cross item", command=del_cross_item)


delbuttom.grid(row=0,column=0) 
addbuttom.grid(row=0,column=1, padx=20)
crossbuttom.grid(row=0,column=2)
uncrossbuttom.grid(row=0,column=3,padx=20)
del_crossbuttom.grid(row=0,column=4)

root.mainloop()