from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    """Show all planets."""
    return render_template("index.html")

@app.route("/planets")
def planets_index():
    """Show all planets."""
    return render_template("planets_index.html")

@app.route("/planets/<name>")
def planet_show(name):
    comments = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    return render_template('planets_show.html', name=name, comments=comments)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
