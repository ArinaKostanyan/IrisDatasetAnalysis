CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

-- Создание таблицы streets
CREATE TABLE IF NOT EXISTS streets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    length DECIMAL(5,2) NOT NULL
);

-- Создание таблицы houses
CREATE TABLE IF NOT EXISTS houses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    street_id INT NOT NULL,
    tenants INT NOT NULL,
    floors INT NOT NULL,
    FOREIGN KEY (street_id) REFERENCES streets(id)
);