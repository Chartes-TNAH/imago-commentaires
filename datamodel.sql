SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema imaginatiiif
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `imaginatiiif` ;

-- -----------------------------------------------------
-- Schema imaginatiiif
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `imaginatiiif` DEFAULT CHARACTER SET utf8 ;
USE `imaginatiiif` ;

-- -----------------------------------------------------
-- Table `imaginatiiif`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `imaginatiiif`.`user` ;

CREATE TABLE IF NOT EXISTS `imaginatiiif`.`user` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `user_nom` TINYTEXT NOT NULL,
  `user_login` VARCHAR(45) NOT NULL,
  `user_email` TINYTEXT NOT NULL,
  `user_password` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `user_login_UNIQUE` (`user_login` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `imaginatiiif`.`comment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `imaginatiiif`.`comment` ;

CREATE TABLE IF NOT EXISTS `imaginatiiif`.`comment` (
  `comment_id` INT NOT NULL AUTO_INCREMENT COMMENT '	',
  `comment_nom` TINYTEXT NOT NULL,
  `comment_commentaire` TEXT NOT NULL,
  `comment_lien` TEXT NOT NULL,
  `comment_date` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `comment_user_id` INT,
  
  PRIMARY KEY (`comment_id`),
  INDEX `fk_comment_1_idx` (`comment_user_id` ASC),
  CONSTRAINT `fk_comment_1`
  FOREIGN KEY (`comment_user_id`) REFERENCES `imaginatiiif`.`user`(`user_id`)ON DELETE NO ACTION
    ON UPDATE NO ACTION)
  
ENGINE = InnoDB;





SET SQL_MODE = '';
GRANT USAGE ON *.* TO imaginatiiif_user;
 DROP USER imaginatiiif_user;
SET SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';
CREATE USER 'imaginatiiif_user' IDENTIFIED BY 'password';

GRANT ALL ON `imaginatiiif`.* TO 'imaginatiiif_user';
GRANT SELECT ON TABLE `imaginatiiif`.* TO 'imaginatiiif_user';
GRANT SELECT, INSERT, TRIGGER ON TABLE `imaginatiiif`.* TO 'imaginatiiif_user';
GRANT SELECT, INSERT, TRIGGER, UPDATE, DELETE ON TABLE `imaginatiiif`.* TO 'imaginatiiif_user';


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `imaginatiiif`.`place`
-- -----------------------------------------------------

START TRANSACTION;
USE `imaginatiiif`;
INSERT INTO `imaginatiiif`.`comment` (`comment_id`, `comment_nom`, `comment_commentaire`, `comment_lien`) VALUES (0, 'Photo Bradley & Rulofson', 'Essaie1', 'http://gallica.bnf.fr/iiif/ark:/12148/btv1b8453687c/manifest.json');
INSERT INTO `imaginatiiif`.`comment` (`comment_id`, `comment_nom`, `comment_commentaire`, `comment_lien`) VALUES (2, 'Pont du Carrousel', 'Essaie2', 'https://data.getty.edu/museum/api/iiif/61899/manifest.json');

COMMIT;
-- -----------------------------------------------------
-- Data for table `imaginatiiif`.`user`
-- -----------------------------------------------------
START TRANSACTION;
USE `imaginatiiif`;
INSERT INTO `imaginatiiif`.`user` (`user_id`, `user_nom`, `user_login`, `user_email`, `user_password`) VALUES (1, 'Administrator', 'admin', 'admin@supersite.com', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8');

COMMIT;
