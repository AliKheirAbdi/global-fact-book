from flask import Blueprint,render_template
from app.requests import get_all_countries



main = Blueprint('main',__name__)


@main.route('/')
def home():
    all_countries = get_all_countries()
    return render_template('home.html')
