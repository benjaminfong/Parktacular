import React, { useState, useEffect } from "react";
import Map from './components/map/Map'
import Header from './components/header/Header'
import FilterBar from './components/filter-bar/FilterBar'
import './App.css'

import axios from 'axios';

import {getLatLong} from './components/map/Map.jsx'

function App() {
  const [address, setAddress] = useState('');
  const [submitTrigger, setSubmitTrigger] = useState(false); 

  const handleAddressSubmit = (newAddress) => {
    setAddress(newAddress);
    setSubmitTrigger(!submitTrigger);
  };

 

  // State to manage API calls
  const [priceMin, setPriceMin] = useState();
  const [priceMax, setPriceMax] = useState();
  const [time, setTime] = useState();
  const [distance, setDistance] = useState();

  // data object fetched from db
  const [places, setPlaces] = useState([]);

  const handlePriceFilter = (value) => {
    if (value === "0-20") {
      setPriceMin(0);
      setPriceMax(20);
    } 
    else if (value === "20-40") {
      setPriceMin(20);
      setPriceMax(40);
    }
    else if (value === "40") {
      setPriceMin(40);
      setPriceMax(100);
    }
    console.log(priceMin)
  };

  const handleTimeFilter = (value) => {
    if (value !== undefined && value >= 0 && value <= 23) {
      setTime(value);
    }
  }

  const handleAddressFilter = (value) => {
    // console.log("Hello2 " + value)
    if (value != undefined && value != "") {
      console.log("Hello3 " + value)
      setAddress(value);
    }
  }

  const handleDistanceFilter = (value) => {
    if (value != undefined && value != "") {
      setDistance(value);
    }
  }

  const handleFilterSubmit = async () => {
    try {
      const params = { };
      // set price into params
      if (priceMax != undefined && priceMin != undefined) {
        params.price_min = priceMin;
        params.price_max = priceMax;
      }
      // set time into params
      if (time != undefined && time != "") {
        params.time = time + ':00';
      }

      // handleAddressSubmit(address); // set address data

      const { lat, lng } = await getLatLong(address);
  
      if (lat != undefined && lng != undefined) {
        params.long = lng;
        params.lat = lat;
      }

      // set distance to params
      if (distance != undefined && distance != "") {
        params.distance = distance;
      }

      // Construct the URL with parameters
      const queryString = new URLSearchParams(params).toString();
      const response = await axios.get(`http://localhost:8000/parking/api?${queryString}`);
      setPlaces(response.data);

      // Do something with the response data
      // console.log(data);
    } catch (error) {
      console.error('Error fetching parking data:', error);
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/parking/api');
        // console.log(response.data);
        setPlaces(response.data);
      } catch (error) {
        console.error('Error fetching parking data:', error);
      }
    };

    fetchData();
  }, []); // Run only once when the component mounts

    


  return (
    <div className="App">
      <div className= "header-area">
        <Header />
      </div>
      <div className="content-area">
        <div className="map-area">
          <Map places={places} address={address} submitTrigger={submitTrigger}/>
        </div>
        <div className="filter-area">
          <FilterBar onPriceChange={handlePriceFilter} 
                    onTimeChange={handleTimeFilter}
                    onAddressChange={handleAddressFilter}
                    onDistanceChange={handleDistanceFilter}
                    onFilterSubmit={handleFilterSubmit}
                    onAddressSubmit={handleAddressSubmit} />
        </div>
      </div>
    </div>
  )
}

export default App
