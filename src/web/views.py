from flask import render_template, url_for, redirect, request, flash
from flask_babel import get_locale
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from test_ssh import scan
from web import app, forms, db, login_manager
from web.forms import RegistrationForm, LoginForm
from web.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    return redirect(url_for('tasks'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    next_page = request.args.get('next')

    if not next_page or url_parse(next_page).netloc != '':
        next_page = url_for('index')

    if current_user.is_authenticated:
        return redirect(next_page)

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)

        return redirect(next_page)

    return render_template('login.html', form=form, next=next_page)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            language=form.language.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    form.language.process_data(get_locale())

    return render_template('register.html', form=form)


@login_manager.unauthorized_handler
def unathorized_user():
    return_url = url_for('index')
    app.logger.debug(f'request.path: {request.path}')

    if request.path:
        parsed_url = url_parse(request.path)
        return_url = ''.join(parsed_url[2:])
    return redirect(url_for('login', next=return_url))
