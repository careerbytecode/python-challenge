import sqlite3
import os

DB_PATH = "data.db"
PRODUCT_FILTER = "Widget"
NUM_RECORDS = 100_00

def connect_db(path):
    return sqlite3.connect(path)

def setup_database(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            customer_name TEXT,
            product TEXT,
            sale_amount REAL,
            sale_date TEXT
        )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_product ON sales(product)")

def seed_data(cursor, num_records):
    existing_count = cursor.execute("SELECT COUNT(*) FROM sales").fetchone()[0]
    if existing_count == 0:
        print(f"Inserting {num_records} records...")
        for i in range(num_records):
            customer = f"Customer{i}"
            sale_amount = 100 + i % 50
            sale_date = f"2025-07-{(i % 30) + 1:02}"
            cursor.execute("""
                INSERT INTO sales (customer_name, product, sale_amount, sale_date)
                VALUES (?, ?, ?, ?)
            """, (customer, PRODUCT_FILTER, sale_amount, sale_date))
        print("Data seeding complete.")

def fetch_top_sales(cursor, product, limit=10):
    cursor.execute("SELECT * FROM sales WHERE product = ? LIMIT ?", (product, limit))
    return cursor.fetchall()

def main():
    conn = connect_db(DB_PATH)
    cursor = conn.cursor()

    setup_database(cursor)
    seed_data(cursor, NUM_RECORDS)
    conn.commit()

    print(f"\nTop 10 results for product: {PRODUCT_FILTER}")
    for row in fetch_top_sales(cursor, PRODUCT_FILTER):
        print(row)

    conn.close()

if __name__ == "__main__":
    main()
