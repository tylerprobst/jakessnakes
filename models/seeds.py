from db import db
from Morph import * 

MORPH_NAMES = ['T+ Argentine',
			   'Black Eyed Anery',
			   'Albino']

for cat in Morph.query.all():
	db.session.delete(cat)
db.session.commit()

for name in MORPH_NAMES:
	db.session.add(Morph(name=name))
db.session.commit()