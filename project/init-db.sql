CREATE DATABASE IF NOT EXISTS app;
USE app;

CREATE TABLE IF NOT EXISTS
users (
    id INTEGER UNIQUE NOT NULL,
    login TEXT NOT NULL,
    money_amount DECIMAL NOT NULL,
    card_number TEXT NOT NULL,
    status ENUM('активен', 'неактивен')
);

CREATE TABLE IF NOT EXISTS
passwords (
    user_id INTEGER UNIQUE NOT NULL,
    password TEXT NOT NULL
);

REPLACE INTO users VALUES
(1, 'admin', 1000, '4556316239655970', 'активен'),
(2, 'user1', 2500, '5490068478138749', 'активен'),
(3, 'user2', 770, '6011549952662302', 'активен'),
(4, 'user3', 140, '373581218400362', 'неактивен'),
(5, 'user4', 10, '4532156864477293', 'неактивен');

REPLACE INTO passwords VALUES
(1, 'password_admin'),
(2, 'password_1'),
(3, 'password_2'),
(4, 'password_3'),
(5, 'password_4');
