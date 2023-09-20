from datetime import datetime

from flask import Flask, redirect, render_template, session, url_for, flash, logging
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, SubmitField
from wtforms.validators import DataRequired, Email
app = Flask(__name__)
logger = logging.create_logger(app)
app.config["SECRET_KEY"] = "shhhh ... "
bootstrap = Bootstrap(app)
moment = Moment(app)

class Form(FlaskForm):
    name = StringField('What is your name?',validators=[DataRequired()])
    email = EmailField('What is your UofT email address?',validators=[DataRequired(),Email()])
    submit = SubmitField('Submit')

@app.route("/",methods=['GET','POST'])
def index():
    form = Form()
    if form.validate_on_submit():
        session['valid_email'] = False
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        session['email'] = form.email.data
        if 'utoronto' in form.email.data.split("@")[1]:
            # logger.log(form.email.data.split("@"))
            session['valid_email'] = True
        return redirect(url_for('index'))
    
    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'), valid_email=session.get('valid_email'))


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


# if __name__ == '__main__':
#     app.run()
