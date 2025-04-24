#ИМПОРТ БИБЛИОТЕК
from tkinter import *
from tkinter import ttk
from tkcalendar import *
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import PIL
from sys import *
#ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ
conn = sqlite3.connect('database.db')
db = conn.cursor()
class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
  
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings
        table["displaycolumns"] = headings
  
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)
#ЕСЛИ БАЗА ДАННЫХ УЖЕ ЕСТЬ, ТО ВОЗНИКНЕТ КОНФЛИКТ ЧТЕНИЯ_ЗАПИСИ, И ИНТЕРПРЕТАТОР ВЫВЕДЕТ ОШИБКУ TABLE ALREADY EXISTS, IF NOT EXISTS ПРЕДЛАГАЕТ SQL ИГНОРИРОВАТЬ ПЕРЕСОЗДАНИЯ БД
db.execute('''CREATE TABLE IF NOT EXISTS events (data DATE PRIMARY KEY, tim TIME, event TEXT)''')
db.execute('''CREATE TABLE IF NOT EXISTS tasks (data DATE PRIMARY KEY, tim TIME, task TEXT)''')
db.execute('''CREATE TABLE IF NOT EXISTS meets (data DATE PRIMARY KEY, tim TIME, meet TEXT)''')
#ФУНКЦИЯ ЗАКРЫТИЯ ОКНА
def close():
    window.quit()
#ОКНО О ПРИЛОЖЕНИИ: ЕГО РАЗМЕРЫ, ЭЛЕМЕНТЫ
def about():
    dialog=Tk()
    dialog.title("authors")
    dialog.geometry("250x150")
    aboutdl = ttk.Label (dialog,text="Time Management program")
    licence = ttk.Label (dialog,text="GNU")
    dev = ttk.Label (dialog,text="Copyright NoginskKollege")
    devel = ttk.Label (dialog,text="S.Khoshvaght, A.Kovarsky")
    aboutdl.pack()
    licence.place(x=50, y=30)
    dev.place(x=50, y=60)
    devel.place(x=50, y=90)
    dialog.mainloop()
def info():
    dialoginfo=Tk()
    dialoginfo.title("manual")
    dialoginfo.geometry("350x100")
    aboutdl = ttk.Label (dialoginfo,text="Time Management program")
    what = ttk.Label (dialoginfo,text="Click Moments and create a new record")
    aboutdl.pack()
    what.place(x=50, y=30)
    dialoginfo.mainloop()
    #ОБЯЗАТЕЛЬНАЯ РАБОТА В ФНЕ, ПОСТОЯННЫЙ ПОКАЗ
    
#ОКНО СОЗДАНИЯ ЗАПИСИ: ЕГО ВИДЖЕТЫ, КНОПКА
def event():
    event=Tk()
    event.title("Create Event")
    event.geometry("250x150")
    create = ttk.Button(event, text="Create new event", command=createevent)
    datetime = ttk.Label(event, text="Print day")
    global day
    day = ttk.Entry(event)
    day.place(x=70,y=10)
    global eventtext
    eventtext = ttk.Entry(event).place(x=70,y=30)
    textevent = ttk.Label(event, text="Input event")
    create.place(x=20, y=60)
    datetime.place(x=10, y=10)
    textevent.place(x=10, y=30)
    event.mainloop()
def task():
    task=Tk()
    task.title("Create task")
    task.geometry("250x150")
    create = ttk.Button(task, text="Create new task")
    datetime = ttk.Label(task, text="Print day")
    global day
    day = ttk.Entry(task).place(x=70,y=10)
    global tasktext
    tasktext = ttk.Entry(task).place(x=70,y=30)
    texttask = ttk.Label(task, text="Input event")
    create.place(x=20, y=60)
    datetime.place(x=10, y=10)
    texttask.place(x=10, y=30)
    task.mainloop()
def meet():
    meet=Tk()
    meet.title("Create meet")
    meet.geometry("250x150")
    create = ttk.Button(meet, text="Create new meet")
    datetime = ttk.Label(meet, text="Print day")
    global day
    day = ttk.Entry(meet).place(x=70,y=10)
    global meettext
    meetttext = ttk.Entry(meet).place(x=70,y=30)
    textmeet = ttk.Label(meet, text="Input event")
    create.place(x=20, y=60)
    datetime.place(x=10, y=10)
    textmeet.place(x=10, y=30)
    meet.mainloop()
    
def de1():
    de1=Tk()
    de1.title("Delete")
    de1.geometry("250x150")
    delet = ttk.Button(de1, text="Delete this day", command=delete)
    datetime = ttk.Label(de1, text="Print day")
    global day
    day = ttk.Entry(de1).place(x=70,y=10)
    global meettext
    delet.place(x=20, y=60)
    datetime.place(x=10, y=10)
    de1.mainloop()

#ФУНКЦИЯ ДЛЯ КНОПКИ: СОЗДАНИЕ ЗАПИСИ
def createevent():
    global day
    
    dbdate=(day.get())
    times=0
    global eventttext
    #ev=(eventtext.get())
    times=0
    request = "INSERT INTO events (data, tim) VALUES (?, ?)"
    send = request + '(' + dbdate + ',00-00-00)'
    db.execute(request, (dbdate, 00-00-00))
    data = (db.fetchall())
    rowid=db.lastrowid
    #db.execute('''INSERT INTO events (data, tim) VALUES (11-11-2024, 0);''')
    #data_tuple = (dbdate, times)
    #db.execute(str(data_tuple))
    return day, eventtext
def createtask():
    global day
    
    dbdate=(day.get())
    times=0
    global taskttext
    #ev=(eventtext.get())
    dbdate=(day.get())
    times=0
    db.execute('''INSERT INTO events (data, tim) VALUES (11-11-2024, 0);''')
    #data_tuple = (dbdate, times)
    #db.execute(str(data_tuple))
    return day, eventtext
def createmeet():
    global day
    
    dbdate=(day.get())
    times=0
    global meetttext
    #ev=(eventtext.get())
    dbdate=(day.get())
    times=0
    db.execute('''INSERT INTO events (data, tim) VALUES (11-11-2024, 0);''')
    #data_tuple = (dbdate, times)
    #db.execute(str(data_tuple))
    return day, eventtext
def reported():
    db.execute('SELECT * FROM events')
    data = (db.fetchall())
    filereport = open("report1.txt", "w+")
    filereport.write(str(data))
    filereport.close()
    creatreport=Tk()
    creatreport.geometry("250x150")
    message = ttk.Label(creatreport, text ="report created")
    message.pack()
def delete():
    global day
    datatim=(day.get())
    db.execute('DElETE * FROM events WHERE data=11-11-2024')
    data = (db.fetchall())
    deleted=Tk()
    deleted.geometry("250x150")
    message = ttk.Label(deleted, text ="deleted")
    message.pack()
#ГЛАВНОЕ ОКНО: ЕГО ПАРАМЕТРЫ И ВИДЖЕТЫ
window=Tk()
window.title("deadlines")
window.geometry("600x500")
background=tk.PhotoImage(file="bg.png")
bg = Label(image = background)
bg.place (x=0, y=0)
thisday=ttk.Label(text="You have planned for this day ^")
thisday.place(x=200, y=280)
#ИНИЦИАЛИЗИРУЕМ МЕНЮ
menu = Menu()
filemenu=Menu()
#ИНИЦИАЛИЗИРУЕМ ПОДМЕНЮ, СВЯЗЫВАЕМ ЕГО СПИСК ДЕЙСТВИЙ С ФУНКЦИЯМИ
filemenu.add_command(label="Exit", command=close)
mmenu=Menu()
mmenu.add_command(label="Create Event", command=event)
mmenu.add_command(label="Create Task", command=task)
mmenu.add_command(label="Create Meet", command=meet)
mmenu.add_command(label="Timemanagement...", command=info)
mmenu.add_command(label="Create report", command=reported)
view=Menu()
view.add_command(label="Zoom")
help=Menu()
help.add_command(label="Manual", command=info)
help.add_command(label="About Application", command=about)
#ДОБАВЛЯЕМ МЕНЮ НАВЕРХУ
menu.add_cascade(label="Window/File",menu=filemenu)
menu.add_cascade(label="Targets",menu=mmenu)
menu.add_cascade(label="View",menu=view)
menu.add_cascade(label="Help",menu=help)
##ДОБАВЛЯЕМ КАЛЕНДАРЬ С РАЗМЕРАМИ, ДАТАМИ
myCal = Calendar(window, selectmode="day", date_pattern="dd/mm/yyyy", )
myCal.grid(row=0, column=0, columnspan=3, rowspan=5, sticky="wesn", pady=0)
myCal.place(x=175, y=20)
#createbuttons
deleteico=tk.PhotoImage(file="trash.png")
newico=tk.PhotoImage(file="new.png")
delete = ttk.Button(text="Delete moment", image=deleteico, command=de1)
createtasks = ttk.Button(text="Create new task", image=newico, command=task)
view = ttk.Button(text="view events relaited to this date")
delete.place(x=100, y=225)
createtasks.place(x=50, y=225)
view.place (x=215, y=205)
#ПРОСИМ ПРОЧИТАТЬ БАЗУ ДАННЫХ
db.execute('SELECT * FROM events')
answer = db.fetchall()

#ВЫВОД ЭЛЕМЕНТОВ БД

#СОЗДАЁМ ТАБЛИЦУ ВНИЗУ, ЗАНОСИМ ИНФРМАЦИЮ
 
data = ()
with sqlite3.connect('database.db') as connection:
    db = connection.cursor()
    db.execute("SELECT * FROM events")
    data = (row for row in db.fetchall())

table = Table(window, headings=('date', 'time', 'MEET/EVENT/TASK'), rows=data)
table.place(x=0, y=300)

#ОБЪЕДИНЯЕМ МЕНЮ, ОКНО И ДЕЛАЕМ ОКНО БЕСКОНЕЧНЫМ ПРОЦЕССОМ
window.config(menu=menu)
window.mainloop()
