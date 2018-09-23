from models import User, City
from PIL import Image
import requests
from flask import render_template, flash, redirect, url_for, request, abort
from weatherwidget.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from weatherwidget.models import User, City
from weatherwidget import app, db, bcrypt
import random, os
from flask_login import login_user, current_user, logout_user, login_required
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=11947201764b5cdd68cd4978b5632046'

@app.route("/")
@app.route("/home ")
def home():
    cities = City.query.all()
    city_data = []
    for city in cities:
        r = requests.get(url.format(city.title)).json()

        city = {
            'id' : city.id,
            'title' : city.title,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
        city_data.append(city)
    return render_template('index.html',cities=city_data)

@app.route("/about")
def about():
    return 'About page'

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pwd =bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = random.randint(1,21)*5
    #_, f_ext = os.path.splitext(form_picture.filename)
    _ext = (form_picture.filename)
    picture_fn = _ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='images/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)

@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        city = City(title=form.title.data,user_id=current_user.id)
        db.session.add(city)
        db.session.commit()
        flash('{} added!'.format(form.title.data),'success')
        return redirect(url_for('home'))
    return render_template('create_post.html',title='New Post',form=form)

@app.route("/post/<int:id>/delete", methods=['POST'])
@login_required
def delete_post(id):
    city = City.query.get_or_404(id)
    if city.author != current_user:
        abort(403)
    db.session.delete(city)
    db.session.commit()
    flash('{} has been removed'.format(city.title), 'success')
    return redirect(url_for('home'))
