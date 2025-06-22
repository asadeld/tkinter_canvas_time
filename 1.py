import tkinter as tk

a = tk.Tk()
a.title('Canvas')
a.geometry('800x600')
a.resizable(False, False)

canvas = tk.Canvas(a, bg='#fff', width=700, height=500)
canvas.pack()

canvas.create_line(0, 0, 700, 500,fill='red')
canvas.create_line(700, 0, 0, 500, width=2, fill='#0f0')
'''
 rgb
#fff - white
#000 - black
#040 - 

0
1
2
3
4
5
6
7
8
9
a
b
c
d
e
f
'''

canvas.create_rectangle(20, 20, 200, 60, fill='#f92')
canvas.create_oval(20, 20, 200, 60, fill='#333')

canvas.create_polygon(10, 30, 200, 200, 200, 30, fill='#00f')
canvas.create_text(350, 250, text='Hello', fill='red', font=(None, 44))

img = tk.PhotoImage(file='img.png')
canvas.create_image(10, 10, image=img)
login = tk.Button(text='click')
canvas.create_window(40, 50, window=login)
a.mainloop()