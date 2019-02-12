from flask import Flask, render_template, request, url_for, session
from data import queries

app = Flask('codecool_series')

app.secret_key = b'\x12\x06\x97O\x8aaw\xadW\x18\xa7\x08%n\x7f\x1a_\xb6\xe03\xf3\xe4\x9f'


def make_embedded(youtube_link):
    youtube_link = youtube_link.replace('watch?v=', 'embed/')
    return youtube_link.replace('http', 'https')  # seems to work only for https


@app.route('/')
@app.route('/page/<int:page>')
def index(page=1):
    try:
        column = request.args.get('column', 'rating')
        previous_column = session.get('previous_column', 'rating')
        reverse = session.get('order', False)
        if column == previous_column:
            reverse = not reverse
        else:
            reverse = False
        session['previous_column'] = column
        session['order'] = reverse
        shows = queries.get_sorted_shows(page, column, reverse)
        return render_template('index.html', shows=shows, page=page)
    except Exception as e:
        return "Error 500"


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows/<int:show_id>/')
def route_details(show_id):
    try:
        show = queries.get_show_by_id(show_id)
        show['trailer'] = make_embedded(show.get('trailer'))
        seasons = queries.get_seasons_by_show_id(show_id)
        return render_template('index.html',
                               show=show,
                               seasons=seasons)
    except Exception as e:
        return "Error 500"


@app.route('/seasons/<int:season_id>/')
def show_season(season_id):
#try:
    season = queries.get_season_by_id(season_id)
    episodes = queries.get_episodes_by_season_id(season_id)
    return render_template('index.html',
                           season=season,
                           episodes=episodes)
#except Exception as e:
#return "Error 500"


@app.route('/episodes/<int:episode_id>')
def show_episode(episode_id=1):
    return "blank page"


@app.route('/genres/<int:genre_id>')
def show_shows_with_genre(genre_id=1):
    try:
        shows = queries.get_shows_by_genre_id(genre_id)
        genre_name = queries.get_genre_name(genre_id)
        return render_template('index.html',
                               shows_by_genre=shows,
                               genre=genre_name)
    except Exception as e:
    return "Error 500"

def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
