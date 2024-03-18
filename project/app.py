from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Подключение к базе данных MySQL
db = mysql.connector.connect(
    host="127.0.0.1", #localhost
    user="root",
    password="123456789",
    database="app"
)
# Для выполнения SQL-запросов
cursor = db.cursor()

@app.route('/')
def index():
    # Предопределенный выбор логинов
    logins = ["admin", "user1", "user2", "user3", "user4"]
    
    # Выбор логина из списка
    form = """
    <h1><center>Добро пожаловать!<center></h1>
    <form action="/by-id" method="get">
        <label for="id">Введите ID пользователя:</label>
        <input type="text" id="id" name="id" required style="width: 35px;"">
        <input type="submit" value="Показать данные">
    </form>
    <form action="/by-login" method="get">
        <label for="login">Выберите логин пользователя:</label>
        <select id="login" name="login" required style="width: 70px;">
    """
    
    # Добавление вариантов логинов
    for login in logins:
        form = form + f'<option value="{login}">{login}</option>'
    form += """
        </select>
        <input type="submit" value="Показать данные">
    </form>
    <a href="/users">Список активных пользователей</a><br>
    """
    return form

@app.route('/by-login')
def user_from_login():
    # Получение login из строки запроса
    login = request.args.get('login')
    
    # Выборка пользователя по id
    query = "SELECT * FROM users INNER JOIN passwords on users.id = passwords.user_id WHERE login = %s;"
    cursor.execute(query, (login,))
    user = cursor.fetchone()
    
    if user:
        return f"""<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
    <title>Таблица login</title>
</head>
<body><center>
<h1><center><font size="5">Данные пользователя с именем "{login}"</font><center></h1>
<table border="1">
    <tr>
        <th>ID</th>
        <th>login</th>
        <th>money_amount</th>
        <th>card_number</th>
        <th>status</th>
        <th>password</th>
    </tr>
    <tr>
        <td><center>{user[0]}<center></td>
        <td><center>{user[1]}<center></td>
        <td><center>{user[2]}<center></td>
        <td><center>{user[3]}<center></td>
        <td><center>{user[4]}<center></td>
        <td><center>{user[6]}<center></td>
    </tr>
</table>

<center></body>
</html>
"""
    else:
        return "<h1>Пользователя не существует!</h1>"

@app.route('/by-id')
def user_from_id():
    # Получение id из строки запроса
    user_id = request.args.get('id')
    
    # Выборка пользователя по id
    query = "SELECT * FROM users INNER JOIN passwords on users.id = passwords.user_id WHERE id = %s;"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    
    if user:
        return f"""<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
    <title>Таблица ID</title>
</head>
<body><center>
<h1><center><font size="5">Данные пользователя с номером ID={user_id}</font><center></h1>
<table border="1">
    <tr>
        <th>ID</th>
        <th>login</th>
        <th>money_amount</th>
        <th>card_number</th>
        <th>status</th>
        <th>password</th>
    </tr>
    <tr>
        <td><center>{user[0]}<center></td>
        <td><center>{user[1]}<center></td>
        <td><center>{user[2]}<center></td>
        <td><center>{user[3]}<center></td>
        <td><center>{user[4]}<center></td>
        <td><center>{user[6]}<center></td>
    </tr>
</table>
<center></body>
</html>
"""
    else:
        return "<h1>Пользователя не существует!</h1>"
        


@app.route('/users')
def list_users():
    # Выборка активных пользователей
    query = "SELECT id, login FROM users WHERE status = 'активен'"
    cursor.execute(query)
    users = cursor.fetchall()
    
    # Оформление списка активных пользователей
    user_list = "<ul>"
    for user in users:
        user_list += f"<li>ID: {user[0]}, Login: {user[1]}</li>"
    user_list += "</ul>"
    return f"<h1><center>Список активных пользователей<center></h1>{user_list}"

if __name__ == '__main__':
    app.run(debug=True)
