from flask import Flask, render_template, request
import pickle

app = Flask('/')

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():

	# When method is POST take input and output it
	if request.method == 'POST':
		# Getting textual data from the input field
		news = request.form['news_input']
		res = news

		# Rendering the output to the output box
		return render_template('index.html', classified=res)

	if request.method == 'GET':
		return render_template('index.html')

# For HotReload/Live Reload
if __name__ == '__main__':
	app.run(port='5050', debug=True)