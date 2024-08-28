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
          "Alien",
          1979,
          "Horror, Sci-Fi",
          "The crew of a commercial spacecraft encounter a deadly lifeform after investigating an unknown transmission.",
          "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
        ),
        (
          "Aliens",
          1986,
          "Horror, Sci-Fi",
          "Ellen Ripley returns to planet LV-426 to battle the Alien menace with a team of colonial marines.",
          "https://upload.wikimedia.org/wikipedia/en/f/fb/Aliens_poster.jpg",
        ),
        (
          "Alien 3",
          1992,
          "Horror, Sci-Fi",
          "Ripley continues her battle with the alien after crash-landing on a prison planet.",
          "https://m.media-amazon.com/images/I/41JDGPK1VML._AC_UF894,1000_QL80_.jpg",
        ),
        (
          "Alien: Resurrection",
          1997,
          "Horror, Sci-Fi",
          "200 years after her death, Ripley is cloned and revived for a mission to extract the Alien queen inside her.",
          "https://m.media-amazon.com/images/M/MV5BNDMyNmU5ZGQtNzhiZi00NjRjLTk3NGUtMmQ5YWU4ODlkNTBhXkEyXkFqcGc@._V1_.jpg",
        ),
        (
          "Prometheus",
          2012,
          "Horror, Sci-Fi",
          "A team of explorers discover a clue to the origins of mankind on Earth, leading them on a journey to the darkest corners of the universe.",
          "https://upload.wikimedia.org/wikipedia/en/a/a3/Prometheusposterfixed.jpg",
        ),
        (
          "Alien: Covenant",
          2017,
          "Horror, Sci-Fi",
          "A colony ship lands on a dark, alien world, where they encounter a terrifying threat beyond their imagination.",
          "https://play-lh.googleusercontent.com/KyHH_uXQI5nq7hWDjmtX-s5gC5EZFZHrtkxTkeaky5Bnb0P5Lsl-dkilEOf3tii1lRBLrA",
        ),
        (
          "Alien: Romulus",
          2024,
          "Horror, Sci-Fi",
          "A group of young adults attempt to escape their awful world.",
          "https://static1.moviewebimages.com/wordpress/wp-content/uploads/2024/06/alien-romulus-poster.jpg",
        ),
        (
          "Predator",
          1987,
          "Action, Sci-Fi",
          "A team of commandos on a mission in a Central American jungle find themselves hunted by an extraterrestrial warrior.",
          "https://upload.wikimedia.org/wikipedia/en/9/95/Predator_Movie.jpg",
        ),
        (
          "Predator 2",
          1990,
          "Action, Sci-Fi",
          "The Predator returns to Earth, this time to stake a claim on the war-torn streets of Los Angeles.",
          "https://lumiere-a.akamaihd.net/v1/images/predator2_feature-poster_584x800_5d26905d.jpeg?region=0%2C0%2C584%2C800",
        ),
        (
          "Predators",
          2010,
          "Action, Sci-Fi",
          "A group of elite warriors are hunted by members of a merciless alien race known as Predators.",
          "https://m.media-amazon.com/images/M/MV5BNjFmNDNlMGItMDQxMS00ZWMxLTg4MmQtMTBiNWU3ZDU1Nzk1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
        ),
        (
          "The Predator",
          2018,
          "Action, Sci-Fi",
          "A young boy accidentally triggers the Predators' return to Earth. Only a ragtag crew of ex-soldiers can prevent the end of the human race.",
          "https://granitebaytoday.org/wp-content/uploads/2018/10/predator-new.jpg",
        ),
        (
          "Prey",
          2022,
          "Action, Horror",
          "A Native American woman fights for her life against the most advanced killing machine.",
          "https://i0.wp.com/screen-connections.com/wp-content/uploads/2023/08/Prey-4K.UHD_.Coverart.jpg",
        ),
        (
          "Alien vs. Predator",
          2004,
          "Action, Horror, Sci-Fi",
          "During an archaeological expedition in Antarctica, a team of scientists finds themselves caught in a battle between two alien species.",
          "https://www.avpgalaxy.net/wordpress/wp-content/uploads/2022/04/avp-ultimate-prey-review-00.jpg",
        ),
        (
          "Aliens vs. Predator: Requiem",
          2007,
          "Action, Horror, Sci-Fi",
          "Warring alien and predator races descend on a rural Colorado town, where unsuspecting residents must band together for any chance of survival.",
          "https://media.themoviedb.org/t/p/w500/jCyJN1vj8jqJJ0vNw4hDH2KlySO.jpg",
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

def movies_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM movies
        WHERE id = ?
        """,
        (id,),
    ).fetchone()
    return dict(row)


def movies_update_by_id(id, name, width, height):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE movies SET name = ?, width = ?, height = ?
        WHERE id = ?
        RETURNING *
        """,
        (name, width, height, id),
    ).fetchone()
    conn.commit()
    return dict(row)

  
if __name__ == "__main__":
    initial_setup()