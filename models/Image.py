from db import db

class Image(db.Model):
	__tablename__ = 'images'
	id = db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.String(255), unique=True, nullable=False) 
	snake_id = db.Column(db.Integer, db.ForeignKey('snakes.id'))

	@classmethod
	def create(cls, **kwargs):
		image = Image(**kwargs)
		db.session.add(image)
		db.session.commit()
		return image
