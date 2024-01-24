from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import stripe

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use your preferred database
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Initialize Stripe
stripe.api_key = 'your_stripe_secret_key'  # Replace with your actual Stripe secret key

# Define User model
class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	# Add other user fields as needed

# Define Product model
class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	price = db.Column(db.Float, nullable=False)
	description = db.Column(db.Text)
	# Add other product fields as needed

# Define Order model
class Order(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	# Add other order fields as needed

# Flask-Login callback to load a user
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
	products = Product.query.all()
	return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
	product = Product.query.get_or_404(product_id)
	return render_template('product_detail.html', product=product)

@app.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
	# Add product to the user's shopping cart (session)
	# Update the session cart and redirect to the cart page
	return redirect(url_for('cart'))

@app.route('/cart')
@login_required
def cart():
	# Display the user's shopping cart
	# Calculate total price
	return render_template('cart.html')

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
	if request.method == 'POST':
		# Handle the payment using the Stripe API
		# Create an order in the database and update product quantities
		flash('Payment successful!', 'success')
		return redirect(url_for('home'))
	return render_template('checkout.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	# Handle user login
	return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	# Handle user registration
	return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('home'))

# Run the app
if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)
