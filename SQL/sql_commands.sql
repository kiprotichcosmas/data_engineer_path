SELECT COUNT(*)
FROM startups;

SELECT SUM(valuation) as total_value
FROM startups;

SELECT MAX(raised)
FROM startups
WHERE stage = 'Seed';

SELECT MIN(founded)
FROM startups;

SELECT AVG(valuation)
FROM startups;

SELECT category, AVG(valuation)
FROM startups
GROUP BY category;

SELECT category, ROUND(AVG(valuation), 2)
FROM startups
GROUP BY category;

SELECT category, ROUND(AVG(valuation), 2) AS average
FROM startups
GROUP BY category
ORDER BY average DESC;

SELECT category, COUNT(*)
FROM startups
GROUP BY category;

SELECT category, COUNT(*) AS count
FROM startups
GROUP BY category
HAVING count > 3
ORDER BY count DESC;


SELECT location, AVG(employees)
FROM startups
GROUP BY location;

SELECT location, AVG(employees) AS average
FROM startups
GROUP BY location
HAVING average > 500;























