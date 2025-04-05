import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re
from PIL import Image, ImageTk

timer_btn_color = '#00bc00'
id = None
APP_TITLE = 'Rest Timer'

def rest_message():
    messagebox.showinfo(title=APP_TITLE, message='You should rest')
    start()

def stop():
    global timer_btn_color
    timer_btn.config(bg = '#00bc00', text='Start Timer', command=start)
    timer_btn_color = '#00bc00'
    window.after_cancel(id)

def start():
    global id, timer_btn_color
    try:
        time = int(minutes_var.get() * 60 * 1000)
    except:
        messagebox.showerror(title = APP_TITLE, message = 'Invalid time')
    else:
        timer_btn.config(bg = '#ff1629', text='Stop Timer', command=stop)
        timer_btn_color = '#ff1629'
        id = window.after(time, rest_message)

window = tk.Tk()
window.title(APP_TITLE)
icon = ImageTk.PhotoImage(Image.open('t.ico'))
window.iconphoto(True,icon)

frm = tk.Frame(bd=5)
minutes_lbl = tk.Label(frm,text = 'Time in minutes:')
minutes_var = tk.DoubleVar(value = 20)

reg = window.register(lambda text : True if re.fullmatch(r'[\d\.]*', text) and text.count('.') < 2 else False)
minutes_entry = ttk.Spinbox(frm,textvariable = minutes_var, validate='key', validatecommand=(reg, '%P'), from_=0,to=float('inf'))
timer_btn = tk.Button(frm,text='Start Timer', bg = '#00bc00', command=start, cursor='hand2')

minutes_lbl.grid(row = 0, column = 0)
minutes_entry.grid(row=0,column=1,padx=5)
timer_btn.grid(row=0,column=2)

frm.pack()

timer_btn.bind('<Enter>', lambda event : timer_btn.config(bg='#9fbc00' if timer_btn_color == '#00bc00' else '#ff8629'))
timer_btn.bind('<Leave>', lambda event : timer_btn.config(bg='#00bc00' if timer_btn_color == '#00bc00' else '#ff3629'))

window.mainloop()
