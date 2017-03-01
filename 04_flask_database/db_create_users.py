from app import db
from app.models import User

db.create_all()
# insert data
db.session.add(User(nickname="michael", email="michael@realpython.com"))
db.session.add(User(nickname="admin", email="ad@min.com"))
db.session.add(User(nickname="mike", email="mike@herman.com"))

# commit the changes
db.session.commit()