import csv
from flask import Flask, render_template, redirect,url_for
from ContactForm import ContactForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwerTY"

@app.route("/", methods = ["GET", "Post"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([form.data["name"], form.data["email"], form.data["message"]])
            print([form.data["name"], form.data["email"], form.data["message"]])
        return redirect(url_for("home"))
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)