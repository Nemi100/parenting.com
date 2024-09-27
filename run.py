import os
from flask import Flask, render_template,request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",page_title="")
    

@app.route("/contact",methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form.get("name"))
    return render_template("contact.html",page_title="Contact us")

@app.route("/about")
def about():
    return render_template("about.html",page_title="About Us")

@app.route("/careers")
def careers():
    return render_template("careers.html",page_title="Careers")

@app.route("/signup")
def signup():
    return render_template("signup.html",page_title="Sign Up")


@app.route("/admin")
def admin():
    return render_template("admin.html",page_title="Sign in")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug=True
    )


