from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.ttk import *
import sqlite3
from tkinter import messagebox
 
# Создание таблицы в интерфейс пользователя
con = sqlite3.connect('userdata.db')
cur = con.cursor()               
cur.execute('''CREATE TABLE IF NOT EXISTS user(
                ID TEXT,
                fullname TEXT, 
                phone TEXT, 
                city TEXT, 
                recording_date TEXT, 
                recording_time TEXT)''')
# Сохраняем изменения и закрываем соединение
con.commit()
                


#Функция открытия главного окна
def EnterWindow():
    openEnterWindow = Tk()
 
    
    openEnterWindow.title("Войти в приложение")
    openEnterWindow.geometry("500x250")

        

    def exit():
        con = sqlite3.connect('userdata.db')
        cur = con.cursor()

            
        login = logent.get()
        password = pasent.get()    
        
        cur.execute("SELECT * FROM records WHERE login=? AND password=?", (login, password))
        userse = cur.fetchone()

        if userse:
            cur.execute(f"SELECT fullname FROM records WHERE login=? AND password=? ", (login, password))
            for Name in cur.fetchone():
                messagebox.showinfo( title="Вы вошли", message=f"Добро пожаловать, {Name} !")
                AppWindow = Tk()
                AppWindow.title(f"Страница: {Name}")
                AppWindow.geometry("1024x768")
                openEnterWindow.destroy()

                Table = Treeview(AppWindow)
                Table.pack(fill=BOTH, expand=1) 
                """fill=BOTH - Растягивание элемента, expand=1 - Заполнение всего окна"""
                
                Table['columns'] = ( 'ID','fullname', 'phone', 'city', 'recording_date', 'recording_time')
                Table.column("#0", width=0,  stretch=NO)
                Table.column("ID", stretch=True, anchor=CENTER, width=50)
                Table.column("fullname", stretch=True, anchor=CENTER, width=170)
                Table.column("phone", stretch=True, anchor=CENTER, width=70)
                Table.column("city", stretch=True, anchor=CENTER, width=50)
                Table.column("recording_date", stretch=True, anchor=CENTER, width=150)
                Table.column("recording_time", stretch=True, anchor=CENTER, width=70)
                
                Table.heading("#0",text="",anchor=CENTER)
                Table.heading("ID", text="ID", anchor=CENTER)
                Table.heading("fullname", text="ФИО", anchor=CENTER)
                Table.heading("phone", text="Телефон", anchor=CENTER)
                Table.heading("city", text="Город", anchor=CENTER)
                Table.heading("recording_date", text="Дата записи", anchor=CENTER)
                Table.heading("recording_time", text="Время записи", anchor=CENTER)

                con = sqlite3.connect('userdata.db')
                cur = con.cursor()
                cur.execute('SELECT * FROM user')
                users = cur.fetchall()
                for row in users:
                    Table.insert("", END, values=row)
                con.close()
                
                
        else:
            messagebox.showerror("Ошибка авторизации", "Не верный логин или пароль!")  

    def register():
        openEnterWindow.destroy()
        openRegisWindow()     

        
    login = Label(openEnterWindow, 
                    text="Ведите логин:")
    login.pack(pady=10)

    logent = Entry(openEnterWindow)
    logent.pack(pady=10)
        
    password = Label(openEnterWindow, 
                    text="Введите пароль:")
    password.pack(pady=10)

    pasent = Entry(openEnterWindow)
    pasent.pack(pady=10)

    step = Button(openEnterWindow, 
                    text ="Войти в приложение", 
                    command=exit)
    step.pack(pady=10)
    
    regist = Button(openEnterWindow, 
        text ="Зарегистрироваться", 
        command = register)
    regist.pack(pady = 10)

def openRegisWindow():
    openRegisWindow = Tk()
 
    
    openRegisWindow.title("Регистрация")
 
    
    openRegisWindow.geometry("260x410")

    fullname = Label(openRegisWindow, 
                  text="Ведите ФИО:")
    fullname.grid(row=0, column=0, sticky=NS)
    fullent = Entry(openRegisWindow, 
                  )
    fullent.grid(row=0, column=1, columnspan=2, pady=10, sticky=NS)

    birthdate = Label(openRegisWindow, 
                  text="Ведите дату рождения:")
    birthdate.grid(row=1, column=0, sticky=NS)
    birthent = Entry(openRegisWindow, 
                  )
    birthent.grid(row=1, column=1, columnspan=2, pady=10, sticky=NS)

    phone = Label(openRegisWindow, 
                  text="Ведите телефон:")
    phone.grid(row=2, column=0, sticky=NS)
    phonent = Entry(openRegisWindow, 
                  )
    phonent.grid(row=2, column=1, columnspan=2, pady=10, sticky=NS)

    email = Label(openRegisWindow, 
                  text="Ведите почту:")
    email.grid(row=3, column=0, sticky=NS)
    emailent = Entry(openRegisWindow, 
                  )
    emailent.grid(row=3, column=1, columnspan=2, pady=10, sticky=NS)

    city = Label(openRegisWindow, 
                  text="Ведите город:")
    city.grid(row=4, column=0, sticky=NS)
    cityent = Entry(openRegisWindow, 
                  )
    cityent.grid(row=4, column=1, columnspan=2, pady=10, sticky=NS)

    recording_date = Label(openRegisWindow, 
                  text="Ведите дата записи:")
    recording_date.grid(row=5, column=0, sticky=NS)
    recordent = Entry(openRegisWindow, 
                  )
    recordent.grid(row=5, column=1, columnspan=2, pady=10, sticky=NS)

    recording_time = Label(openRegisWindow, 
                  text="Ведите время записи:")
    recording_time.grid(row=6, column=0, sticky=NS)
    recordtiment = Entry(openRegisWindow, 
                  )
    recordtiment.grid(row=6, column=1, columnspan=2, pady=10, sticky=NS)

    login = Label(openRegisWindow, 
                  text="Введите логин:")
    login.grid(row=7, column=0, sticky=NS)
    loginent = Entry(openRegisWindow, 
                  )
    loginent.grid(row=7, column=1, columnspan=2, pady=10, sticky=NS)

    password = Label(openRegisWindow, 
                  text="Введите пароль:")
    password.grid(row=8, column=0, sticky=NS)
    passwordent = Entry(openRegisWindow, 
                  )
    passwordent.grid(row=8, column=1, columnspan=2, pady=10, sticky=NS)

    def record():
        check_counter=0
        if fullent.get() == "":
           warm = messagebox.showerror("Внимание!", "Укажите ФИО")
        else:
            check_counter += 1
            
        if birthent.get() == "":
            warm = messagebox.showerror("Внимание!", "Укажите дату рождения")
        else:
            check_counter += 1

        if phonent.get() == "":
            warm = messagebox.showerror("Внимание!", "Укажите номер телефона")
        else:
            check_counter += 1
        
        if  emailent.get() == "":
            warm = messagebox.showerror("Внимание!", "Укажите вашу электронную почту")
        else:
            check_counter += 1

        if cityent.get() == "":
            warm = messagebox.showerror("Внимание!", "Укажиет ваш город")
        else:
            check_counter += 1

        if recordent.get() == "":
            warm = messagebox.showerror("Внимание!", "Укажите дату на которую хотите записаться")
        else:
            check_counter += 1

        if recordtiment.get() == "":
            warm = messagebox.showerror("Внимание!", "Укажите времня на которое хотите записаться")
        else:
            check_counter += 1
        if loginent.get() == "":
            warm = messagebox.showerror("Внимание!", "Введите логин!")
        else:
            check_counter += 1
        if passwordent.get() == "":
            warm = messagebox.showerror("Внимание!", "Введите пароль!")
        else:
            check_counter += 1
        if check_counter == 9:
            try:
                con = sqlite3.connect('userdata.db')
                cur = con.cursor()
                
                # Добавляем нового пользователя
                cur.execute('''INSERT INTO records 
                        (fullname, birthdate, phone, email, city, recording_date, recording_time, login, password)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                        (fullent.get(), birthent.get(), phonent.get(), emailent.get(), cityent.get(), recordent.get(), recordtiment.get(), loginent.get(), passwordent.get()))
                # Сохраняем изменения и закрываем соединение
                con.commit()
                messagebox.showinfo("Информация", "Вы зарегистрированы!")
                cur.execute('''INSERT INTO user 
                        (fullname, phone, city, recording_date, recording_time)
                        VALUES (?, ?, ?, ?, ?)''', 
                        (fullent.get(), phonent.get(), cityent.get(), recordent.get(), recordtiment.get()))
                # Сохраняем изменения и закрываем соединение
                messagebox.showinfo("Информация", "Информация отображена в профиле")
                con.commit()
                openRegisWindow.destroy()
                EnterWindow()
                
            
            except Exception as ep:
                messagebox.showerror('', ep) 
        else:
            messagebox.showerror('Ошибка', warm)

    register = Button(openRegisWindow, 
            text ="Внести дaнные", 
            command=record)
    register.grid(row=9, column=0, columnspan=1, pady=10, sticky=NSEW)




#Окно авторизации пользователя
mainWindow = Tk()
 
    
mainWindow.title("Авторизация")
mainWindow.geometry("500x250")
mainWindow.destroy()
EnterWindow()





mainWindow.mainloop()