-- Lists all shows in hbtn_0d_tvshows
-- Should have 2 columns
SELECT s.title, g.genre_id
FROM tv_shows s
   JOIN tv_show_genres g
   ON s.id = g.show_id
ORDER BY s.title, g.genre_id;
