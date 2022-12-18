DROP TABLE IF EXISTS suppliers_products;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    category VARCHAR (255),
    description VARCHAR (255),
    manufacturer VARCHAR (255),
    retail_price FLOAT,
    stock_level INT
);

CREATE TABLE suppliers_products (
    id SERIAL PRIMARY KEY,
    supplier_id INT NOT NULL REFERENCES suppliers(id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    cost_price FLOAT
);

