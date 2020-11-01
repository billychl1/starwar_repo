from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ShipRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    hyperdriverating = db.Column(db.Float())

    def __init__(self, id, name, hyperdriverating):
        self.id = id
        self.name = name
        self.hyperdriverating = hyperdriverating

    def __repr__(self):
        return "<Name %r>" % (self.name)
    

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'name': self.name,
           'hyperdriverating'  : 'No Hyperdrive' if (str(self.hyperdriverating) == "999") else self.hyperdriverating
       }


