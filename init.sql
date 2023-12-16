CREATE DATABASE IF NOT EXISTS insurance;
CREATE USER IF NOT EXISTS 'user'@'%' IDENTIFIED BY 'pass';
GRANT ALL ON insurance.* TO 'user'@'%';
FLUSH PRIVILEGES;

use insurance;