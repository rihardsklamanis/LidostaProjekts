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
    lidojumaLaiks = db.Column(db.String(300), nullable=False)
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


@app.route("/saraksts/<int:fid>/del")
def delete(fid):
    lidojumi_delete = Lidojumi.query.get_or_404(fid)
    try:
        db.session.delete(lidojumi_delete)
        db.session.commit()

        lidojumi = Lidojumi.query.order_by(Lidojumi.lidojumaDatums).all()
        return render_template("flights.html", lidojumi=lidojumi) 
    except:
        return "Error"   
  

@app.route("/lidmasinas")
def planes():
    planesdata = planesData.query.order_by(planesData.pid).all()
    return render_template("planes.html", planesdata=planesdata)


@app.route("/lidmasinas/<int:pid>/del")
def delete_plane(pid):
    planesdata_Delete = planesData.query.get_or_404(pid)

    try:
        db.session.delete(planesdata_Delete)
        db.session.commit()
        planesdata = planesData.query.order_by(planesData.pid).all()
        return render_template("planes.html", planesdata=planesdata)
    except:
        return "Error"   


@app.route("/lidostas")
def airports():
    airportdata = airportData.query.order_by(airportData.aid).all()
    return render_template("airport.html", airportdata=airportdata)

@app.route("/lidostas/<int:aid>/del")
def delete_airport(aid):
    airportdata_Delete = airportData.query.get_or_404(aid)

    try:
        db.session.delete(airportdata_Delete)
        db.session.commit()
        airportdata = airportData.query.order_by(airportData.aid).all()
        return render_template("airport.html", airportdata=airportdata)
    except:
        return "Error"    

         
@app.route("/pievienotLidojumu", methods=['POST', 'GET'])
def pievienotLidojumu():
    if request.method == "POST":
        lidojumaDatums = request.form["lidojumaDatums"]
        lidojumaLaiks = request.form["lidojumaLaiks"]
        no = request.form["no"]
        uz = request.form["uz"]
        lidosta = request.form["lidosta"]
        cena = request.form["cena"]

        lidojumi = Lidojumi(lidojumaDatums=lidojumaDatums, lidojumaLaiks=lidojumaLaiks, no=no, uz=uz, lidosta=lidosta, cena=cena)

        try:
            db.session.add(lidojumi)
            db.session.commit()
            return redirect("/saraksts")
        except:
            pass
    else:    
        return render_template("addFlight.html")


@app.route("/saraksts/<int:fid>/update", methods=['POST', 'GET'])
def updateFlight(fid):
    lidojumi = Lidojumi.query.get(fid) 
    if request.method == "POST":
        lidojumi.lidojumaDatums = request.form["lidojumaDatums"]
        lidojumi.lidojumaLaiks = request.form["lidojumaLaiks"]
        lidojumi.no = request.form["no"]
        lidojumi.uz = request.form["uz"]
        lidojumi.lidosta = request.form["lidosta"]
        lidojumi.cena = request.form["cena"]

        try:
            db.session.commit()
            return redirect("/saraksts")
        except:
            return "Error"
    else:   
        return render_template("updateFlight.html", lidojumi=lidojumi)        


@app.route("/addPlane", methods=['POST', 'GET'])
def addPlane():
    if request.method == "POST":
        planeName = request.form["planeName"]
        planePlaces = request.form["planePlaces"]
        planeReleaseDate = request.form["planeReleaseDate"]
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


@app.route("/lidmasinas/<int:pid>/update", methods=['POST', 'GET'])
def updatePlanes(pid):
    planesdata = planesData.query.get(pid) 
    if request.method == "POST":
        planesdata.planeName = request.form["planeName"]
        planesdata.planePlaces = request.form["planePlaces"]
        planesdata.planeReleaseDate = request.form["planeReleaseDate"]
        planesdata.planeAirport = request.form["planeAirport"]

        try:
            db.session.commit()
            return redirect("/lidmasinas")
        except:
            return "Error"
    else:   
        return render_template("updatePlane.html", planesdata=planesdata) 


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


@app.route("/lidostas/<int:aid>/update", methods=['POST', 'GET'])
def updateAirport(aid):
    airportdata = airportData.query.get(aid) 
    if request.method == "POST":
        airportdata.airportName = request.form["airportName"]
        airportdata.shortAirportName = request.form["shortAirportName"]
        airportdata.airportAddress = request.form["airportAddress"]

        try:
            db.session.commit()
            return redirect("/lidostas")
        except:
            return "Error"
    else:   
        return render_template("updateAirport.html", airportdata=airportdata) 


@app.route("/reservationfinished/<int:id>")
def reservationfinished(id):
    rezervacija = Rezervacija.query.get(id)
    return render_template("reservationFinished.html", rezervacija=rezervacija)

if __name__ == "__main__":
    app.run(debug=True)
