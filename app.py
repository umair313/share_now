from flask import Flask, render_template, url_for, request, redirect, session
from datetime import timedelta

app = Flask(__name__) 
app.secret_key = "sharenow"
app.permanent_session_lifetime = timedelta(minutes=15)
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == "POST":
		# this makes session permanent
		session.permanent = True
		# getting data from form
		userEmail = request.form["userEmail"]
		# adding data to session
		session["userEmail"] = userEmail
		return redirect(url_for("dashboard"))
	else:
		# if user is already logged in
		if "userEmail" in session:
			return redirect(url_for("dashboard"))
		else:
			pass
		return render_template("login.html")

@app.route('/logout')
def logout():
	# removing session data
	# .pop function removes a key
	session.pop("userEmail", None)
	# after removing session redirect to
	return redirect(url_for("login"))

@app.route('/dashboard')
def dashboard():
	if "userEmail" in session:
		userEmail = session["userEmail"]
		return render_template("dashboard.html", usr=userEmail)
	else:
		return redirect(url_for("login"))
if __name__ == '__main__': 
	app.run(debug=True) 
