-- a script that prepares a MySQL server for the project

-- testing database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant priviliges
GRANT ALL PRIVILEGES ON  hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

--select privileges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;