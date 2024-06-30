from flask import Blueprint, render_template
from flask import request, redirect, url_for, session
from .models import db, Item, Zone
from flask import jsonify
from flask import Flask, jsonify
from . import db



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
    zones = Zone.query.all()
    return render_template('index.html', zones=zones)

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

@main.route('/api/zones')
def zones():
    zones = Zone.query.all()
    zones_data = [
        {
            'name': zone.name,
            'description': zone.description,
            'items': [
                {'name': item.name, 'description': item.description, 'acquired': item.acquired}
                for item in zone.items
            ]
        } for zone in zones
    ]
    return jsonify(zones_data)

@main.route('/zone/<int:zone_id>', methods=['GET', 'POST'])
def zone_detail(zone_id):
    zone = Zone.query.get_or_404(zone_id)
    items = Item.query.filter_by(zone_id=zone_id).all()

    if request.method == 'POST':
        # Update session with the items acquired status
        acquired_items = {key[5:]: True for key in request.form.keys() if key.startswith('item_')}
        session['acquired_items'] = acquired_items
        session.modified = True
        return redirect(url_for('zone_detail', zone_id=zone_id))

    acquired_items = session.get('acquired_items', {})
    return render_template('zone_detail.html', zone=zone, items=items, acquired_items=acquired_items)



@main.route('/save_item_state', methods=['POST'])
def save_item_state():
    if 'acquired_items' not in session:
        session['acquired_items'] = {}

    for key in request.form:
        item_id = int(key.replace('item', ''))
        session['acquired_items'][item_id] = request.form[key] == 'on'

    session.modified = True  # Ensure changes to the session are saved
    return jsonify(status="success", message="Items updated successfully in session!")