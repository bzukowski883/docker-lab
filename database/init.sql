CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name varchar(50),
    email varchar(100) UNIQUE
);
INSERT INTO users(name, email) VALUES
    ('Brent', 'brent@snhu.edu'),
    ('Trunks', 'trunks@snhu.edu'),
    ('Daniel', 'daniel@snhu.edu');