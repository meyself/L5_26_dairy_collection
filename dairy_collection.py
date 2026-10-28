"""Dairy collection: record milk deliveries and report on them."""
import hashlib
import sqlite3

SCHEMA = "CREATE TABLE milk (id INTEGER PRIMARY KEY, farmer TEXT, litres REAL, fat REAL, day TEXT)"


def create_connection():
    """Create an in-memory database containing the milk table."""
    conn = sqlite3.connect(":memory:")
    conn.execute(SCHEMA)
    return conn


def record_milk(conn, farmer, litres, fat, day):
    """Insert one milk record using a parameterised query."""
    sql = "INSERT INTO milk (farmer, litres, fat, day) VALUES (?, ?, ?, ?)"
    conn.execute(sql, (farmer, litres, fat, day))
    conn.commit()


def farmer_token(farmer):
    """Return a SHA-256 token for the given farmer name."""
    return hashlib.sha256(farmer.encode()).hexdigest()


def daily_total(conn, day):
    """Return a formatted string with total litres collected on a day."""
    rows = conn.execute("SELECT litres FROM milk WHERE day = ?", (day,)).fetchall()
    return f"Total: {sum(row[0] for row in rows):.1f} litres"


def top_farmer(conn):
    """Return the farmer with the highest total litres, or None if empty."""
    rows = conn.execute("SELECT farmer, SUM(litres) FROM milk GROUP BY farmer").fetchall()
    top = max(rows, key=lambda row: row[1], default=None)
    return top[0] if top else None


def print_slip(farmer):
    """Print a collection slip for the given farmer."""
    print(f"printing slip for {farmer}")


def low_fat(conn):
    """Return farmers whose fat reading is missing or below 3.5."""
    rows = conn.execute("SELECT farmer, fat FROM milk").fetchall()
    return [farmer for farmer, fat in rows if fat is None or fat < 3.5]


def main():
    """Run a small demonstration of the dairy collection system."""
    conn = create_connection()
    record_milk(conn, "Gopal", 12.5, 4.1, "Mon")
    record_milk(conn, "Lata", 20.0, 3.2, "Mon")
    print(daily_total(conn, "Mon"), top_farmer(conn), low_fat(conn))
    print_slip("Gopal")
    print(farmer_token("Lata"))
    conn.close()


if __name__ == "__main__":
    main()
