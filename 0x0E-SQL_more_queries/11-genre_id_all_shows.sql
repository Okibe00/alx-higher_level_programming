-- list all shows contained in hbtn_0d_tvshows having at least on henre

SELECT tv_shows.title, genre_id FROM tv_show_genres 
	RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
	ORDER BY title ASC, genre_id ASC;
