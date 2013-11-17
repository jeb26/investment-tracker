CREATE TABLE stocks(
	`id` INT NOT NULL AUTO_INCREMENT,
	`Ticker` VARCHAR(255),
	`Name` VARCHAR(255),
	`Price` VARCHAR(255),
	`Change` VARCHAR(255),
	`Percent_change` VARCHAR(255),
	`Volume` VARCHAR(255),
	PRIMARY KEY (id)
)ENGINE = InnoDB;

INSERT INTO `stocks` (`Ticker`, `Name`, `Price`, `Change`, `Percent_change`, `Volume`) VALUES ("DAL", "Delta Air Lines Inc", "28.12", "+0.18", "+0.64%", "10,508,616");
INSERT INTO `stocks` (`Ticker`, `Name`, `Price`, `Change`, `Percent_change`, `Volume`) VALUES ('HD', 'Home Depot Inc', '80.03', '+1.09', '+1.38%', '10,414,767');
INSERT INTO `stocks` (`Ticker`, `Name`, `Price`, `Change`, `Percent_change`, `Volume`) VALUES ('RAD', 'Rite Aid Corporation', '5.26', '+0.04', '+0.77%', '10,356,198');
