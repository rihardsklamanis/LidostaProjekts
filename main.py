from flask import Flask, render_template, url_for, request, redirect, Response, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lidosta.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Rezervacija(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vards = db.Column(db.String(300), nullable=False)
    uzvards = db.Column(db.String(300), nullable=False)
    epasts = db.Column(db.String(300), nullable=False)
    telefonaNumurs = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Rezervacija %r>" % self.id


class Lidojumi(db.Model):
    fid = db.Column(db.Integer, primary_key=True)
    lidojumaDatums = db.Column(db.String(300), nullable=False)
    no = db.Column(db.String(300), nullable=False)
    uz = db.Column(db.String(300), nullable=False)
    lidosta = db.Column(db.String(300), nullable=False)
    cena = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<Lidojumi %r>" % self.fid


class airportData(db.Model):
    aid = db.Column(db.Integer, primary_key=True)
    airportName = db.Column(db.String(300), nullable=False)
    shortAirportName = db.Column(db.String(300), nullable=False)
    airportAddress = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return "<airportData %r>" % self.aid


class planesData(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    planeName = db.Column(db.String(300), nullable=False)
    planePlaces = db.Column(db.Integer, nullable=False)
    planeReleaseDate = db.Column(db.String(300), nullable=False)
    planeAirport = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return "<planesData %r>" % self.pid


@app.route("/")
def index():
    return render_template("html.html")


@app.route("/rezervacija", methods=['POST', 'GET'])
def rezervacija():
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
            return redirect(url_for('reservationfinished', id=rezervacija.id))
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
    lidojumi = Lidojumi.query.order_by(Lidojumi.lidojumaDatums).all()
    return render_template("flights.html", lidojumi=lidojumi)
  

@app.route("/lidmasinas")
def planes():
    planesdata = planesData.query.order_by(planesData.pid).all()
    return render_template("planes.html", planesdata=planesdata)


@app.route("/lidostas")
def airports():
    airportdata = airportData.query.order_by(airportData.aid).all()
    return render_template("airport.html", airportdata=airportdata)

@app.route("/pievienotLidojumu", methods=['POST', 'GET'])
def pievienotLidojumu():
    if request.method == "POST":
        lidojumaDatums = datetime.strptime(request.form['lidojumaDatums'],'%Y-%m-%d')
        fid = request.form("fid")
        no = request.form["no"]
        uz = request.form["uz"]
        lidosta = request.form["lidosta"]
        cena = request.form["cena"]

        lidojumi = Lidojumi(lidojumaDatums=lidojumaDatums,fid=fid, no=no, uz=uz, lidosta=lidosta, cena=cena)

        try:
            db.session.add(lidojumi)
            db.session.commit()
            return redirect("/saraksts")
        except:
            pass
    else:    
        return render_template("addFlight.html")


@app.route("/addPlane", methods=['POST', 'GET'])
def addPlane():
    if request.method == "POST":
        planeName = request.form["planeName"]
        planePlaces = request.form["planePlaces"]
        planeReleaseDate = datetime.strptime(request.form['planeReleaseDate'],'%Y-%m-%d')
        planeAirport = request.form["planeAirport"]

        planesdata = planesData(planeName=planeName, planePlaces=planePlaces, planeReleaseDate=planeReleaseDate, planeAirport=planeAirport)

        try:
            db.session.add(planesdata)
            db.session.commit()
            return redirect("/")
        except:
            pass
    else:    
        return render_template("addPlane.html")


@app.route("/addAirport", methods=['POST', 'GET'])
def addAirport():
    if request.method == "POST":
        airportName = request.form["airportName"]
        shortAirportName = request.form["shortAirportName"]
        airportAddress = request.form["airportAddress"]

        airportdata = airportData(airportName=airportName, shortAirportName=shortAirportName, airportAddress=airportAddress)

        try:
            db.session.add(airportdata)
            db.session.commit()
            return redirect("/")
        except:
            pass
    else:    
        return render_template("addAirport.html") 


@app.route("/reservationfinished/<int:id>")
def reservationfinished(id):
    rezervacija = Rezervacija.query.get(id)
    return render_template("reservationFinished.html", rezervacija=rezervacija)

if __name__ == "__main__":
    app.run(debug=True)
