from db import db

class Cart(db.Model):
	__tablename__ = 'carts'
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	totalPrice = db.Column(db.Integer)
	tax = db.Column(db.Integer)
	items = db.relationship('Snake', backref='cart')


	@classmethod	
	def create(cls, **kwargs):
		cart = Cart(**kwargs)
		db.session.add(cart)
		db.session.commit()
		return cart

	@classmethod
	def from_user_id(cls, user_id):
		return cls.query.filter(cls.user_id == user_id).first()

