from flask import Blueprint, render_template, request, redirect, url_for
from .models import Destination
from . import db

mainbp = Blueprint('main', __name__)


@mainbp.route('/')
def index():
    # Query database for all destinations
    destinations = db.session.scalars(db.select(Destination)).all()
    return render_template('index.html', destinations=destinations)


# Search function
@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        # Query the database
        query = "%" + request.args['search'] + "%"
        destinations = db.session.scalars(db.select(Destination).where(Destination.description.like(query)))
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))
