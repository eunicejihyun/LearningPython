from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, InputRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

options = ['!', '!!', '!!!', '!!!!', '!!!!!', 'X']


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField(label='Location URL', validators=[DataRequired(), URL()])
    open = StringField(label='Open Time', validators=[DataRequired()])
    close = StringField(label='Close Time', validators=[DataRequired()])
    coffee = SelectField(label='Coffee Rating', choices=options, validators=[InputRequired()])
    wifi = SelectField(label='Wifi Rating', choices=options, validators=[InputRequired()])
    power = SelectField(label='Outlet Rating', choices=options, validators=[InputRequired()])
    submit = SubmitField('Submit')




# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print(str(form.data))
        new_data = f"\n{form.cafe.data}, {form.location.data}, {form.open.data}, {form.close.data}, {form.coffee.data}, {form.wifi.data}, {form.power.data}"
        with open('cafe-data.csv', 'a', newline='') as file:
            file.write(new_data)
        return cafes()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
