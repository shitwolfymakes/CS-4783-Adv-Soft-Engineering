CREATE DATABASE assignment5

CREATE TABLE `tbl_properties_test`(ID INT(11) AUTO_INCREMENT KEY, address VARCHAR(200) NOT NULL, city VARCHAR(50) NOT NULL, state VARCHAR(2) NOT NULL, zip VARCHAR(10) NOT NULL)

INSERT INTO `tbl_properties_test`(`ID`, `address`, `city`, `state`, `zip`) VALUES (NULL,"123 Valid St.","San Diego","CA","12345")