-- SQL script that createa a trigger that decreases the quantity of an 
-- item after adding a new order

DROP TRIGGER IF EXISTS remain_quantity;

DELIMITER $$

CREATE TRIGGER remain_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE items
    SET quantity = quantity - NEW.number
      WHERE name = New.item_name;
END $$
DELIMITER ;
