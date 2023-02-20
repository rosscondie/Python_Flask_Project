DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    country_continent VARCHAR(255),
    country_population INT,
    country_language VARCHAR(255)
);


CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id)
);
