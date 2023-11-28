from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db = SQLAlchemy()
db.init_app(app)

class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(250), unique=True, nullable=False)
	author = db.Column(db.String(250), nullable=False)
	rating = db.Column(db.Float, nullable=False)

def __repr__(self):
		return f'<Book {self.title}>'

with app.app_context():
	db.create_all()
	
with app.app_context():
	new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
	db.session.add(new_book)
	db.session.commit()

# @app.route('/')
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)