-- Resets the attribute valid_email on the
-- database if a user's email has been changed
delimiter //
CREATE TRIGGER email_invalidator
    BEFORE UPDATE on users
    FOR EACH ROW
    BEGIN
        IF NEW.email != old.email THEN
            SET NEW.valid_email = 0;
        END IF;
    END; //
delimiter ;
