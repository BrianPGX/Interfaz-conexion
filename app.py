from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/signup.db'
db = SQLAlchemy(app)

class Signup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    pasw = db.Column(db.String(30))
    pas_repeat = db.Column(db.String(30))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-signup',methods=['POST'])
def create():
   signup = Signup(email=request.form['emails'],pasw=request.form['psw'],pas_repeat=request.form['psw-repeat'])
   db.session.add(signup)
   db.session.commit()
   return 'saved'

if __name__=='__main__':
    app.debug = True
    app.run()
