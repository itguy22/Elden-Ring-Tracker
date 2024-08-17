from . import db

class Zone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    map_image = db.Column(db.String(255), nullable=True)
    items = db.relationship('Item', backref='zone', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    acquired = db.Column(db.Boolean, default=False)
    icon = db.Column(db.String(255), nullable=True)
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'), nullable=False)
    dungeon_id = db.Column(db.Integer, db.ForeignKey('dungeon.id'), nullable=True)  # This allows an item to optionally belong to a dungeon

class Dungeon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    acquired = db.Column(db.Boolean, default=False)
    icon = db.Column(db.String(255), nullable=True)
    items = db.relationship('Item', backref='dungeon', lazy=True)  # This establishes a relationship with items