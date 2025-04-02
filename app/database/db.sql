-- Create the users table (users)
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(60) NOT NULL,
    rol VARCHAR(20)
);

-- Create the roles table (roles)
--CREATE TABLE IF NOT EXISTS roles (
  --  id INTEGER PRIMARY KEY AUTOINCREMENT,
    --role_name VARCHAR(50) UNIQUE NOT NULL  -- e.g. 'admin', 'user'
--);

-- Create the mezcal houses table (mezcal_house)
CREATE TABLE IF NOT EXISTS mezcal_house (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL
);

-- Create the brands table (brand)
CREATE TABLE IF NOT EXISTS brands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    mezcal_house_id INTEGER,
    FOREIGN KEY (mezcal_house_id) REFERENCES mezcal_houses(id) ON DELETE CASCADE
);

CREATE INDEX idx_mezcal_house_id ON brands(mezcal_house_id);

-- Create the main products table (products)
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand_id INTEGER,
    price DECIMAL(10,2) CHECK (price > 0),
    stock INTEGER DEFAULT 0,
    FOREIGN KEY (brand_id) REFERENCES brands(id) ON DELETE CASCADE
);

CREATE INDEX idx_brand_id ON products(brand_id);

-- Create a table to store history of movements (stock_movements)
CREATE TABLE IF NOT EXISTS stock_movements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    movement_type VARCHAR(50),  -- 'entrada' o 'salida'
    quantity INTEGER,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Create a unified table for creams, liquors, cocktails, and gins
CREATE TABLE IF NOT EXISTS alcoholic_drinks (
    product_id INTEGER PRIMARY KEY,
    type VARCHAR(50),  -- Cream, liquor, cocktail, gin
    flavour VARCHAR(50),
    alcohol_content REAL,  -- In percentage
    size_ml INTEGER CHECK (size_ml > 0),
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create the specific table for crafts
CREATE TABLE IF NOT EXISTS crafts (
    product_id INTEGER PRIMARY KEY,
    craft_type VARCHAR(50),  -- Type of craft (e.g. caballito, cuchara, botella pintada, etc.)
    material VARCHAR(50),  -- Material (e.g. madera, barro rojo, etc.)
    size VARCHAR(50),  -- Size of the craft (e.g. chico, mediano, uni, etc.)
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create the specific table for kits
CREATE TABLE IF NOT EXISTS kits (
    product_id INTEGER PRIMARY KEY,
    type VARCHAR(50),  -- Type of Kit (Espadín, Regalo, Degustacion, Variado)
    description VARCHAR(70),  -- Text description of the kit contents
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create the specific table for mezcals
CREATE TABLE IF NOT EXISTS mezcals (
    product_id INTEGER PRIMARY KEY,
    agave_type VARCHAR(50),  -- Agave type (Espadín, Ensamble, Mexicano, etc.)
    aging VARCHAR(50),  -- Aging type: Joven, Reposado, Añejo
    detail VARCHAR(50),  -- Additional characteristics (if agave = ensamble, then the agaves in it)
    alcohol_content REAL CHECK (alcohol_content BETWEEN 34 AND 60),  -- In percentage
    size_ml INTEGER CHECK (size_ml > 0),
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create the specific table for salts
CREATE TABLE IF NOT EXISTS salts (
    product_id INTEGER PRIMARY KEY,
    type VARCHAR(50),  -- Type of salt (e.g, gusano, chapulin)
    size_units VARCHAR(50),  -- Units of the size (e.g. gr, oz)
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);
