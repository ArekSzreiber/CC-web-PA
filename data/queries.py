from data import data_manager as data


def get_shows():
    return data.execute_select("""
        SELECT
            id,
            title
        FROM shows;
    """)


def get_most_rated(page=1):
    page -= 1  # n-th page has index (n-1)
    number_at_page = 15
    return data.execute_select("""
        SELECT
            DISTINCT shows.title,
            shows.year,
            shows.runtime,
            ARRAY_TO_STRING((ARRAY_AGG(DISTINCT genres.name))[1:3], ', ') AS genres,
            shows.rating,
            shows.trailer,
            shows.homepage
        FROM shows
        JOIN show_genres ON show_genres.show_id = shows.id
        JOIN genres ON genres.id = show_genres.genre_id
        GROUP BY
            title,
            year,
            runtime,
            rating,
            trailer,
            homepage
        ORDER BY rating DESC
        OFFSET %(ignored)s
        LIMIT %(amount)s;
    """, {'ignored': page*number_at_page,
          'amount': number_at_page})
