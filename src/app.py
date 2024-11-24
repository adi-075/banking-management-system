from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss
from datetime import datetime

app = Flask(__name__)
# Scss(app)

#SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
# db = SQLAlchemy(app)
@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/accounts')
def accounts():  # put application's code here
    return render_template("accounts.html")

if __name__ == '__main__':
    with app.app_context():
        pass

    app.run(debug=True)

