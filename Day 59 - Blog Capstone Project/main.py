from flask import Flask, render_template
import requests

API_ENDPOINT = "https://api.npoint.io/674f5423f73deab1e9a7"

app = Flask(__name__)

all_posts = requests.get(url=API_ENDPOINT).json()
for post in all_posts:
    print(post)
@app.route("/")
def index():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about():
    return render_template("about.html", posts=all_posts)


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    selected_post = None
    for post in all_posts:
        if post.get('id') == index:
            selected_post = post
    return render_template('post.html', post=selected_post)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)