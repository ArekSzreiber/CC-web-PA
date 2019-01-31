from data import data_manager as data


def get_shows():
    return data.execute_select('SELECT id, title FROM shows;')


def get_season(show_title, season_number):
    return data.execute_select("""
        SELECT
            shows.title,
            shows.rating,
            shows.year
        FROM
            shows
        JOIN seasons ON shows.id = seasons.show_id
        WHERE
            shows.title = %(title)s
            AND seasons.season_number = %(season)s
    """, {'title': show_title,
          'season': season_number})
