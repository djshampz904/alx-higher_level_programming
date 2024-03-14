-- Script lists all tv shows with atleast one genre linked
SELECT
    ts.title,
    tsg.genre_id
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
JOIN tv_genres g ON tsg.genre_id = g.id
ORDER BY ts.title ASC, tsg.genre_id ASC;