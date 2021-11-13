DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS episode;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE episode (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  episode_id TEXT NOT NULL,
  name TEXT NOT NULL,
  viewed INTEGER NOT NULL CHECK (viewed in (0, 1))
);