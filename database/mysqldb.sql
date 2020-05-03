CREATE TABLE `tbl_props`(ID INT(11) AUTO_INCREMENT KEY, address VARCHAR(200) NOT NULL, city VARCHAR(50) NOT NULL, state VARCHAR(2) NOT NULL, zip VARCHAR(10) NOT NULL)

INSERT INTO `tbl_props`(`ID`, `address`, `city`, `state`, `zip`) VALUES (NULL,"123 Valid St.","San Diego","CA","12345")
INSERT INTO `tbl_props`(`ID`, `address`, `city`, `state`, `zip`) VALUES (NULL,"234 Valid? St.","San Diego","CA","12345")
INSERT INTO `tbl_props`(`ID`, `address`, `city`, `state`, `zip`) VALUES (NULL,"177 Bleecker St.","New York City","NY","10012")
