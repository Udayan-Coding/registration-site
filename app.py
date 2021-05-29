import os

from dotenv import load_dotenv
from flask import Flask
from flask import render_template
from werkzeug.utils import redirect

from registration_form import RegistrationForm
from repository import get_sheet

load_dotenv()

app = Flask(__name__)
app.config.update(SECRET_KEY=os.getenv("SECRET_KEY"))


@app.route('/', methods=('GET', 'POST'))
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        gsheet = get_sheet(form.chapter.data)
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
        gsheet.insert_row(row, 2)
        return redirect('/')
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
