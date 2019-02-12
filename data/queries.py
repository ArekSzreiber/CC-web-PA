from data import data_manager as data


def get_shows():
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
            homepage;
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


def get_columns_names():
    return data.execute_select("""
        SELECT
            DISTINCT column_name
        FROM information_schema.columns
        WHERE
            table_catalog = 'web_pa'
	        AND table_schema = 'public';
    """)


def get_sorted_shows(page=1, column="rating", reverse=False):
    page -= 1  # n-th page has index (n-1)
    number_at_page = 15
    if reverse:
        direction = "DESC"
    else:
        direction = "ASC"
    columns = get_columns_names()
    columns = [d['column_name']for d in columns]
    if column not in columns:
        print(column)
        print(columns)
        column = 'title'
    statement = """
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
        ORDER BY """ + column + " " + direction + """
        OFFSET %(ignored)s
        LIMIT %(amount)s;
    """
    variables = {'ignored': page*number_at_page,
                 'amount': number_at_page}
    return data.execute_select(statement, variables)


def get_show_by_id(id):
    show_list = data.execute_select("""
        SELECT
            title,
            year,
            overview,
            runtime,
            homepage,
            rating,
            STRING_AGG(DISTINCT genres.name, ', ') AS genres,
            STRING_AGG(DISTINCT actors.name, ', ') AS actors,
            trailer
        FROM shows
        JOIN show_genres
            ON show_genres.show_id = shows.id
        JOIN genres
            ON genres.id = show_genres.genre_id
        JOIN show_characters
            ON show_genres.show_id = shows.id
        JOIN actors
            ON actors.id = show_characters.actor_id
        WHERE
            shows.id = %(id)s
        GROUP BY
            title,
            year,
            overview,
            runtime,
            homepage,
            rating,
            show_characters.show_id,
            show_genres.show_id,
            trailer;
    """, {'id': id})
    return show_list[0]


def get_seasons_by_show_id(show_id):
    seasons = data.execute_select("""
        SELECT
            title
        FROM
            seasons
        WHERE
            show_id = %(id)s
        ORDER BY seasons ASC;
    """, {'id': show_id})
    return seasons

def get_season_by_id(season_id):
    seasons = data.execute_select("""
        SELECT
            id,
            season_number,
            title,
            overview
        FROM seasons
        WHERE id = %(id)s;
    """, {'id': season_id})
    try:
        return seasons[0]
    except IndexError:
        return {}


def get_episodes_by_season_id(season_id):
    episodes = data.execute_select("""
        SELECT
            id,
            title,
            episode_number
        FROM episodes
        WHERE season_id = %(season_id)s;
    """, {'season_id': season_id})
    try:
        return episodes
    except IndexError:
        return {}
