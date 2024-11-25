CREATE TABLE films (id SERIAL PRIMARY KEY, name VARCHAR(40), director VARCHAR(40), year VARCHAR(5), genres TEXT[]);

INSERT INTO films (name, director, year, genres) VALUES
('Inception', 'Christopher Nolan', '2010', ARRAY['Sci-Fi', 'Thriller']),
('The Godfather', 'Francis Ford Coppola', '1972', ARRAY['Crime', 'Drama']),
('Pulp Fiction', 'Quentin Tarantino', '1994', ARRAY['Crime', 'Comedy']),
('The Dark Knight', 'Christopher Nolan', '2008', ARRAY['Action', 'Thriller']),
('Forrest Gump', 'Robert Zemeckis', '1994', ARRAY['Drama', 'Romance']),
('Fight Club', 'David Fincher', '1999', ARRAY['Drama', 'Thriller']),
('The Matrix', 'Lana Wachowski, Lilly Wachowski', '1999', ARRAY['Sci-Fi', 'Action']),
('Gladiator', 'Ridley Scott', '2000', ARRAY['Action', 'Drama']),
('The Shawshank Redemption', 'Frank Darabont', '1994', ARRAY['Drama', 'Crime']),
('The Lion King', 'Roger Allers, Rob Minkoff', '1994', ARRAY['Animation', 'Adventure']),
('Jurassic Park', 'Steven Spielberg', '1993', ARRAY['Adventure', 'Sci-Fi']),
('The Silence of the Lambs', 'Jonathan Demme', '1991', ARRAY['Thriller', 'Crime']),
('Interstellar', 'Christopher Nolan', '2014', ARRAY['Sci-Fi', 'Adventure']),
('Goodfellas', 'Martin Scorsese', '1990', ARRAY['Crime', 'Drama']),
('The Green Mile', 'Frank Darabont', '1999', ARRAY['Drama', 'Fantasy']),
('Saving Private Ryan', 'Steven Spielberg', '1998', ARRAY['War', 'Drama']),
('Titanic', 'James Cameron', '1997', ARRAY['Romance', 'Drama']),
('Braveheart', 'Mel Gibson', '1995', ARRAY['Action', 'History']),
('The Departed', 'Martin Scorsese', '2006', ARRAY['Crime', 'Thriller']);