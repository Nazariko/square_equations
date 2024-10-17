import tkinter as tk

FONT = ('Courier' , 20)

root = tk.Tk()

label1 = tk.Label(root, text= 'x\u00b2 + ', font=FONT)
label1.grid(row = 0 , column=0)

entry_b = tk.Entry(root, width=5 ,font = FONT )
entry_b.grid(row=0 , column=1)

label2 = tk.Label(root , text ='x + ' , font = FONT)
label2.grid(row = 0, column=2)

entry_a = tk.Entry(root, width=5 ,font = FONT )
entry_a.grid(row= 0 , column=3)

label3 = tk.Label(root, text = '= 0', font = FONT)
label3.grid(row=0,column=4)

solve = tk.Button(root , text='Solve' , font=FONT,width=20)
solve.grid(row=1,column=0,columnspan=5,pady=10)

label_solution = tk.Label(root , text ='', font=FONT ,
                          width=25,height=5 , bg='yellow')
label_solution.grid(row=2,column=0,columnspan=5,pady=10)

def handler_solver():
    try:
        b= float(entry_b.get())
        a = float(entry_a.get())
    except ValueError:
        text = 'wrong format'
    else:
        d = b ** 2 - 4 * a
        if d > 0.0:
            x1 = (-b - d ** 0.5)/ 2
            x2 = (-b + d ** 0.5)/ 2
            text = f'x\u2081 = {x1:.3f}\nx\u2082 = {x2:.3f}'
        elif d == 0.0:
            x1 = -b / 2
            text = f'x\u2081 = {x1:.3f}'
        else:
            text = 'no roots'
    finally:
        label_solution.config(text = text)

solve.config(command=handler_solver , fg='blue')

root.mainloop()