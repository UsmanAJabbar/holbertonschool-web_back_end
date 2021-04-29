-- Adds an index to the first element
-- in the database names.
CREATE INDEX idx_name_first_score
    ON names (name(1), score);