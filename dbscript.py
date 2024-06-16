# Import the factory function for creating the Flask app
from app import create_app, db  # Assuming db and create_app are accessible here
from app.models import Zone, Item, Dungeon

# Add new data after database rebuild
# Create the Flask application instance using the factory function
app = create_app()

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
        new_item = Item(name="Hookclaws", description="Hookclaws", acquired=False, icon="path_to_icon.png", zone=zone)
        db.session.add(new_item)

        # Commit the changes to the database
        db.session.commit()
        print("Item added successfully.")

def add_item_dungeon(dungeon_name="Siofra River", item_name="Golden Seed"):
    with app.app_context():
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
    result = add_data()
    print(result)
