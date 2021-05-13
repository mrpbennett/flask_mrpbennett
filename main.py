from os import environ, path

import contentful
from dotenv import load_dotenv
from flask import Flask, render_template
from flaskext.markdown import Markdown

app = Flask(__name__)

Markdown(app, extensions=["fenced_code"], output_format="html5")

app.config.from_object("config.ProdConfig")

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

client = contentful.Client(
    environ.get("CONTENTFUL_SPACE_ID"),
    environ.get("CONTENTFUL_ACCESS_TOKEN"),
    environment="master",
)

entries = client.entries()


def format_datetime(value):
    """Format date time object using jinja filters"""
    return value.strftime("%B %-d, %Y")


app.jinja_env.filters["datetime"] = format_datetime

social = [
    {"name": "Github", "url": "http://github.com/mrpbennett"},
    {"name": "Linkedin", "url": "http://linked.com"},
    {"name": "Strava", "url": "https://www.strava.com/athletes/866413"},
]

tech_i_use = [
    "Python",
    "Docker",
    "Git/Github",
    "HTML/CSS/SASS",
    "JavaScript (we have a love/hate relationship)",
]


@app.route("/")
@app.route("/home/")
def index():
    return render_template("home.html", social=social)


@app.route("/about/")
def about():
    return render_template("about.html", title="About Me", tech_i_use=tech_i_use)


@app.route("/blog/")
def blog():

    posts = client.entries({"content_type": "posts"})

    return render_template("blog.html", title="Blog", posts=posts)


@app.route("/blog/<string:slug>/")
def post(slug):
    post = client.entries({"content_type": "posts", "fields.slug": slug})
    post = post[0]

    return render_template("post.html", post=post)


# HTTP Error handlers ---
@app.errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
