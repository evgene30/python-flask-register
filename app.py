from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY DATABASE_URI'] = "MySQL:///users.db"
db = SQLAlchemy(app)


class Userreg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    UserName = db.Column(db.String(20), nullable=False)
    LastName = db.Column(db.String(30), nullable=False)
    Date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<UserReg %r>' % self.id


@app.route('/')
@app.route('/home')
def index():
    q = request.args.get('q')
    if q:
        return render_template('search.html')

    else:
        return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search')
def search():
    return render_template('search.html')


if __name__ == "__main__":
    app.run(debug=True)
