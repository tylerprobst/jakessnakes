from db import db 

class Morph(db.Model):
	__tablename__ = 'morphs'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), index=True, nullable=False)
	snakes = db.relationship('Snake', backref='morph')