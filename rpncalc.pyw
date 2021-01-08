from tkinter import *
from tkinter import ttk
from rpn     import Rpn

rpn = Rpn()
show = True
pad = [0.00 for i in range(6)]
keys = [str(i) for i in range(10)] + ['.']
ops = {
       '+':rpn.sum,
       '-': rpn.sub,
       '*': rpn.mul,
       '/':rpn.div,
       'log': rpn.log,
       'pow': rpn.pow,
       'sqrt':rpn.sqrt
       }
subject = ''
hist = '0.0'

root = Tk()
root.title("RPyNCalc")
#root.iconbitmap('RPyNCalc.ico')
root.resizable(False, False)

frame_display = Frame(root, padx=5, pady=5)
frame_display.grid(row=0)

frame_buttons = Frame(root, padx=5, pady=5)
frame_buttons.grid(row=1)

# Refresh Display
def refreshCalc():
    memory = (rpn.mem + pad)[:6]
    if subject:
        mem0 = Label(frame_display, text="%s :0" % subject, width = 20, anchor=E, bg="#FFFFFF")
    else:
        mem0 = Label(frame_display, text="%s :0" % hist, width = 20, anchor=E, bg="#FFFFFF")
    mem1 = Label(frame_display, text="%s :1" % memory[0], width = 20, anchor=E, bg="#FFFFFF")
    mem2 = Label(frame_display, text="%s :2" % memory[1], width = 20, anchor=E, bg="#FFFFFF")
    mem3 = Label(frame_display, text="%s :3" % memory[2], width = 20, anchor=E, bg="#FFFFFF")
    mem4 = Label(frame_display, text="%s :4" % memory[3], width = 20, anchor=E, bg="#FFFFFF")
    mem5 = Label(frame_display, text="%s :5" % memory[4], width = 20, anchor=E, bg="#FFFFFF")

    mem5.grid(row=0, column=0)
    mem4.grid(row=1, column=0)
    mem3.grid(row=2, column=0)
    mem2.grid(row=3, column=0)
    mem1.grid(row=4, column=0)
    mem0.grid(row=5, column=0)

# Save to memory
def enter(*args):
    global subject
    global hist
    if subject:
        hist = subject
        rpn.add(hist)
        subject = ''
        refreshCalc()
    elif hist != '0.0':
        rpn.add(hist)
        refreshCalc()

# Delete from memory
def delete(*args):
    global subject
    global hist
    if rpn.mem:
        rpn.delete()
    else:
        hist = '0.0'
        subject  = ''
    refreshCalc()

def clear():
    global subject
    global hist
    rpn.mem = []
    subject = ''
    hist = '0.0'
    refreshCalc()

# Numbers and Operations
def operate(op):
    global subject
    global hist
    if subject:
            hist = float(subject)
            subject = ''
    elif hist != '0.0':
        hist = float(hist)
    hist = ops[op](hist)
    refreshCalc()

def entry(event):
    global subject
    global hist
    if event.char =='\r':
        enter()
    elif event.char in keys:
        subject += event.char
        refreshCalc()
    elif event.char in ops:
        operate(event.char)


# Buttons
button_sqrt = Button(frame_buttons, text="√", padx=5, pady=5, command=lambda: operate('sqrt'))
button_pow = Button(frame_buttons, text="X^Y", padx=5, pady=5, command=lambda: operate('pow'))
button_log = Button(frame_buttons, text="log", padx=5, pady=5, command=lambda: operate('log'))
button_clear = Button(frame_buttons, text="CLR", padx=5, pady=5, command=clear)

# Key bindings
root.bind("<Return>", enter)
root.bind("<Delete>", delete)
root.bind("<Key>", entry)

# Assembling calculator
refreshCalc()
button_sqrt.grid(row=0, column=0)
button_pow.grid(row=0, column=1)
button_log.grid(row=0, column=2)
button_clear.grid(row=0, column=3)

root.mainloop()
