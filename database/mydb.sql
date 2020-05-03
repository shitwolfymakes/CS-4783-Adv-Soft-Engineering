CREATE DATABASE assignment4;
GO
USE assignment4;
GO
CREATE TABLE tbl_props (id INT IDENTITY(1,1) PRIMARY KEY, address VARCHAR(200) NOT NULL, city VARCHAR(50) NOT NULL, state VARCHAR(2) NOT NULL, zip VARCHAR(10) NOT NULL);
GO
INSERT INTO tbl_props (address, city, state, zip) VALUES ('123 Valid St.', 'San Diego', 'CA', '12345');
INSERT INTO tbl_props (address, city, state, zip) VALUES ('456 Valid? St.', 'San Diego', 'CA', '12345');
INSERT INTO tbl_props (address, city, state, zip) VALUES ('177A Bleecker St.', 'New York City', 'NY', '10012');
GO
CREATE ROLE api_role;
GRANT select, update , insert, delete ON assignment4 TO api_role;
GRANT SELECT, UPDATE, DELETE, INSERT TO api_role;
CREATE LOGIN api_user WITH PASSWORD = 'P@ssw0rd';
CREATE USER api_user FROM LOGIN api_user;
ALTER ROLE api_role ADD MEMBER api_user;
GO
