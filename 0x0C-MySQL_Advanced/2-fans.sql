-- Counts the number of fans each country's
-- metal bands have using an SQL query
SELECT origin, sum(fans) as nb_fans
    FROM metal_bands
    GROUP by origin
    ORDER BY nb_fans DESC;