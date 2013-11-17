CREATE TABLE stocks(
	`ID` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	`Ticker` VARCHAR(5),
	`Name` VARCHAR(255),
	`Price` FLOAT(5,5),
	`Change` FLOAT(5,5),
	`Percent_change` FLOAT(5,5),
	`Volume` INT
)ENGINE = InnoDB;
