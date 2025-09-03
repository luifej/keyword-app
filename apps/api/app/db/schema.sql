CREATE TABLE IF NOT EXISTS keywords (
    id SERIAL PRIMARY KEY,
    keyword TEXT NOT NULL,
    volume INT,
    cpc REAL,
    difficulty REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
