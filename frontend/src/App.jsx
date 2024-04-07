import React, { useState } from 'react';
import Map from './components/map/Map'
import Header from './components/header/Header'
import FilterBar from './components/filter-bar/FilterBar'
import './App.css'

function App() {
  const [address, setAddress] = useState('');
  const [submitTrigger, setSubmitTrigger] = useState(false); 

  const handleAddressSubmit = (newAddress) => {
    setAddress(newAddress);
    setSubmitTrigger(!submitTrigger);
  };

  return (
    <div className="App">
      <div className= "header-area">
        <Header />
      </div>
      <div className="content-area">
        <div className="map-area">
          <Map address={address} submitTrigger={submitTrigger}/>
        </div>
        <div className="filter-area">
          <FilterBar onAddressSubmit={handleAddressSubmit} />
        </div>
      </div>
    </div>
  )
}

export default App
