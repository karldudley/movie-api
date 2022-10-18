DROP TABLE IF EXISTS movie;

CREATE TABLE movie (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title varchar(255) NOT NULL,
  rating int NOT NULL,
  genre varchar(255) NOT NULL
);

INSERT INTO movie (title, rating, genre) VALUES ('Shrek 2', 5, 'epic'), ('Entergalactic', 4, 'animated rom-com')
