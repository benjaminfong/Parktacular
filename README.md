# PARKTACULAR

Our team built a web app to improve upon SMFTA's parking interface by providing various filters based on 
price, location, opening time, distance, and in the future, previous crime history.

## How we built it
We used React Vite for the front end and Django for the back end and server. 
We used a Jupyter notebook to perform the machine leaning model training. 

## Backend
-- backend content --

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
