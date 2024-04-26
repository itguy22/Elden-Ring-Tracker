from flask import Blueprint, render_template
from flask import request, redirect, url_for
from .models import db, Item

main = Blueprint('main', __name__)

@main.route('/add-item', methods=['POST'])
def add_item():
    if request.method == 'POST':
        new_item = Item(
            name=request.form['name'],
            description=request.form['description'],
            acquired=request.form.get('acquired', False),
            icon=request.form['icon']  # Assuming this is a path provided by the form
        )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('main.show_items'))

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/zone/<zone_name>')
def zone(zone_name):
    # Dummy data; you would fetch real data from the database
    items = [{'name': 'Stonesword Key', 'acquired': False}, {'name': 'Glintstone Staff', 'acquired': True}]
    return render_template('zone.html', zone_name=zone_name, items=items)
