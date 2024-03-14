-- Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
--
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT
    ts.title,
    tsg.genre_id
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres g ON tsg.genre_id = g.id
WHERE tsg.genre_id IS NULL
ORDER BY ts.title ASC, tsg.genre_id ASC;