from db import db

class Snake(db.Model):
	__tablename__ = 'snakes'
	id = db.Column(db.Integer, primary_key=True)
	morph_id = db.Column(db.Integer, db.ForeignKey('morphs.id'))
	jakes_id = db.Column(db.String(100), unique=True, nullable=False)
	title = db.Column(db.String(100))
	description = db.Column(db.String(10000), nullable=False)
	price = db.Column(db.Integer, nullable=False)
	gender = db.Column(db.String(1), nullable=False)
	images = db.relationship('Image', backref='snake')
	in_cart = db.Column(db.Boolean, default=False)
	cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))

	
	def addToCart(self, cart_id):
		if self.in_cart:
			return False
		else:
			self.cart_id = cart_id
			self.in_cart = True
			db.session.commit()
			return True

	@classmethod	
	def create(cls, **kwargs):
		snake = Snake(**kwargs)
		db.session.add(snake)
		db.session.commit()
		return snake

	@classmethod
	def from_id(cls, snake_id):
		return cls.query.filter(cls.id == snake_id).first()

	

