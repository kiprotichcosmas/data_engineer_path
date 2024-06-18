--  Most popular Hacker News Stories

 SELECT title, score
 FROM hacker_news
 ORDER BY score DESC
 LIMIT 5;

 -- Total Scores for all stories
 SELECT SUM(score)
 FROM hacker_news;

-- Find the individual users who have gotten combined scores of more than 200, and their combined scores.

SELECT user, SUM(score)
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200;

-- add these users’ scores together and divide by the total to get the percentage
SELECT (517 + 309 + 304 + 282) / 6366.0 * 100;

-- times has each offending user posted this link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
SELECT user,
COUNT(*)
FROM hacker_news
WHERE  url LIKE '%watch?v=dQw4w9WgXcQ%'
GROUP BY user
ORDER BY COUNT(*) DESC;

--Rewriting using  column reference numbers instead of column names
SELECT user,
   COUNT(*)
FROM hacker_news
WHERE url LIKE '%watch?v=dQw4w9WgXcQ%'
GROUP BY 1
ORDER BY 2 DESC;

-- Grouping sources of news
SELECT user, 
CASE
   WHEN url LIKE '%github%' THEN 'GitHub'
   WHEN url LIKE '%medium%' THEN 'Medium'
   WHEN url LIKE '%nytimes%' THEN 'New York Times'
   WHEN url LIKE '%youtube%' THEN 'Youtube'
   ELSE 'Other'
  END AS 'Source'
FROM hacker_news;


-- -- Adding count
SELECT CASE
   WHEN url LIKE '%github%' THEN 'GitHub'
   WHEN url LIKE '%medium%' THEN 'Medium'
   WHEN url LIKE '%nytimes%' THEN 'New York Times'
   WHEN url LIKE '%youtube%' THEN 'Youtube'
   ELSE 'Other'
  END AS 'Source',
  COUNT(*)
FROM hacker_news
GROUP BY 1;

-- Getting best time to post story, unformatted time
SELECT timestamp
FROM hacker_news
LIMIT 10;

-- Getting best time to post story, formatted time using strftime function
SELECT timestamp,
   strftime('%Y/%m/%d:  %Hhrs:%Mmins:%Secs', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;

-- a query that returns three columns:
      -- The hours of the timestamp
      -- The average score for each hour
      -- The count of stories for each hour
  
SELECT strftime('%H', timestamp), 
   AVG(score),
   COUNT(*)
FROM hacker_news
GROUP BY 1
ORDER BY 2 DESC;

-- What's the best time to post a story?

SELECT strftime('%H', timestamp) AS 'Hour', 
   ROUND(AVG(score), 1) AS 'Average Score', 
   COUNT(*) AS 'Number of Stories'
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;


