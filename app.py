from flask import Flask, render_template, url_for, request, redirect, session

app = Flask(__name__) 
app.secret_key = "sharenow"
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == "POST":
		# getting data from form
		userEmail = request.form["userEmail"]
		# adding data to session
		session["userEmail"] = userEmail
		return redirect(url_for("dashboard"))
	else:
		return render_template("login.html")

@app.route('/dashboard')
def dashboard():
	if "userEmail" in session:
		userEmail = session["userEmail"]
		return render_template("dashboard.html", usr=userEmail)
	else:
		return redirect(url_for("login"))
if __name__ == '__main__': 
	app.run(debug=True) 
