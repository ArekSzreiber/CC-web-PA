from flask import Flask, render_template, request, url_for
from data import queries

app = Flask('codecool_series')


@app.route('/')
@app.route('/page/<int:page>')
def index(page=1):
    try:
        column = request.args.get('column', 'rating')
        reverse = request.args.get('reversed', False)
        if reverse == "False":
            reverse = False
        shows = queries.get_sorted_shows(page, column, reverse)
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
