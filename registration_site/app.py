from flask import Flask
from flask import render_template, redirect

from .registration_form import RegistrationForm
from .repository import get_sheet
from . import settings

app = Flask(__name__)
app.config.update(SECRET_KEY=settings.secret_key())


@app.route('/', methods=('GET', 'POST'))
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        sheet = get_sheet(form.chapter.data)
        row = [form.first_name.data,
               form.middle_name.data,
               form.last_name.data,
               form.gender.data,
               str(form.date_of_birth.data),
               form.contact_number.data,
               form.home_address.data,
               form.country.data,
               form.state.data,
               form.city.data,
               form.email.data,
               form.religion.data,
               form.caste.data]
        sheet.insert_row(row, 2)
        return redirect('/')
    return render_template('index.html', form=form)
