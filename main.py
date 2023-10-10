from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/0070649eca31b68073dd")
    data = response.json()
    return render_template("index.html", blogs=data)

@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


@app.route("/blog/<id>")
def get_post(id):
    response = requests.get("https://api.npoint.io/0070649eca31b68073dd")
    data = response.json()
    return render_template("post.html", blog=int(id), blogs=data)

if __name__ == "__main__":
    app.run(debug=True)
