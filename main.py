from flask import Flask, render_template, url_for, request, redirect, Response, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lidosta.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Rezervacija(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vards = db.Column(db.String(300), nullable=False)
    uzvards = db.Column(db.String(300), nullable=False)
    epasts = db.Column(db.String(300), nullable=False)
    telefonaNumurs = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return "<Article %r>" % self.id


@app.route("/")
def index():
    return render_template("html.html")


@app.route("/rezervacija", methods=['POST', 'GET'])
def rezevacija():
    if request.method == 'POST':
        vards = request.form["vards"]
        uzvards = request.form["uzvards"]
        epasts = request.form["epasts"]
        telefonaNumurs = request.form["telefonaNumurs"]

        rezervacija = Rezervacija(
            vards=vards, uzvards=uzvards, epasts=epasts, telefonaNumurs=telefonaNumurs)

        try:
            db.session.add(rezervacija)
            db.session.commit()
            return redirect('/')
        except:
            pass
    else:
        return render_template("reservations.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/saraksts")
def nauraVienigaLapa():
    return render_template("flights.html")

@app.route("/sarakstsadmin")
def flightsAdmin():
    return render_template("flightsAdmin.html")    


@app.route("/lidmasinas")
def planes():
    return render_template("planes.html")

@app.route("/lidmasinasadmin")
def planesAdmin():
    return render_template("planesAdmin.html")    


@app.route("/lidostas")
def airports():
    return render_template("airport.html")

@app.route("/lidostasadmin")
def airportsAdmin():
    return render_template("airportAdmin.html")    


if __name__ == "__main__":
    app.run(debug=True)
