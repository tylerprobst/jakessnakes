from db import db
# get rid of jakes id
# add age column
# add locale column


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
	cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))

	@classmethod	
	def create(cls, **kwargs):
		snake = Snake(**kwargs)
		db.session.add(snake)
		db.session.commit()
		return snake

