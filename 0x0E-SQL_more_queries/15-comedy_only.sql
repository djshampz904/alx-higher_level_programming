-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
--
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT
    ts.title
FROM tv_shows ts
JOIN tv_show_genres tsg ON tsg.show_id = ts.id
JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY ts.title ASC;