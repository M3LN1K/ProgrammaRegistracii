from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.ttk import *
import sqlite3
from tkinter import messagebox

#Основное окно программы  
MainWindow = Tk()
MainWindow.title("Test Prog")
MainWindow.geometry('400x250')

con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS records(
                    ID int, AUTO_INCREMENT,
                    fullname text, 
                    birthdate text,
                    phone text,
                    email text,
                    city text,
                    recording_date text,
                    recording_time text,
                    login text,
                    password text
                )'''
            )
con.commit()

#Окно с базой данных
def bdWindow():
    bdWindow = Toplevel(MainWindow)

    bdWindow.title("Запись клиента")
 
    
    bdWindow.geometry("1300x500")

    #columns = ( 'ID', 'fullname', 'birthdate', 'phone', 'email', 'city', 'recording_date', 'recording_time', 'login', 'password')
    Table = ttk.Treeview(bdWindow)
    Table.pack(fill=BOTH, expand=1) 
    """fill=BOTH - Растягивание элемента, expand=1 - Заполнение всего окна"""
    
    Table['columns'] = ( 'ID','fullname', 'birthdate', 'phone', 'email', 'city', 'recording_date', 'recording_time', 'login', 'password')
    Table.column("#0", width=0,  stretch=NO)
    Table.column("ID", stretch=True, anchor=CENTER, width=50)
    Table.column("fullname", stretch=True, anchor=CENTER, width=170)
    Table.column("birthdate", stretch=True, anchor=CENTER, width=120)
    Table.column("phone", stretch=True, anchor=CENTER, width=70)
    Table.column("email", stretch=True, anchor=CENTER, width=150)
    Table.column("city", stretch=True, anchor=CENTER, width=50)
    Table.column("recording_date", stretch=True, anchor=CENTER, width=150)
    Table.column("recording_time", stretch=True, anchor=CENTER, width=70)
    Table.column("login", stretch=True, anchor=CENTER, width=70)
    Table.column("password", stretch=True, anchor=CENTER, width=70)
    
    Table.heading("#0",text="",anchor=CENTER)
    Table.heading("ID", text="ID", anchor=CENTER)
    Table.heading("fullname", text="ФИО", anchor=CENTER)
    Table.heading("birthdate", text="Дата рождения", anchor=CENTER)
    Table.heading("phone", text="Телефон", anchor=CENTER)
    Table.heading("email", text="Почта", anchor=CENTER)
    Table.heading("city", text="Город", anchor=CENTER)
    Table.heading("recording_date", text="Дата записи", anchor=CENTER)
    Table.heading("recording_time", text="Время записи", anchor=CENTER)
    Table.heading("login", text="Логин", anchor=CENTER)
    Table.heading("password", text="Пароль", anchor=CENTER)

    con = sqlite3.connect('userdata.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM records')
    users = cur.fetchall()
    for row in users:
        Table.insert("", END, values=row)
    con.close()
 
    
    

label = Label(MainWindow, 
              text ="Выберите действие.")
 
label.pack(pady = 10)

btn = Button(MainWindow, 
             text ="Открыть базу данных", 
             command = bdWindow
             )
btn.pack(pady = 10)

def openRegisWindow():
    openRegisWindow = Toplevel(MainWindow)
 
    
    openRegisWindow.title("Регистрация")
 
    
    openRegisWindow.geometry("260x410")

    fullname = Label(openRegisWindow, 
                  text="Ведите ФИО:")
    fullname.grid(row=0, column=0)
    fullent = Entry(openRegisWindow, 
                  )
    fullent.grid(row=0, column=1, columnspan=2, pady=10)

    birthdate = Label(openRegisWindow, 
                  text="Ведите дату рождения:")
    birthdate.grid(row=1, column=0)
    birthent = Entry(openRegisWindow, 
                  )
    birthent.grid(row=1, column=1, columnspan=2, pady=10)

    phone = Label(openRegisWindow, 
                  text="Ведите телефон:")
    phone.grid(row=2, column=0)
    phonent = Entry(openRegisWindow, 
                  )
    phonent.grid(row=2, column=1, columnspan=2, pady=10)

    email = Label(openRegisWindow, 
                  text="Ведите почту:")
    email.grid(row=3, column=0)
    emailent = Entry(openRegisWindow, 
                  )
    emailent.grid(row=3, column=1, columnspan=2, pady=10)

    city = Label(openRegisWindow, 
                  text="Ведите город:")
    city.grid(row=4, column=0)
    cityent = Entry(openRegisWindow, 
                  )
    cityent.grid(row=4, column=1, columnspan=2, pady=10)

    recording_date = Label(openRegisWindow, 
                  text="Ведите дата записи:")
    recording_date.grid(row=5, column=0)
    recordent = Entry(openRegisWindow, 
                  )
    recordent.grid(row=5, column=1, columnspan=2, pady=10)

    recording_time = Label(openRegisWindow, 
                  text="Ведите время записи:")
    recording_time.grid(row=6, column=0)
    recordtiment = Entry(openRegisWindow, 
                  )
    recordtiment.grid(row=6, column=1, columnspan=2, pady=10)

    login = Label(openRegisWindow, 
                  text="Введите логин:")
    login.grid(row=7, column=0)
    loginent = Entry(openRegisWindow, 
                  )
    loginent.grid(row=7, column=1, columnspan=2, pady=10)

    password = Label(openRegisWindow, 
                  text="Введите пароль:")
    password.grid(row=8, column=0)
    passwordent = Entry(openRegisWindow, 
                  )
    passwordent.grid(row=8, column=1, columnspan=2, pady=10)

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
            
            except Exception as ep:
                messagebox.showerror('', ep) 
        else:
            messagebox.showerror('Ошибка', warm)
        
    register = Button(openRegisWindow, 
            text ="Зарегистрироваться", 
            command=record)
    register.grid(row=9, column=0, columnspan=2, pady=10)

regist = Button(MainWindow, 
             text ="Зарегистрироваться", 
             command = openRegisWindow)
regist.pack(pady = 10)


#Окно авторизации пользователя
def openEnterWindow():
    openEnterWindow = Toplevel(MainWindow)
 
    
    openEnterWindow.title("Войти в приложение")
    openEnterWindow.geometry("500x250")

    

    def exit():
        con = sqlite3.connect('userdata.db')
        cur = con.cursor()

        
        login = logent.get()
        password = pasent.get()
        

        cur.execute("SELECT * FROM records WHERE login=? AND password=?", (login, password))
        user = cur.fetchone()

        if user:
            messagebox.showinfo("Вы вошли", "Добро пожаловать, " + login + "!")
            AppWindow = Tk()
            AppWindow.title("Страница: " + login )
            AppWindow.geometry("1000x300")
            openEnterWindow.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")  

        

    
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
                text ="Войти", 
                command=exit)
    step.pack(pady = 10)

enter = Button(MainWindow, 
             text ="Войти в приложение", 
             command = openEnterWindow)
enter.pack(pady = 10)

#Запись
def bdWindow():
    bdWindow = Toplevel(MainWindow)
 
    
    bdWindow.title("Запись клиента")
 
    
    bdWindow.geometry("600x600")



    
   


MainWindow.mainloop()






