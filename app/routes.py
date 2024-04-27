from flask import Blueprint, render_template
from flask import request, redirect, url_for, session
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

@main.route('/acquire_item/<int:item_id>')
def acquire_item(item_id):
    if 'acquired_items' not in session:
        session['acquired_items'] = []
    session['acquired_items'].append(item_id)  # Add the item ID to the session
    session.modified = True  # Ensure the session is marked as modified
    return 'Item acquired'

@main.route('/my_items')
def my_items():
    items_acquired = session.get('acquired_items', [])
    # Fetch item details from the database based on IDs stored in the session
    items = Item.query.filter(Item.id.in_(items_acquired)).all() if items_acquired else []
    return render_template('my_items.html', items=items)

