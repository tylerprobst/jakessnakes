from db import db

class Cart(db.Model):
	__tablename__ = 'carts'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	totalPrice = db.Column(db.Integer, nullable=False)
	tax = db.Column(db.Integer, nullable=False)
	items = db.relationship('Snake', backref='cart')

	@classmethod	
	def create(cls, **kwargs):
		cart = Cart(**kwargs)
		db.session.add(cart)
		db.session.commit()
		return cart

