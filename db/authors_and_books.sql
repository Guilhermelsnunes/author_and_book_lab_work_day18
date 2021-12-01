DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    title VARCHAR(255)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    author INT REFERENCES authors(id)
);

