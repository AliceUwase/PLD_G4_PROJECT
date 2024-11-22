from db import cursor, conn

cursor.execute("DROP TABLE IF EXISTS clients;")

cursor.execute("""
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_info VARCHAR(200) NOT NULL,
    email VARCHAR(100) NOT NULL,
    notes TEXT,
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cursor.execute("DROP TABLE IF EXISTS jobs;")

cursor.execute("""
CREATE TABLE jobs (
    job_id SERIAL PRIMARY KEY,
    job_name VARCHAR(255) NOT NULL,
    company_name VARCHAR(255) NOT NULL,
    rate DECIMAL(10,2) NOT NULL,
    hours DECIMAL(10,2) NOT NULL,
    location VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()