import os
import psycopg2

dsn = os.getenv("POSTGRES_URL", "postgresql://postgres:postgres@db:5432/keywords")
conn = psycopg2.connect(dsn)
cur = conn.cursor()
cur.execute("INSERT INTO keywords(keyword, volume, cpc, difficulty) VALUES (%s,%s,%s,%s)", 
            ("example keyword", 100, 1.5, 30))
conn.commit()
print("Seeded one keyword")
cur.close(); conn.close()
