from flask import Flask, url_for, render_template, request, redirect, session
import sqlite3
from back import *
from operator import itemgetter

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])    #декоратор логінації(перша сторінка)
def logination():
    global password_zn, login_zn
    session.clear() 
    if request.method=="GET":   #якщо отримуємо ін-фу
        return render_template('log.html') 
    else:           #якщо надсилаємо ін-фу(кнопки)
        passwod_correct = request.form.get('password_zn')   #пароль, який ввели на сайті
        login_correct = request.form.get('login_zn')    #логін, який ввели на сайті


        if login_check(login_correct):
            if pass_check(login_correct, passwod_correct):
                session['auth'] = True
                return redirect(url_for('start'))
            else:
                return '<p> Пароль невірний </p>'
        else:
            return '<h1> Невірний логін</h1>'

@app.route('/start', methods=['GET', 'POST'])   #декоратор стартової сторінки(2)
def start():
    if request.method=="GET":
        if not ('auth' in session):
            return redirect(url_for('logination'))
        if session['auth'] is True:
            names = get_info()
            named = sorted(names, key=itemgetter(1))
            print(names)
            print(named)
            return render_template('start.html', name_list = named)
    
    else:
        person = request.form.get('persons')
        info_about = get_name_and_info(person)
        return render_template('people.html', name=info_about[1], info=info_about[3], photo = info_about[2]) 

@app.route('/new', methods=['GET', 'POST'])
def new_people():
    if request.method=="GET":
        return render_template('new.html') 
    else:
        passwod_new = request.form.get('password_new')
        login_new = request.form.get('login_new')
        add_user(login_new, passwod_new)
        return '<h1> Запис пройшов успішно </h1>'


app.config['SECRET_KEY'] = '12345678'

if __name__ == '__main__':
    app.run(port=8000)