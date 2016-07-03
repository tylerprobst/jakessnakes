from flask import Flask, session, g
from db import db

class Comment(db.Model):
	__tablename__ = 'comments'
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(255), nullable=False)		
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

	def from_id(self, comment_id):
		return Comment.query.filter(Comment.id == comment_id).first()

	def delete(self):
		db.session.delete(self)
		db.session.commit()
	
	@classmethod
	def create(cls, *args, **kwargs):
		comment = Comment(*args, **kwargs)
		db.session.add(comment)
		db.session.commit()

