import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS movies;
        """
    )
    conn.execute(
        """
        CREATE TABLE movies (
          id INTEGER PRIMARY KEY NOT NULL,
          name TEXT,
          width INTEGER,
          height INTEGER
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    movies_seed_data = [
        ("1st movie", 800, 400),
        ("2nd movie", 1024, 768),
        ("3rd movie", 200, 150),
    ]
    conn.executemany(
        """
        INSERT INTO movies (name, width, height)
        VALUES (?,?,?)
        """,
        movies_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()