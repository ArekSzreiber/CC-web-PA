from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


def correct_int(number, default):
    if not type(number) is int:
        return default
    return number


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    shows = queries.get_shows()
    return render_template('design.html', shows=shows)


#/shows/<show>/seasons/<int:season>
@app.route('/season', methods=["POST"])
def route_season():
    show = request.form.get('show', '')
    season_nr = request.form.get('season', 1)
    season_nr = correct_int(season_nr, 1)
    seasons = queries.get_season(show, season_nr)
    header = ['Title',
              'Rating',
              'Year']
    return render_template('index.html',
                           seasons=seasons,
                           headers=header)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
