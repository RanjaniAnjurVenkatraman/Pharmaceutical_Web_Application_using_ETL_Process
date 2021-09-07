CREATE TABLE population (
COUNTRY_CODE TEXT PRIMARY KEY,
COUNTRY TEXT,
POPULATION bigint
);

select * from population;

CREATE TABLE pharma_spending (
COUNTRY_CODE TEXT PRIMARY KEY,
PERCENT_PHARMACEUTICAL_SPENDING DECIMAL
);

select * from pharma_spending;

-- Join table
SELECT population.COUNTRY_CODE,population.COUNTRY,population.POPULATION,pharma_spending.PERCENT_PHARMACEUTICAL_SPENDING
FROM population
JOIN pharma_spending
ON population.COUNTRY_CODE = pharma_spending.COUNTRY_CODE;