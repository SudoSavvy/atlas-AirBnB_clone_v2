-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Drop database if it exists
DROP DATABASE IF EXISTS hbnb_dev_db;

-- Create the database
CREATE DATABASE hbnb_dev_db;

-- Use the new database
USE hbnb_dev_db;

-- Create table for states
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

-- Create table for cities with a foreign key to states
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(128) NOT NULL,
    CONSTRAINT fk_state FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);

-- Grant all privileges on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to ensure that the changes take effect
FLUSH PRIVILEGES;
