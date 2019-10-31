from flask import Blueprint,render_template
from app.requests import get_countries_by_continents


main = Blueprint('main',__name__)
@main.route('/')
def home():
    return render_template('home.html')

@main.route('/continental/<continent>')
@main.route('/continental/<continent>/<sub_region>')
def continent(continent, sub_region = None):
    countries = get_countries_by_continents(continent)
    return render_template('continental.html',countries = countries, continent = continent)