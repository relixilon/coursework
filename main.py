from flask import Flask, render_template, flash, url_for , redirect
import mysql.connector, datetime, dbfunc, functions
from forms import RegistrationForm, LoginForm
from database import Database

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'penis'

DB_NAME = 'travel'

logedIn = False

session = ''

@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html', title='Home', login=logedIn , user=session)

@app.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm()

   users = ''

   if form.validate_on_submit():
      conn = dbfunc.getConnection()
      cursor = conn.cursor()
      cursor.execute('USE {}'.format(DB_NAME))

      sql = "SELECT email, password  FROM users"
      cursor.execute(sql)
      users = cursor.fetchall()
      cursor.close()
      conn.close()
   
      if functions.checkLogin(users,(form.email.data,form.password.data)):
         session = (form.data)
         print(f'logging in as {form.email.data}')
         flash('Log In succesfull')
         logedIn = True
         return redirect(url_for('home'))
      else:
         flash('Log in unsuccessfull')
   
   return render_template('login.html', title='login',  form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
   form = RegistrationForm()

   if form.validate_on_submit():
      conn = dbfunc.getConnection()
      cursor = conn.cursor()
      cursor.execute('USE {}'.format(DB_NAME))

      sql = "INSERT INTO users (username, password, email, dateCreated) VALUES (%s, %s, %s, %s)"
      val = (form.username.data, form.password.data, form.email.data, datetime.datetime.now())
      cursor.execute(sql,val)
      
      conn.commit()
      conn.cursor.close()
      conn.close()
      
      flash(f'Account created for {form.username.data}!','success')
      
      return redirect(url_for('home'))

   return render_template('register.html', title='Register', form=form)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
