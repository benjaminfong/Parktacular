# PARKTACULAR

Our team built a Web App to improve upon SMFTA's parking map by providing various filters based on 
price, location, opening time, distance, and probability predictions of different types of crime arount the parking facilities using ML.

## How we built it
We used React Vite for the front end and Django for the back end and server. <br>
We used Azure SQL Database for parking lots data storage and retrieval. <br>
We used a Jupyter notebook to perform the machine leaning model training. 

## Backend
Please go to the backend subdirectory: <br><code>[path/to/]/Parktacular/cd backend</code><br>

Create and activate a virtual environment:<br>
<code>[path/to/]/Parktacular/python3 -m venv env</code><br>
<code>[path/to/]/Parktacular/source env/bin/activate</code><br><br>
It’s better to install an isolated python package in venv. To get all the packages you need to run the server:<br>
<code>(env) [path/to/]/Parktacular/backend/pip install -r requirements.txt</code><br>
<br>Make sure you have ODBC Driver 18 for SQL Server installed in your local environment.<br>
If you don’t have, follow this reference: [Download ODBC driver for SQL server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16)<br>
<br>In the root of backend folder, run this command to start the server: <br>
<code>(env) [path/to/]/Parktacular/backend/python manage.py runserver </code><br><br>
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
We used XGBoost ML model to determine the likelihood of a particular type of crime occuring within the a location. 
In the future, we hope to integrate this information on our page.<br>
Please refer here: [XGBoost for crime prediction](https://github.com/AnanyaAgarwal1997/hackathon.git)
