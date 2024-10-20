-- Create the rules table
CREATE TABLE rules (
    id SERIAL PRIMARY KEY,
    rule_name VARCHAR(255),
    rule_ast JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the users table (to store user data for evaluation)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    age INT,
    department VARCHAR(255),
    salary INT,
    experience INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
