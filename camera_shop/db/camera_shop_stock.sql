DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    category VARCHAR (255),
    description VARCHAR (255),
    manufacturer_id VARCHAR (255),
    cost_price FLOAT,
    retail_price FLOAT,
    stock_level INT
);


