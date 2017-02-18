from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/production.db'
Bootstrap(app)
db = SQLAlchemy(app)

class Tempreading(db.Model):
    __tablename__ = 'tempreadings'
    id = db.Column(db.Integer, primary_key = True)
    temperature = db.Column('Temperature', db.Float)

    def __init__(self, temperature):
        self.temperature = temperature

class Location(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    place = db.Column(db.String(80))

    def __init__(self, place):
        self.place = place

    def __repr__(self):
        return '[location %r]' %self.place

#db.create_all()
#test1 = Location('Seattle')
#test2 = Location('Shit')
#db.session.add(test1)
#db.session.add(test2)
#db.session.commit()


@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/search/<searchterm>")
def search(searchterm):
    print(request.args.get('test', ''))
    return render_template('search.html', searchvar=searchterm)

@app.route("/welcome")
def welcome():
    locations = db.session.query(Location).order_by(Location.place.desc()).all()
    for location in locations:
        print(location.place)
    return render_template('welcome.html', locations = locations)

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    return render_template('signin.html', name=request.form['name'])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
