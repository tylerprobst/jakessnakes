from flask import Flask, Blueprint, render_template, redirect, session, g, request, send_from_directory
from models import *
from blueprints import *
from helpers import *
import os, random, string

application = Flask(__name__)
application.config.from_object('config')

@application.teardown_appcontext
def shutdown_session(exception=None):
        db.session.remove()

@application.route('/')
def home():
	user = current_user()
	username = None
	if user:
		username = user.username
	return render_template('home.html', snakes=Snake.query.all(), current_user=user)

@application.route('/create', methods=['GET', 'POST'])
def create():
	if request.method == 'GET':
		return render_template('create_snake.html', morphs=Morph.query.all())
	if request.method == 'POST':
		morph_id = request.form.get('morph-id')
		jakes_id = request.form.get('jakes-id')
		title = request.form.get('title')
		price = request.form.get('price')
		gender = request.form.get('gender')
		description = request.form.get('description')
		snake = Snake.create(morph_id=morph_id, jakes_id=jakes_id, title=title, price=price, gender=gender, description=description)
		for img_file in request.files.getlist('file[]'):
			if img_file:
				filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(26)) + ".jpeg"
				img_file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
				Image.create(filename=filename, snake_id=snake.id)		
		return redirect('/')

@application.route('/snakes', methods=['GET'])
def snakes():
	return render_template('snakes.html', snakes=Snake.query.all())

@application.route('/snake/<path:snake_id>', methods=['GET'])
def snake(snake_id):
	snake = Snake.query.filter(Snake.id == snake_id).first()
	return render_template('snake.html', snake=snake)

@application.route('/morphs', methods=['GET'])
def morphs():
	return render_template('morphs.html', morphs=Morph.query.all())

@application.route('/assets/<path:path>')
def assets(path):
	return send_from_directory('assets', path)

@application.route('/uploads/<path:path>')
def uploads(path):
	return send_from_directory('uploads', path)

app.register_blueprint(auth.auth, session=session, g=g)
app.register_blueprint(user.user, session=session, g=g)

if __name__ =='__main__':
	application.run()