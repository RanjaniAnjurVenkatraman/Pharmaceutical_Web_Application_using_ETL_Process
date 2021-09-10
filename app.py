import numpy as np
import pandas as pd 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask import render_template, request, redirect, url_for, flash

#################################################
# Database Setup
#################################################
connection_string = "postgres:postgres@localhost:5432/pharma_db"
engine = create_engine(f'postgresql://{connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Population= Base.classes.population
Pharma_spending = Base.classes.pharma_spending

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return render_template('index.html')


@app.route("/api/v1.0/population")
def population():
    # Create our session (link) from Python to the DB
    session = Session(engine)

   
    # Query all passengers
    results = session.query(Population.country_code, Population.country, Population.population).all()

    session.close()
    return render_template('index1.html', population=results  )


@app.route("/api/v1.0/pharma_spending")
def pharma():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all passengers
    results = session.query(Pharma_spending.country_code, Pharma_spending.percent_pharmaceutical_spending).all()

    session.close()
    return render_template('index2.html', pharma=results)

@app.route("/api/v1.0/population_pharma_spending")
def pop_pharma():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # """Joining"""
   
    p = [Population.country_code, Population.country, Population.population,Pharma_spending.percent_pharmaceutical_spending]	
    results = session.query(*p).filter(Population.country_code == Pharma_spending.country_code).all()

    session.close()
    return render_template('index3.html', population_pharma=results)



if __name__ == '__main__':
    app.run(debug=True)
