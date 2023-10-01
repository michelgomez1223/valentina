from flask import Blueprint, render_template

index = Blueprint('index',
                __name__)

@index.route('/')
def index_view():
    return render_template('index.html')                