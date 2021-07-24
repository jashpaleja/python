from tkinter import *
expression = ""
total = 0
def eq() :
 global expression
 try :
  total = str(eval(expression))
  equation.set(total)
 except :
 	equation.set("Error")
 finally:
 	expression = ""
def cls() :
 global expression
 expression = ""
 equation.set("Enter your expression :")
def press(n):
 global expression
 expression = expression + str(n)
 equation.set(expression)

m = Tk()
equation = StringVar()
m.title("Calculator")
m.configure(background = "light blue")
m.geometry("320x320")
field = Entry(m,textvariable = equation,state = DISABLED)
field.grid(columnspan = 4,ipadx = 100,ipady = 9)
equation.set("Enter your expression :")
button1 = Button(m,text = "1",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press(1))
button1.grid(row = 2 , column = 0)
button2 = Button(m,text = "2",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press(2))
button2.grid(row = 2 , column = 1)
button3 = Button(m,text = "3",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press(3))
button3.grid(row = 2 , column = 2)
add = Button(m,text = "+",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press("+"))
add.grid(row = 2 , column = 3)
button4 = Button(m,text = "4",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press(4))
button4.grid(row = 3 , column = 0)
button5 = Button(m,text = "5",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press(5))
button5.grid(row = 3 , column = 1)
button6 = Button(m,text = "6",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press(6))
button6.grid(row = 3 , column = 2)
sub = Button(m,text = "-",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press("-"))
sub.grid(row = 3 , column = 3)
button7 = Button(m,text = "7",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press(7))
button7.grid(row = 4 , column = 0)
button8 = Button(m,text = "8",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press(8))
button8.grid(row = 4 , column = 1)
button9 = Button(m,text = "9",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press(9))
button9.grid(row = 4 , column = 2)
mul = Button(m,text = "*",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press("*"))
mul.grid(row = 4 , column = 3)
button0 = Button(m,text = "0",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press(0))
button0.grid(row = 5 , column = 0)
clear = Button(m,text = "C",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: cls())
clear.grid(row = 5 , column = 1)
equals = Button(m,text = "=",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: eq())
equals.grid(row = 5 , column = 2)
div = Button(m,text = "/",bg = "black",fg  = "white",height = 4,width = 10,command = lambda: press("/"))
div.grid(row = 5 , column = 3)
m.mainloop()