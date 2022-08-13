-- SQL script that creates a trigger that resets the attribure valid_email
-- only when email has been changed

DELIMITER $$

CREATE TRIGGER IF NOT EXISTS check_valid_email
  BEFORE UPDATE ON users
  FOR EACH ROW
  BEGIN
    IF NEW.email != OLD.email
    THEN
      SET NEW.valid_email = 0;
    ELSE
      SET NEW.valid_email = NEW.valid_email;
    END IF;
  END$$

DELIMITER ;


