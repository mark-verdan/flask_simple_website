from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/why")
def why():
    return "<h1>Just...why?</h1><p>dang just why?</p>"

@app.route("/about/contact")
def contact():
    return "<h1>My Contact</h1><p>Hah....you're not getting my number.</p>"

if __name__ == "__main__":
    app.run(debug=True)