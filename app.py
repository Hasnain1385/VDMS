from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///vehicles.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg_no = db.Column(db.String(20), unique=True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    copy = db.Column(db.String(50))
    engine_no = db.Column(db.String(50))
    chasis_no = db.Column(db.String(50))
    registered_to = db.Column(db.String(100))
    token = db.Column(db.String(50))
    
    # Buyer details
    buyer_name = db.Column(db.String(100))
    buyer_cnic = db.Column(db.String(15))
    buyer_address = db.Column(db.Text)
    buyer_father = db.Column(db.String(100))
    buyer_contact = db.Column(db.String(20))
    purchase_date = db.Column(db.Date)
    
    # Seller details
    seller_name = db.Column(db.String(100))
    seller_cnic = db.Column(db.String(15))
    seller_address = db.Column(db.Text)
    seller_father = db.Column(db.String(100))
    seller_contact = db.Column(db.String(20))
    seller_witness = db.Column(db.String(100))
    
    # Deal details
    deal_date = db.Column(db.Date)
    deal_price = db.Column(db.Float)
    advance_amount = db.Column(db.Float)
    balance_amount = db.Column(db.Float)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    vehicles = Vehicle.query.filter(
        (Vehicle.reg_no.ilike(f'%{query}%')) |
        (Vehicle.make.ilike(f'%{query}%')) |
        (Vehicle.model.ilike(f'%{query}%')) |
        (Vehicle.buyer_name.ilike(f'%{query}%')) |
        (Vehicle.seller_name.ilike(f'%{query}%'))
    ).all()
    return render_template('search_results.html', vehicles=vehicles)

@app.route('/vehicles')
def vehicle_list():
    vehicles = Vehicle.query.all()
    return render_template('search_results.html', vehicles=vehicles, title="All Vehicles")

@app.route('/buyers-sellers')
def buyers_sellers():
    vehicles = Vehicle.query.all()
    return render_template('search_results.html', vehicles=vehicles, title="Buyers & Sellers")

@app.route('/deals')
def deals():
    vehicles = Vehicle.query.all()
    return render_template('search_results.html', vehicles=vehicles, title="Deal Management")

@app.route('/add_deal', methods=['GET', 'POST'])
def add_deal():
    if request.method == 'POST':
        try:
            vehicle = Vehicle(
                reg_no=request.form['reg_no'],
                make=request.form['make'],
                model=request.form['model'],
                copy=request.form['copy'],
                engine_no=request.form['engine_no'],
                chasis_no=request.form['chasis_no'],
                registered_to=request.form['registered_to'],
                token=request.form['token'],
                
                buyer_name=request.form['buyer_name'],
                buyer_cnic=request.form['buyer_cnic'],
                buyer_address=request.form['buyer_address'],
                buyer_father=request.form['buyer_father'],
                buyer_contact=request.form['buyer_contact'],
                purchase_date=datetime.strptime(request.form['purchase_date'], '%Y-%m-%d').date(),
                
                seller_name=request.form['seller_name'],
                seller_cnic=request.form['seller_cnic'],
                seller_address=request.form['seller_address'],
                seller_father=request.form['seller_father'],
                seller_contact=request.form['seller_contact'],
                seller_witness=request.form['seller_witness'],
                
                deal_date=datetime.strptime(request.form['deal_date'], '%Y-%m-%d').date(),
                deal_price=float(request.form['deal_price']),
                advance_amount=float(request.form['advance_amount']),
                balance_amount=float(request.form['balance_amount'])
            )
            db.session.add(vehicle)
            db.session.commit()
            flash('Deal added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error adding deal: {str(e)}', 'error')
            return redirect(url_for('add_deal'))
    
    return render_template('add_deal.html')

@app.route('/vehicle/<int:id>')
def vehicle_details(id):
    vehicle = Vehicle.query.get_or_404(id)
    return render_template('vehicle_details.html', vehicle=vehicle)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # Get host from environment variable or default to '0.0.0.0'
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(host=host, port=port, debug=True) 