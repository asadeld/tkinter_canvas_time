import tkinter as tk
import time
import random

#12:00:33
def update_time():
    current_time = time.strftime('%H:%M:%S')
    timer_label.config(text=current_time)
    root.after(1000, update_time)
    colors = ['red', 'green', 'blue', 'yellow', 'orange']
    timer_label.config(fg=colors[random.randint(0, 4)])



root = tk.Tk()
root.title('Часы с датой')

timer_label = tk.Label(root, font=(None, 60), bg='black', fg='green')
timer_label.pack(pady=20)

update_time()
#def click(a):
#    print(a)
#button1 = tk.Button(command=lambda a: click('1'))

root.mainloop()