from tkinter import *

# global variable
font= "arial 15 bold"
bg = "snow"

#backward function
def backward():
    data = text.get()
    lenth = len(data)
   
    text.delete(lenth-1)



# clear function
def clear():
    text.delete(0,END)

# button function
def button_clicked(event):
    b = event.widget
    button = b["text"]

    if button == "=":
        ques = text.get()
        ans = eval(ques)
        text.delete(0,END)
        text.insert(0,ans)
        return

    elif button == "x":
        text.insert(END,"*")
        return

    text.insert(END,button)

# creating main window
window = Tk()
window.geometry("259x289")
window.title("Calculator")
window.config(bg = "snow")
window.iconbitmap("cal.ico")


#heading
heading = Label(text = "Calculator",font = font,bg =bg )
heading.pack()

# entry widget
text = Entry(font = font,justify="right",borderwidth=5)
text.pack(pady = 6,ipadx=15)

#button frame
frame = Frame(window)
frame.pack()

num = 1

#button 1 to 9
for i in range(0,3):
    for j in range(0,3):
        b = Button(frame,text = num,width=4,height=1,padx=4,bg=bg,relief = RIDGE,font=font)
        b.grid(row = i,column = j)
        b.bind("<Button-1>",button_clicked)
        num = num+1

# plus minus mutilpy and divide buttons
plus = Button(frame,text ="+",width=4,height=1,padx=4,bg=bg,relief = RIDGE,font=font)
plus.grid(row = 0,column = 3)

multy = Button(frame,text = "x",width=4,height=1,padx=4,bg=bg,relief = RIDGE,font=font)
multy.grid(row = 1,column = 3)

divide = Button(frame,text = "/",width=4,height=1,padx=4,bg=bg,relief = RIDGE,font=font)
divide.grid(row = 2,column = 3)

zero = Button(frame,text = "0",width=4,height=1,padx=4,bg=bg,relief = RIDGE,font=font)
zero.grid(row = 3,column = 0)

clear = Button(frame,text = "C",width=4,height=1,padx=4,bg=bg,relief = RIDGE,font=font,command=clear)
clear.grid(row = 3,column = 1)

equal = Button(frame,text = "=",width=9,height=1,padx=4,bg=bg,relief = RIDGE,font=font)
equal.grid(row = 4,column = 1,columnspan=2)

minus = Button(frame,text = "-",width=4,height=1,padx=4,bg=bg,relief = RIDGE,font=font)
minus.grid(row = 3,column = 3)

dot = Button(frame,text = ".",width=4,height=1,padx=4,bg=bg,relief = RIDGE,font=font)
dot.grid(row = 3,column = 2)

module = Button(frame,text = "%",width=4,height=1,padx=4,bg=bg,relief = RIDGE,font=font)
module.grid(row = 4,column = 3)

back = Button(frame,text = "<x",width=4,height=1,padx=4,bg=bg,relief = RIDGE,font=font,command = backward)
back.grid(row = 4,column = 0)


#binding buttons
plus.bind("<Button-1>",button_clicked)
multy.bind("<Button-1>",button_clicked)
divide.bind("<Button-1>",button_clicked)
minus.bind("<Button-1>",button_clicked)
equal.bind("<Button-1>",button_clicked)
zero.bind("<Button-1>",button_clicked)
dot.bind("<Button-1>",button_clicked)
module.bind("<Button-1>",button_clicked)


window.mainloop()
