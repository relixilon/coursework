from flask import Flask, render_template, flash, url_for , redirect
from forms import RegistrationForm, LoginForm
from flaskext.mysql import MySQL
app = Flask(__name__)

app.config['SECRET_KEY'] = 'penis'

mysql = MySQL()
mysql.init_app(app)

cursor = mysql.get_db().cursor()


@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html', title='Home')

@app.route('/login')
def login():
   form = LoginForm()
   return render_template('login.html', title='login',  form=form)

@app.route('/register', methods=['Get', 'POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
      flash(f'Account created for{form.username.data}!','success')
      return redirect(url_for('home'))
   return render_template('register.html', title='Register', form=form)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
