-- Trigger that reduces the stock of an item
-- as soon as an order comes through the database
CREATE TRIGGER stock_update
    AFTER INSERT on orders
    FOR EACH ROW
        UPDATE items
        SET items.quantity = items.quantity - NEW.number
        WHERE items.name = NEW.item_name
