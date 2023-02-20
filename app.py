from flask import Flask, render_template

from controllers.countries_controller import countries_blueprint


app = Flask(__name__)

app.register_blueprint(countries_blueprint)



# This route displays the homepage html file

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)