from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "super secret key"
app.debug = True

@app.route('/hello')
def index():
	flash("What's your name?")
	return render_template('index.html')

@app.route("/greet", methods=["POST", "GET"])
def greets():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	request.form['name_input']
	return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()