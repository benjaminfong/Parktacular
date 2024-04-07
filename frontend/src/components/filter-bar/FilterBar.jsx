import React, { useState } from 'react';
import './filter-bar.css';

const FilterBar = ({ onPriceChange, onTimeChange, onAddressChange, onDistanceChange, onFilterSubmit, onAddressSubmit }) => {
  // State to manage form values
  const [filterOps, setFilterOps] = useState({
    price: '',
    openTime: '',
    distanceRadius: '',
    location: ''
  });

  // Function to handle form submission
  const handleAddressSubmit = (e) => {
    e.preventDefault();
    onAddressSubmit(filterOps.location);
    console.log("Address" + filterOps.location);
  };

  // Function to handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFilterOps({
      ...filterOps,
      [name]: value
    });
  };

  const handlePriceChange = (e) => {
    const {value} = e.target;
    handleChange(e);
    onPriceChange(value);
  
  };

  const handleTimeChange = (e) => {
    const {value} = e.target;
    handleChange(e);
    onTimeChange(value);
  }

  const handleAddressChange = (e) => {
    const {value} = e.target;
    // console.log("Hello1 " + value);
    handleChange(e);
    onAddressChange(value);
  }

  const handleDistanceChange = (e) => {
    const {value} = e.target;
    handleChange(e);
    onDistanceChange(value);
  }


  const handleSubmit = (e) => {
    e.preventDefault();
    onAddressSubmit(filterOps.location);
    onFilterSubmit();
  }

  return (
    <div className="form-container">
      <h2 id="title">Tailor your Parking!</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="price">Price:</label>
          <select name="price" id="price" value={filterOps.price} onChange={handlePriceChange}>
            <option value="">Select Price</option>
            <option value="0-20">$0-20 per hour</option>
            <option value="20-40">$20-40 per hour</option>
            <option value="40">$Above 40 per hour</option>
            <option value="all">All</option>
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="openTime">Open Time:</label>
          {/* <select name="openTime" id="openTime" value={filterOps.openTime} onChange={handleChange}>
            <option value="">Select</option>
            <option value="9am-9pm">9am-9pm</option>
            <option value="10am-10pm">10am-10pm</option>
            <option value="11am-11pm">11am-11pm</option>
            <option value="all">All</option>
          </select> */}
          <select name="openTime" id="openTime" value={filterOps.openTime} onChange={handleTimeChange}>
          <option value="">Select Hour</option>
          {[...Array(24)].map((_, hour) => (
            <option key={hour} value={hour}>
              {hour}:00
            </option>
          ))}
        </select>
        </div>
        <div className="form-group">
          <label htmlFor="location">Destination:</label>
          <input type="text" id="location" name="location" value={filterOps.location} onChange={handleAddressChange} />
        </div>
        <div className="form-group">
          <label htmlFor="distanceRadius">Distance (to Destination):</label>
          <select name="distanceRadius" id="distanceRadius" value={filterOps.distanceRadius} onChange={handleDistanceChange}>
            <option value="">Select Distance</option>
            <option value="2">2 miles</option>
            <option value="1">1 miles</option>
            <option value="0.5">0.5 miles</option>
          </select>
        </div>
        
        <div className="submit-btn-container">
          <button type="submit">Filter</button>
        </div>
      </form>
    </div>
  );
};

export default FilterBar;

