# Веб-приложение (Flask, SQl)

Постановка задачи: написание небольшого веб-приложения, использующего SQL-базу данных.

- о пользователях хранятся банковские данные, такие как: имя, номер счета, состояние счета, статус активности
- README файл, содержащий все зависимости в коде, а также инструкцию по установке/запуску приложения.
- Код приложения и файл инициализации таблиц (фреймворк Flask и запросы на языке SQL)

В папке project находятся 2 файла: **app.py** - файл с кодом приложения, **init-db.sql** - файл инициализации таблиц.

## **Инструкция по установке/запуску:**

Веб-приложение создано на Python с использованием фреймворка Flask и базы данных MySQL. База данных создана в MySQL на локальном хосте с помощью файла инициализации init-db.sql.

1. Для работы с MySQL необходимо установить библиотеку mysql-connector- python (терминал

```
pip install Flask
pip install mysql-connector-python
```

*Установка MySQL:
```
brew install mysql
brew services start mysql #запуск и настройка(если необходимо)
mysql_secure_installation
#В моем случае: имя root, пароль 123456789
```
2. Войдите в систему MySQL, используя учетную запись администратора (root). Замените your_username на ваше имя пользователя MySQL и выполните следующую команду (терминал)

```
mysql -u your_username -p
```
3. Создание базы данных app на localhost для дальнейшего обращения к ней:
```
CREATE DATABASE IF NOT EXISTS app;
USE app;
SOURCE path/to/init-db.sql; #полный путь к файлу init-db.sql
QUIT
```
4. В той же папке project выполните команду
```
FLASK_APP=app.py flask run
```
