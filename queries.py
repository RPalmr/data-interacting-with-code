# pylint: disable=missing-docstring, C0103

def directors_count(db):
    # Write a SQL query to count the number of directors in the database
    query = "SELECT COUNT(*) FROM directors"
    db.execute(query)
    result = db.fetchone()

    # The result is a tuple with a single value, so we extract that value
    if result:
        count = result[0]
        return count

    return 0


def directors_list(db):
    # Write an SQL query to fetch all director names and sort them alphabetically
    query = """ SELECT d.name FROM directors AS d ORDER BY d.name """
    db.execute(query)
    results = db.fetchall()

    # Extract director names from the results and return them in a list
    director_names = [result[0] for result in results]
    return director_names


def love_movies(db):
    # SQL query select movies with the exact word "love" in their title, excluding "Cloverfield"
    query = """
        SELECT title
        FROM movies
        WHERE UPPER(title) LIKE '% LOVE %'
        OR UPPER(title) LIKE 'LOVE %'
        OR UPPER(title) LIKE '% LOVE'
        OR UPPER(title) LIKE 'LOVE'
        OR UPPER(title) LIKE '% LOVE''%'
        OR UPPER(title) LIKE '% LOVE.'
        OR UPPER(title) LIKE 'LOVE,%'
        ORDER BY title
    """

    results = db.execute(query)
    return [row[0] for row in results]


def directors_named_like_count(db, name):
    # Write an SQL query to count directors whose names contain the given word
    query = """SELECT COUNT(*) FROM directors WHERE name LIKE ?"""
    db.execute(query, ('%' + name + '%',))
    result = db.fetchone()

    # Extract the count from the result and return it
    count = result[0] if result else 0
    return count

def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = f"""SELECT m.id, m.title, m.minutes
                FROM movies as m
                WHERE m.minutes >= {min_length}
                ORDER BY m.title"""
    db.execute(query)
    results = db.fetchall()
    movie = [result[1] for result in results]
    print(movie)
    return movie
