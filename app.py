# Import Dependencies
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Connect to PostgreSQL
#################################################
engine = create_engine(f'postgresql://postgres:postgres@localhost:5432/pharma_db')
# Base = automap_base()
# Base.prepare(engine, reflect=True)

# # Save reference to the table
# population = Base.classes.population
# pharma_spending = Base.classes.pharma_spending

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    return (
        f"hi"
    )


@app.route("/population")
def data():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a population table"""
    # Query population
    results = pd.read_sql_query('select country from population', con=engine).head()

    session.close()

    print(results, flush = True)
    return (results)

if __name__ == '__main__':
    app.run(debug=True)


