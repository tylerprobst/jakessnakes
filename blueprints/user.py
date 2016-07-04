from flask import Blueprint, flash, Flask, g, redirect, render_template, request, session
from models import *
from helpers import *

user = Blueprint("user", __name__)

app = Flask(__name__)
app.config.from_object('config')

@user.route('/cart', methods=['GET'])
@logged_in
def cart():
	if request.method == 'GET':
		user = current_user()
		cart = user.cart
		print getattr(cart, 'items')
		return render_template('cart.html', current_user=user, cart=cart)

@user.route('/add-to-cart', methods=['POST'])
@logged_in
def addToCart():
	if request.method == 'POST':
		user = current_user()
		cart = Cart.from_user_id(user.id)
		snake_id = request.form.get('snake_id')
		snake = Snake.from_id(snake_id)
		result = snake.addToCart(cart.id)
		if result:
			flash('Snake Added To Cart')
		else: 
			flash('Snake Not Added to Cart')
		return redirect('/cart')

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

