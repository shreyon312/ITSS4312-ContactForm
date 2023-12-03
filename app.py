from flask import Flask, render_template
from ContactForm import ContactForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwerTY"

@app.route("/")
def home():
    form = ContactForm()
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)