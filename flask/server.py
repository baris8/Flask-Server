from flask import Flask, render_template, url_for, flash, redirect
from forms import RegsitrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c0790e478f0eba7b451b4b0cec876a66'

posts= [
	{
		'author': 'Baris Üctas',
		'title': 'First Server', 
		'content': 'Das ist mein erster Server!',
		'date_posted': 'November 6, 2019'
	}
]	

#@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegsitrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.username.data == 'baris' and form.password.data == "123456":
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unseccessfull. Please Check Login-Data!', 'danger')
		
	return render_template('login.html', title = 'Login', form = form)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)
