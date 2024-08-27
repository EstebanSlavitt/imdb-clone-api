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
          id INTEGER PRIMARY KEY,
          title TEXT,
          year INTEGER,
          genre TEXT,
          description TEXT,
          image TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    movies_seed_data = [
        (
          "Alien: Romulus",
          2024,
          "horror",
          "A group of young adults attempt to escape their awful world.",
          "https://static1.moviewebimages.com/wordpress/wp-content/uploads/2024/06/alien-romulus-poster.jpg",
        ),
        (
          "Prey",
          2022,
          "horror",
          "A native american fights for her life agains the most advanced killing machine.",
          "https://i0.wp.com/screen-connections.com/wp-content/uploads/2023/08/Prey-4K.UHD_.Coverart.jpg",
        ),
    ]
    conn.executemany(
        """
        INSERT INTO movies (title, year, genre, description, image)
        VALUES (?,?,?, ?,?)
        """,
        movies_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()

def movies_all():
  conn = connect_to_db()
  rows = conn.execute(
      """
      SELECT * FROM movies
      """
  ).fetchall()
  return [dict(row) for row in rows]

def movies_create(title, year, genre, description, image):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO movies (title, year, genre, description, image)
        VALUES (?, ?, ?, ?, ?)
        RETURNING *
        """,
        (title, year, genre, description, image),
    ).fetchone()
    conn.commit()
    return dict(row)
  
if __name__ == "__main__":
    initial_setup()