from flask import Flask, render_template as ender_dragon
moon = Flask(__name__)

@moon.route("/")
def home():
    return ender_dragon("index.html")

@moon.route("/about")
def about():
    return ender_dragon("about.html")

@moon.route("/why")
def why():
    return "<h1>Just...why?</h1><p>dang just why?</p>"

@moon.route("/about/contact")
def contact():
    return "<h1>My Contact</h1><p>Hah....you're not getting my number.</p>"

if __name__ == "__main__":
    moon.run(debug=True)

# I just learned that I can change some of the things name here like render_dragon as ender_dragon.