# PARKTACULAR

Our team built a web app to improve upon SMFTA's parking interface by providing various filters based on 
price, location, opening time, distance, and in the future, previous crime history.

## How we built it
We used React Vite for the front end and Django for the back end and server. 
We used Azure SQL Database for parking lots data storage and retrieval. 
We used a Jupyter notebook to perform the machine leaning model training. 

## Backend
Django server: <code>[path/to/]/Parktacular/cd backend</code><br>

Create and activate a virtual environment:
<code>[path/to/]/Parktacular/python3 -m venv env[path/to/]/Parktacular/source env/bin/activate
</code><br>

It’s better to install an isolated python package in venv. To get all the packages you need to run the server:<br>
<code>(env) [path/to/]/Parktacular/backend %pip install -r requirements.txt</code><br>
Make sure you have ODBC Driver 18 for SQL Server installed in your local environment. If you don’t have, follow this reference: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16<br>
In the root of backend folder, run this command to start the server: <br>
<code>(env) [path/to/]/Parktacular/python manage.py runserver </code>
If you see “Starting development server at http://127.0.0.1:8000/“ on the terminal, the server is started successfully! You can quit the server with CONTROL-C. 

## Frontend
The frontend uses google maps api to display the map component. We also uses axios to make a call to the backend. 
When the page is first loaded, we get all the parking lots data from the backend. 
Also, everytime the user submits a new filter another call is made to display the available parking area that satisfy the condition. 
We also use google geocode to enable the filter by distance.

Finally, to enable the frontend. 
Please go to the frontend subdirectory, then run the following:<br> 
<code>npm install</code> -- install dependencies<br>
<code>npm run dev</code> -- start a local server

## What's next for Parktacular
We hope to display the price and hours of operation in the UI as well as integrate the machine learning crime safety prediction in our website.
