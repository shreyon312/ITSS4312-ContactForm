# from flask import Flask, render_template
# from ContactForm import ContactForm

# app = Flask(__name__)
# app.config["SECRET_KEY"] = "qwerTY"

# @app.route("/")
# def home():
#     form = ContactForm()
#     return render_template("index.html", form=form)

# if __name__ == "__main__":
#     app.run(debug=True)

import csv
from flask import Flask, render_template, redirect, request,url_for
from ContactForm import ContactForm
from SignUpForm import RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "qwerTY"

@app.route("/", methods = ["GET", "POST"])
def home():
    form = ContactForm()
    if form.is_submitted():
        with open("data.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([form.data["email"], form.data["rating"], form.data["message"]])
        return redirect(url_for("home"))
    return render_template("index.html", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        if form.is_submitted():
            return redirect(url_for("success"))
    return render_template('register.html', form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    form = {"name":"Jamie Bray", "email":"abd123@gmail.com"}
    #if request.method=="POST":
        # print("Candidate Name:",form.name.data)
        # print("Address:",form.Address.data)
        # print("Email:",form.email.data)
        # print("Skills:",form.skill.data)
    return render_template("profile.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)