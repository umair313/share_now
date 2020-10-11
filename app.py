from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__) 

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == "POST":
		userEmail = request.form["userEmail"]
		return redirect(url_for("dashboard", usr=userEmail))
	else:
		return render_template("login.html")

@app.route('/dashboard/<usr>')
def dashboard(usr = "aun"):
	return render_template("dashboard.html", usr=usr)
if __name__ == '__main__': 
	app.run(debug=True) 
