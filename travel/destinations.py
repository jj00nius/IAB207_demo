from flask import Flask, Blueprint, render_template, request
from .models import Destination, Comment
from .forms import DestinationForm

# Use of blueprints to group routes:
# name - first argument is blueprint name
# import name - second argument which helps to identify the root url for it
destbp = Blueprint('destination', __name__, url_prefix='/destinations')

@destbp.route('/<id>')
def show(id):
    destination = get_destination()
    return render_template('destinations/show.html', destination=destination)

@destbp.route('/create', methods = ['GET', 'POST'])
def create():
    print('Method type: ', request.method)
    form = DestinationForm()
    if form.validate_on_submit():
        print('Successfully created new travel destination')
        # return redirect(url_for('destination.create'))
    return render_template('destinations/create.html', form=form)

def get_destination():
    # Creating the description of Brazil
    b_desc = """Brazil is considered an advanced emerging economy.
       It has the ninth largest GDP in the world by nominal, and eight by PPP measures. 
       It is one of the world\'s major breadbaskets, being the largest producer of coffee for the last 150 years."""
    # Image location
    image_loc = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFyC8pBJI2AAHLpAVih41_yWx2xxLleTtdshAdk1HOZQd9ZM8-Ag'
    destination = Destination('Brazil', b_desc, image_loc, 'R$10')
    # Comment
    comment = Comment("Anshul", "Visited during the olympics, was great", '2023-08-12 11:00:00')
    destination.set_comments(comment)
    comment = Comment("Emma", "It's so postmodern", '2023-08-12 11:00:00')
    destination.set_comments(comment)
    comment = Comment("Andy", "Come to Brazil", '2023-08-12 11:00:00')
    destination.set_comments(comment)
    return destination