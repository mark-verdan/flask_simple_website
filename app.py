from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to my Windows website!</h1>"

@app.route("/about")
def about():
    return "<h1>About me</h1><p>I'm a Python Beginner</p>"

@app.route("/why")
def why():
    return "<h1>Just...why?</h1><p>dang just why?</p>"

@app.route("/about/contact")
def contact():
    return "<h1>My Contact</h1><p>Hah....you're not getting my number.</p>"

if __name__ == "__main__":
    app.run(debug=True)