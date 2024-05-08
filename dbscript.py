# Import Flask and SQLAlchemy
from flask import Flask
from app import db  # Adjusted import to absolute from relative
from app.models import Zone, Item, Dungeon

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eldenring.db'  # Ensure this points to your actual database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def add_data():
    # Ensure we are in an app context
    with app.app_context():
        # Query for an existing zone by its name
        zone_name = "Stormveil Castle"  # Adjust the name as needed
        zone = Zone.query.filter_by(name=zone_name).first()
        if not zone:
            print(f"No zone found with the name {zone_name}")
            return  # Optionally, create the zone here if it does not exist

        # Creating a new item within that zone
        new_item = Item(name="Hookclaws", description="Enhances guard counters.", acquired=False, icon="path_to_icon.png", zone=zone)
        db.session.add(new_item)

        # Commit the changes to the database
        db.session.commit()
        print("Item added successfully.")

def add_item_dungeon(dungeon_name="Siofra River.", item_name="Golden Seed"):
    # Check if the dungeon already exists
    dungeon = Dungeon.query.filter_by(name=dungeon_name).first()
    
    # If the dungeon does not exist, create and add it to the database
    if dungeon is None:
        dungeon = Dungeon(name=dungeon_name)
        db.session.add(dungeon)
        db.session.commit()

    # Check if the item already exists in the dungeon
    item = Item.query.filter_by(name=item_name, dungeon=dungeon).first()

    # If the item does not exist, create and add it to the dungeon
    if item is None:
        item = Item(name=item_name, dungeon=dungeon)
        db.session.add(item)
        db.session.commit()
        return f"Added item '{item_name}' to new/existing dungeon '{dungeon_name}'."
    else:
        return f"Item '{item_name}' already exists in dungeon '{dungeon_name}'."


# Run this function to add the item
if __name__ == "__main__":
    add_item_dungeon()
