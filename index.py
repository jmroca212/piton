from flask import Flask, render_template

app = Flask(__name__)



# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

@app.route('/nada', strict_slashes=False)
def nada():
    return render_template("nada.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
