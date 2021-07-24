from tkinter import *
window=Tk()
window.geometry("700x400")

options=StringVar(window)
options.set("a")
menu=OptionMenu(window,options, "a","b","c")
menu.grid(row=2,column=2)
selection=options.get()
print(selection)