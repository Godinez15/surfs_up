# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Importing SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Importing dependencies for Flask
from flask import Flask, jsonify

# Set up the database engine for the Flask application
engine=  create_engine("sqlite:///hawaii.sqlite")

# Reflects the database into our classes.
Base= automap_base()

# Reflects the code
Base.prepare(engine, reflect=True)

# Creating a variable for each of the classes to reference them later
measuremet= Base.classes.measurement
station= Base.classes.station

# Creates a session link from Python to our database
session= Session(engine)

# Defines our Flask app
app=Flask(__name__)

# Defines the welcome route 
@app.route("/")

# Next add the routing info. for each of the other routes
# Creating the welcome() function.
def welcome():
	return(
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end<br/>"
	)
# Creates a new route(Route 2)
@app.route("/api/v1.0/precipitation")

# Creates the precipitation() function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
return jsonify(precip)

# Creating route #3
@app.route("/api/v1.0/stations")

# Using the stations() function.
def stations():
# Creates a query that will allow us
# to get all of the stations in out
# database
    results= session.query(Station.station).all()
# Coverts the results into a list
    stations= list(np.ravel(results))
    return jsonify(stations)

# Route #4 returning the temperature 
# observations for the prev. year
@app.route("/api/v1.0/tobs")

# Creates a function called temp_monthly()
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).\
    filter(Measurement.station = 'USC00519281').\
    filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
return jsonify(temps)

# Creating route # 5 
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Creates a function called stats()
# Adds the start and end parameters
# For now they are both set to None
def stats(start=None, end=None):
# Create a query to select the min., 
#avg., max. temperatures from SQlite
    sel=[func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    if not end:
        results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
    return jsonify(temps)
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all().\
        temps = list(np.ravel(results)).\
        return jsonify(temps)