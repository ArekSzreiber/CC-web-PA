from flask import Flask, render_template, request, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
@app.route('/page/<int:page>')
def index(page=1):
    try:
        shows = queries.get_most_rated(page)
        return render_template('index.html', shows=shows)
    except Exception as e:
        return "Error 500"


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
