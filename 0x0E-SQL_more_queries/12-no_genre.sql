-- shows contained in hbtn_0d_tvshows without a genre linked.
SELECT title, genre_id FROM tv_show_genres sg
	 RIGHT JOIN tv_shows sh ON sg.show_id = sh.id WHERE sg.genre_id IS NULL
	ORDER BY title ASC;
