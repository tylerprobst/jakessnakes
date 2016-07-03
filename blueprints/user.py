from flask import Blueprint, flash, Flask, g, redirect, render_template, request, session
from models import *
from helpers import *

user = Blueprint("user", __name__)

app = Flask(__name__)
app.config.from_object('config')

@user.route('/users', methods=['GET'])
@logged_in
def index():
	return render_template('users.html', current_user=current_user(), users=filter(lambda x: x.id != g.current_user.id, User.query.all()))

@user.route('/posts', methods=['GET', 'POST'])
@logged_in
def post():
	if request.method == 'GET':
		return render_template('posts.html', posts=Post.query.all())
	elif request.method == 'POST':
		body = request.form.get('body')
		user = current_user()
		Post.create(body=body, user_id=user.id)
		return redirect('/profile/{0}'.format(user.id))

@user.route('/profile/<path:user_id>', methods=['GET'])
@logged_in
def profile(user_id):
	if request.method == 'GET':
		user = User.query.filter(User.id == user_id).first()
		return render_template('profile.html', user=user, current_user=current_user())

@user.route('/comment', methods=['POST'])
@logged_in
def comment():
	if request.method == 'POST':
		curr_user = current_user()
		user_id = request.form.get('user_id')
		body = request.form.get('body')
		post_id = request.form.get('post_id')
		Comment.create(body=body, post_id=post_id, user_id=curr_user.id)
		return redirect('/profile/{0}'.format(user_id))

@user.route('/comment/delete', methods=['POST'])
@logged_in
def delete_comment():
	if request.method == 'POST':
		user_id = request.form.get('user_id')
		comment_id = request.form.get('comment_id')
		comment = Comment.from_id(comment_id)
		comment.delete()
		flash('Comment deleted')
		return redirect('/profile/{0}'.format(user_id))

