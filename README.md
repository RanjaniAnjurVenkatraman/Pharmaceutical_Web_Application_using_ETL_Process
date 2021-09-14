![image](https://i.pinimg.com/originals/cc/b4/e0/ccb4e025060e377a55f04f3cdd19743f.jpg)

## Table of Contents
   =================

  1. [About This Project](#about-this-project) <br>
	 - [Technologies](#technologies)
	 - [Architectural Diagram](#architectural-diagram)
  	 - [ETL Process](#etl-process)
  4. [Flask App](#flask-app)
  5. [Visualizations](#visualizations)
  6. [Contributors](#contributors)

## About This Project 	
Our team was interested in exploring healthcare data. We extracted pharmaceutical spending data across the globe to determine how much each country is spending on off the shelf pharmaceutical medicines. Data was extracted from CSV and JSON sources, transformed using Python, Pandas and SQL. Data was then loaded into PostgreSQL. SQLAlchemy was used with Flask to deploy results to a pharmaceutical web application. 

This web application can be used by pharmaceutical companies to promote products globally.

## Technologies :hammer:	
![image](https://img.shields.io/badge/technologies-Python-green)
![image](https://img.shields.io/badge/technologies-Pandas-green)
![image](https://img.shields.io/badge/technologies-SQL-green)
![image](https://img.shields.io/badge/technologies-PostgreSQL-green)
![image](https://img.shields.io/badge/technologies-SQLAlchemy-green)
![image](https://img.shields.io/badge/technologies-Flask-green)
![image](https://img.shields.io/badge/technologies-HTML-green)
![image](https://img.shields.io/badge/technologies-Bootstrap-green)

## Architectural Diagram 	
<img src="https://i.pinimg.com/originals/f9/bd/b2/f9bdb222137b9b1d00faf66420994299.jpg" width=800 align=center> <br>

## ETL Process 	

#### Extract 
Pharmaceutical and Population datasets were extracted from the following CSV and JSON sources. EDA was performed on the data.

- [Pharmaceutical_Spending](https://data.oecd.org/healthres/pharmaceutical-spending.htm#indicator-chart)
	- Format: CSV
	- Size: 240 KB
- [Population](https://datahub.io/core/population#pandas)
	- Format: JSON
	- Size: 1 MB

#### Transform 
Data was transformed and cleaned using Python, Pandas and SQL. 
Transformations include: 
- Filtering the population dataframe for year = 2018. The year 2018 was the latest data available.  
- Filtering based on ‘% of Pharmaceutical spending’ 
- Changing column datatypes
- Renaming columns
- Retrieving required columns and dropping unwanted columns to load into PostgreSQL		

#### Load
Due to the relational nature of the population and pharmaceutical spending data, we decided to use PostgreSQL. Pandas was used to load dataframes into the database. Tables were merged on ‘country code’ using SQL in PostgreSQL. SQLAlchemy was then used with Flask to deploy results to an HTML page. 
	
## Flask App 
A Flask application was created to display data for the following routes: 
<br>
- / <br>
<br>
<img src="https://i.pinimg.com/originals/f2/42/04/f24204c441e79cbec95ed179f0dace50.jpg" width=600 align=center> <br>

- /population <br>
<br>
<img src="https://i.pinimg.com/originals/a6/ef/26/a6ef264ad56d89f7743b2b701e287c6e.jpg" width=600 align=center> <br>

- /pharma_spending <br>
<br>
<img src="https://i.pinimg.com/originals/5e/54/5f/5e545fa765feac3390ae7ca823da5eb2.jpg" width=600 align=center> <br>

- /population_pharma_spending <br>
<br>
<img src="https://i.pinimg.com/originals/1a/bd/ae/1abdaed9716a68537ddff55324f0b825.jpg" width=600 align=center> <br>

#### How to Run The Application
1. Ensure Flask is installed in the virtual environment: 'python -m pip install flask'.
2. Clone this repository to run on your local machine.
3. In the virtual environment, navigate to the 'Pharmaceutical App' folder.
4. In the virtual environment, run the app by using the command'python app.py'
5. To open your default browser to the rendered page, Ctrl+click the http://127.0.0.1:5000/ URL in the terminal.
6. On the webpage, click 'Routes' to view and explore Population, Pharmaceutical and Pharmaceutical Spending data. 


## Visualizations 	
Countries with the highest pharmaceutical spend include: <br>
<img src="https://i.pinimg.com/originals/7c/f6/d6/7cf6d611cba4092b60c667b36667bc62.jpg" width=800 align=center> <br>

Countries with the lowest pharmaceutical spend include: <br>
<img src="https://i.pinimg.com/originals/4d/e0/7e/4de07e56d6136ef5aca09410167d736d.jpg" width=800 align=center> <br>

## Contributors

- [Ranjani Venkatraman](https://github.com/RanjaniAnjurVenkatraman)
- [Saiana Darizhapova](https://github.com/Saiana82)
- [Lauren To](https://github.com/laurenemilyto)