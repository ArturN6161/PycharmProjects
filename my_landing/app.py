from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from wrkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from models import db, User, PortfolioItem

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this' # Change in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/')
def index():
    items = PortfolioItem.query.all()
    # Pass items to template. If empty, template might show defaults or nothing.
    # For now, we will modify index.html to use these items if present.
    return render_template('index.html', portfolio_items=items)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('admin'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin():
    items = PortfolioItem.query.all()
    return render_template('admin.html', items=items)

@app.route('/admin/add_item', methods=['POST'])
@login_required
def add_item():
    title = request.form.get('title')
    description = request.form.get('description')
    price = request.form.get('price')
    location = request.form.get('location')
    file = request.files['image']
    
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        new_item = PortfolioItem(title=title, description=description, price=price, location=location, image_filename=filename)
        db.session.add(new_item)
        db.session.commit()
        
    return redirect(url_for('admin'))

@app.route('/admin/delete_item/<int:id>', methods=['POST'])
@login_required
def delete_item(id):
    item = PortfolioItem.query.get_or_404(id)
    # Optional: Delete file from filesystem
    try:
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], item.image_filename))
    except:
        pass
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('admin'))

def create_admin():
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            hashed_pw = generate_password_hash('admin', method='scrypt')
            admin = User(username='admin', password_hash=hashed_pw)
            db.session.add(admin)
            db.session.commit()
            print("Admin user created!")

if __name__ == '__main__':
    create_admin()
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)
