-- Adds an index to the first element
-- in the database names.
CREATE INDEX idx_name_first
    ON names (name(1));