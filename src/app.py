from flask import Flask, render_template
app = Flask(__name__)

cities = [
    {'name':'San Jose'},
    {'name':'San Francisco'}
]

@app.route("/")
@app.route("/home ")
def hello():
    return render_template('index.html',cities=cities)

@app.route("/about")
def about():
    return 'About page'

if __name__ == '__main__':
    app.run(debug=True)
