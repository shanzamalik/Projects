from tkinter import Tk, ttk,END
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()


display = ttk.Entry(frm, font=("Arial", 18), width=20)
display.grid(column=0, row=0, columnspan=4, pady=10)

######


def press(num):
   display.insert(END, num)#insert(position, text)

def clear():
    display.delete(0, END)# clear the entry for the next number

def set_operator(op):
    global current, operator
    current = display.get()   # store the number currently in the entry
    operator = op             # store which operator (+, -, *, /)
    display.delete(0, END)    

def calculate():
    global current, operator
    second = display.get()        
    display.delete(0, END) 
    
    try:
        if operator == "+":
            display.insert(END, str(float(current) + float(second)))#insert(position, text)
        elif operator == "-":
            display.insert(END, str(float(current) - float(second)))
        elif operator == "*":
            display.insert(END, str(float(current) * float(second)))
        elif operator == "/":
            display.insert(END, str(float(current) / float(second)))
    except:
        display.insert(END, "Error")



row_offset = 1
column_offset = 0
current = ""     # store the first number
operator = ""    # store the selected operator


ttk.Button(frm, text="7",  command=lambda: press(7)).grid(column=0+column_offset, row=0+row_offset)
ttk.Button(frm, text="8", command=lambda: press(8)).grid(column=1+column_offset, row=0+row_offset)
ttk.Button(frm, text="9", command=lambda: press(9)).grid(column=2+column_offset, row=0+row_offset)
ttk.Button(frm, text="4", command=lambda: press(4)).grid(column=0+column_offset, row=1+row_offset)
ttk.Button(frm, text="5", command=lambda: press(5)).grid(column=1+column_offset, row=1+row_offset)
ttk.Button(frm, text="6", command=lambda: press(6)).grid(column=2+column_offset, row=1+row_offset)
ttk.Button(frm, text="1",command=lambda: press(1)).grid(column=0+column_offset, row=2+row_offset)
ttk.Button(frm, text="2", command=lambda: press(2)).grid(column=1+column_offset, row=2+row_offset)
ttk.Button(frm, text="3", command=lambda: press(3)).grid(column=2+column_offset, row=2+row_offset)
ttk.Button(frm, text="0",command=lambda: press(0)).grid(column=1+column_offset, row=3+row_offset)

ttk.Button(frm, text="+",  command=lambda: set_operator("+")).grid(column=3+column_offset, row=0+row_offset)
ttk.Button(frm, text="-",  command=lambda: set_operator("-")).grid(column=3+column_offset, row=1+row_offset)
ttk.Button(frm, text="*",  command=lambda: set_operator("*")).grid(column=3+column_offset, row=2+row_offset)
ttk.Button(frm, text="/", command=lambda: set_operator("/")).grid(column=3+column_offset, row=3+row_offset)
ttk.Button(frm, text="Clear", command=clear).grid(column=0+column_offset, row=3+row_offset)
ttk.Button(frm, text="=", command=calculate).grid(column=2+column_offset, row=3+row_offset)
root.mainloop()