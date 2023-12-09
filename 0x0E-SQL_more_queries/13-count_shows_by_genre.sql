-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT DISTINCT tg.name AS genre, COUNT(*) OVER (PARTITION BY tg.name) AS number_of_shows FROM tv_show_genres sg
 	JOIN tv_shows sh ON sg.show_id = sh.id
	JOIN tv_genres tg ON sg.genre_id = tg.id
	ORDER BY number_of_shows DESC;
