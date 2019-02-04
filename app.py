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
        return render_template('index.html', shows=shows)
    except Exception as e:
        return "Error 500"


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/shows/<int:show_id>/')
def route_details(show_id):
#try:
    show = queries.get_show_by_id(show_id)
    return render_template('index.html', show=show)
#except Exception as e:
#    return "Error 500"


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
