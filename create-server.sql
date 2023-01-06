DROP DATABASE cart;
CREATE DATABASE cart;

\c cart;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

/* Create Wizard Session Table */
CREATE TABLE item_categories (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    category VARCHAR(255) NOT NULL,
    tags VARCHAR(255)[] DEFAULT ARRAY[]::VARCHAR(255)[],
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    updated_at DATE NOT NULL DEFAULT CURRENT_DATE
);

INSERT INTO item_categories
    (category,tags) 
    VALUES 
    (
        'simple',
        ARRAY['kitchen']::VARCHAR(255)[]
    ),
    (
        'complex',
        ARRAY['garage']::VARCHAR(255)[]
    ),
    (
        'common',
        ARRAY['garden']::VARCHAR(255)[]
    );

/* Create Answers Table */
CREATE TABLE items (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    category uuid NOT NULL,
    description VARCHAR(255),
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    updated_at DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT fk_category FOREIGN KEY (category) REFERENCES item_categories(id)
);

INSERT INTO items
    ( category, description) 
    VALUES 
    (
        
        (SELECT id from item_categories where category='simple'),
        'A Mixer'
    ),
    (
        (SELECT id from item_categories where category='complex'),
        'An Automobile'
    ),
    (
        (SELECT id from item_categories where category='common'),
        'A Spade'
    );

/* Create Wizard Step Table */
CREATE TABLE shipments (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    item uuid NOT NULL,
    complete BOOLEAN DEFAULT FALSE NOT NULL,
    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
    updated_at DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT fk_item FOREIGN KEY (item) REFERENCES items(id)
);






