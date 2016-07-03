from flask import Flask
from db import db


class Post(db.Model):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(1000), nullable=False)
	comments = db.relationship('Comment', backref='post', cascade='all, delete, delete-orphan', lazy=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	images = db.relationship('Image', backref='post', lazy=False)

	@classmethod
	def create(cls, *args, **kwargs):
		post = Post(*args, **kwargs)
		db.session.add(post)
		db.session.commit()
		return post
