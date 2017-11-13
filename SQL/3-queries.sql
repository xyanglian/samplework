--a
SELECT bar FROM Serves WHERE beer = 'Corona';

--b
SELECT DISTINCT beer FROM Frequents, Serves WHERE drinker = 'Ben' AND times_a_week = 1;

--c
SELECT DISTINCT name, address FROM Serves,Likes,Drinker WHERE bar = 'Talk of the Town' AND Likes.drinker = Drinker.name;

--d
SELECT DISTINCT n1.name AS name1, n2.name AS name2 FROM Drinker AS n1, Drinker AS n2 WHERE n1.name > n2.name AND n1.address = n2.address;

--e 
SELECT name FROM beer EXCEPT ALL (SELECT beer FROM likes);

--f
SELECT Beer.name, A.bar FROM Beer LEFT OUTER JOIN ((SELECT * FROM Serves) EXCEPT ALL 
	(SELECT DISTINCT s1.bar, s1.beer, s1.price FROM Serves AS s1, Serves AS s2 
		WHERE s1.beer = s2.beer AND s1.price < s2.price)) AS A ON Beer.name = A.beer;

--g
SELECT DISTINCT drinker FROM Frequents EXCEPT (SELECT DISTINCT drinker FROM (SELECT DISTINCT drinker, bar FROM Frequents EXCEPT ALL (SELECT DISTINCT drinker, bar FROM Likes NATURAL JOIN Serves)) AS f);

--h
SELECT DISTINCT drinker FROM Frequents EXCEPT (SELECT DISTINCT drinker FROM (SELECT DISTINCT drinker, bar FROM Likes NATURAL JOIN Serves EXCEPT ALL (SELECT DISTINCT drinker, bar FROM Frequents)) AS f);

--i

(SELECT DISTINCT Drinker.name AS drinker, 0.00 AS amount FROM Drinker WHERE Drinker.name NOT IN (SELECT Frequents.drinker FROM Frequents))
UNION 
(SELECT Frequents.drinker, COALESCE (SUM(Frequents.times_a_week * Serves.price),0) AS amount 
FROM 
( (Serves RIGHT OUTER JOIN (Frequents LEFT OUTER JOIN Likes ON Frequents.drinker = Likes.drinker) ON Likes.beer = Serves.beer 
	AND Frequents.bar = Serves.bar )) GROUP BY Frequents.drinker) ORDER BY amount DESC;







