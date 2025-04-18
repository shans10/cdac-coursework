import logging
import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Grievance
from forms import RegistrationForm, LoginForm, GrievanceForm, UpdateStatusForm

# Initialize app and configurations
app = Flask(__name__)
# Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{
    os.path.join(app.instance_path, 'database.db')}"
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

logging.basicConfig(level=logging.DEBUG)


# Initialize extensions
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)  # Add user to the session
        db.session.commit()  # Commit changes to the database
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check username and password.', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if current_user.is_admin:
        grievances = Grievance.query.all()
        return render_template('admin.html', grievances=grievances, form=UpdateStatusForm())
    else:
        grievances = Grievance.query.filter_by(user_id=current_user.id).all()
        form = GrievanceForm()
        return render_template('grievance.html', grievances=grievances, form=form)


@app.route('/submit_grievance', methods=['POST'])
@login_required
def submit_grievance():
    form = GrievanceForm()
    if form.validate_on_submit():
        grievance = Grievance(
            title=form.title.data,
            description=form.description.data,
            user_id=current_user.id
        )
        db.session.add(grievance)
        db.session.commit()
        flash('Grievance submitted successfully!', 'success')
    else:
        flash('Failed to submit grievance. Please check your input.', 'danger')
    return redirect(url_for('dashboard'))


@app.route('/grievances', methods=['GET'])
def grievances():
    form = GrievanceForm()  # Create a form object if needed for any other purposes

    # Fetch grievances from the database
    grievances = Grievance.query.filter_by(user_id=current_user.id).all()

    return render_template('grievance.html', grievances=grievances, form=form)


@app.route('/delete_grievance/<int:id>', methods=['POST'])
@login_required  # Ensure the user is logged in before they can delete
def delete_grievance(id):
    # Retrieve the grievance by id or return a 404 if not found
    grievance = Grievance.query.get_or_404(id)

    # Ensure that the grievance belongs to the current user (optional, if you want to restrict deletion to the creator)
    if grievance.user_id != current_user.id:
        flash('You cannot delete this grievance.', 'danger')
        return redirect(url_for('grievances'))

    try:
        db.session.delete(grievance)  # Delete the grievance
        db.session.commit()  # Commit the transaction
        flash('Grievance deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()  # Rollback if there's an error
        flash('Failed to delete grievance. Please try again later.', 'danger')

    return redirect(url_for('grievances'))  # Redirect to the grievances page


@app.route('/update_status/<int:grievance_id>', methods=['POST'])
@login_required
def update_status(grievance_id):
    if not current_user.is_admin:
        flash('Unauthorized access.', 'danger')
        return redirect(url_for('dashboard'))

    form = UpdateStatusForm()
    if form.validate_on_submit():
        grievance = Grievance.query.get_or_404(grievance_id)
        grievance.status = form.status.data
        db.session.commit()
        flash('Status updated successfully!', 'success')
    else:
        flash('Failed to update status. Please try again.', 'danger')
    return redirect(url_for('dashboard'))


# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Automatically create the tables if they don't exist
    app.run(debug=True)
