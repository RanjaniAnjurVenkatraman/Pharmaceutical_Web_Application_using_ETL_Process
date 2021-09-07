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

SELECT *
FROM population
JOIN pharma_spending
ON population.COUNTRY_CODE = pharma_spending.COUNTRY_CODE;