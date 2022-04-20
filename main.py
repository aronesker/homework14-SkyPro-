from flask import Flask, render_template
from utils import get_title_by_name, get_title_year_to_year, get_title_by_rating, title_genre

app = Flask(__name__)


@app.route('/movie/<title>')
def search_page(title):
    """ Выводим фильмы, имеющие одно вхождение с названием фильма"""
    result_search = get_title_by_name(title)
    return render_template("search.html", title=title, result_search=result_search)


@app.route('/movie/<first_year>/<last_year>')
def search_title_by_year(first_year, last_year):
    """ Выводим фильмы, имеющие одно вхождение с названием фильма"""
    result_film_by_year = get_title_year_to_year(first_year, last_year)
    return render_template("film_by_year.html", first_year=first_year, last_year=last_year,
                           result_film_by_year=result_film_by_year)


@app.route('/rating/<rating>')
def title_rating_age(rating):
    """ Выводим фильмы, по возрастному рейтингу"""
    result_film_rating_age = get_title_by_rating(rating)
    return render_template("film_rating_age.html", result_film_rating_age=result_film_rating_age)


@app.route('/genre/<genre>')
def title_by_genre(genre):
    """ Выводим фильмы, по жанру"""
    result_film_genre = title_genre(genre)
    return render_template("film_genre.html", result_film_genre=result_film_genre)


if __name__ == "__main__":
    app.run()
