# Import Flask and SQLAlchemy
from flask import Flask
from app import db  # Adjusted import to absolute from relative
from app.models import Zone, Item

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
        new_item = Item(name="Academy Glintstone Key", description="Key to open the academy's two sealed gates.", acquired=False, icon="path_to_icon.png", zone=zone)
        db.session.add(new_item)

        # Commit the changes to the database
        db.session.commit()
        print("Item added successfully.")

# Run this function to add the item
if __name__ == "__main__":
    add_data()
