DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS cities;

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    country VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    country_continent VARCHAR(255),
    country_population INT,
    country_language VARCHAR(255)
    city_id INT NOT NULL REFERENCES cities(id)
);