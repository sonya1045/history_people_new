import sqlite3

db_name = 'historical_people.db'

def open():  #функція відкриття бази даних
    global conn, cursor
    conn = sqlite3.connect(db_name) #підключамо conn до бд
    cursor = conn.cursor()  #об'єкт курсора


def close():     #функція закриття бд
    cursor.close()  #ховаємо курсор
    conn.close()    #закриваємо бд





def login_check(login_zn):  #вибираєм логін з бд в змінну
    open()
    cursor.execute('SELECT login FROM auth WHERE login == ?', [login_zn])
    res = cursor.fetchone() #записуєм зміни в змінну
    conn.commit()
    close()
    if res is not None:
        return True
    else:
        return False


def pass_check(login_zn, password_zn): #Вибираємо з бд пароль з логіна
    open()
    cursor.execute('SELECT password FROM auth WHERE login == ?', [login_zn])
    password = cursor.fetchone()
    
    conn.commit()       #підтвердити зміни
    close()
    if password_zn == password[0]:  #
        return True
    else:
        return False
    
def add_people():  
    names = [
        ('Нікола Тесла', ),
        ('Леонардо да Вінчі', ),
        ('Ісаак Ньютон', ),

    ]
    open()
    cursor.executemany('''INSERT INTO history_peoples (name) VALUES (?)''', names)
    conn.commit()
    close()

def get_info(): #повертає імена
    open()
    cursor.execute('SELECT id, name FROM history_peoples ORDER BY name')
    result = cursor.fetchall()
    close()
    return result

def get_name_and_info(person):  #вибираємо всю інформацію про людину
    open()
    cursor.execute('SELECT id, name, photo, info FROM history_peoples WHERE id = ? ORDER BY id', (person,))
    info = cursor.fetchone()
    close()
    return info

def add_user(new_login, new_password):  #записує новий логін та пароль в бд
    open()
    cursor.execute('INSERT INTO auth (login, password) VALUES (?, ?)', (new_login, new_password))
    conn.commit()
    close()