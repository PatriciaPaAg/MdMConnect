-- Sample Data

INSERT INTO mezcal_houses(name) VALUES
('MdM'),
('Don Agave'),
('Convite'),
('Casa Chagoya');

INSERT INTO brands (name, mezcal_house_id) VALUES 
('Mercado del Mezcal', 1),
('Silvestres',2),
('Convite', 3),
('Donaji', 4),
('Gotas de Vida', 4);


INSERT INTO products(p_type, brand_id, price, stock) 
VALUES ('Mezcal', 1, 20, 280.00);
SET @product_id = LAST_INSERT_ID();
INSERT INTO mezcals (product_id, agave_type, aging, detail, alcohol_content, size_ml) 
VALUES (@product_id, 'Espadín', 'Joven', 'Gusano', 38.0, 750);

INSERT INTO products(p_type, brand_id, stock, price) 
VALUES ('Mezcal', 3, 5, 280.00);
SET @product_id = LAST_INSERT_ID();
INSERT INTO mezcals (product_id, agave_type, aging, detail, alcohol_content, size_ml) 
VALUES (@product_id, 'Tóbala', 'Joven', 'Edición Aniversario', 45.0, 750);


INSERT INTO products (p_type, brand_id, stock, price) 
VALUES ('Craft', 1, 100, 15.00);
SET @product_id = LAST_INSERT_ID();
INSERT INTO crafts (product_id, craft_type, material, size)
VALUES (@product_id, 'Vaso de veladora', 'Vidrio', 'Uni');

INSERT INTO products (p_type, brand_id, stock, price) 
VALUES ('Craft', 1, 25, 50.00);
SET @product_id = LAST_INSERT_ID();
INSERT INTO crafts (product_id, craft_type, material, size)
VALUES (@product_id, 'Plato', 'Barro Rojo', 'Chico');


INSERT INTO products (p_type, brand_id, stock, price) 
VALUES ('AlcohoDrink', 2, 30, 200.00);
SET @product_id = LAST_INSERT_ID();
INSERT INTO alcoholic_drinks (product_id, ad_type, flavour, alcohol_content, size_ml)
VALUES (@product_id, 'Crema', 'Avellana', 20.0, 750);

INSERT INTO products (p_type, brand_id, stock, price) 
VALUES ('AlcohoDrink', 4, 4, 250.00);
SET @product_id = LAST_INSERT_ID();
INSERT INTO alcoholic_drinks (product_id, ad_type, flavour, alcohol_content, size_ml)
VALUES (@product_id, 'Licor', 'Café', 30.0, 750);


INSERT INTO products (p_type, brand_id, stock, price) 
VALUES ('Salt', 1, 50, 100);
SET @product_id = LAST_INSERT_ID();
INSERT INTO salts (product_id, s_type, size, units)
VALUES (@product_id, 'Gusano', '1', 'oz');

INSERT INTO products (p_type, brand_id, stock, price) 
VALUES ('Salt', 1, 15, 150);
SET @product_id = LAST_INSERT_ID();
INSERT INTO salts (product_id, s_type, size, units)
VALUES (@product_id, 'Gusano', '250', 'gr');


INSERT INTO products (p_type, brand_id, stock, price) 
VALUES ('Kit', 3, 5, 450);
SET @product_id = LAST_INSERT_ID();
INSERT INTO kits (product_id, k_type,  description)
VALUES (@product_id, 'Kit de degustación',  'Esencial, Espadín & Madrecuishe, Coyote, Tepextate');

