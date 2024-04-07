import React, { useState } from 'react';
import './filter-bar.css';

const FilterBar = ({ onAddressSubmit }) => {
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
  };

  // Function to handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFilterOps({
      ...filterOps,
      [name]: value
    });
  };

  return (
    <div className="form-container">
      <h2 id="title">Search Filters</h2>
      <form onSubmit={handleAddressSubmit}>
        <div className="form-group">
          <label htmlFor="location">Location:</label>
          <input type="text" id="location" name="location" value={filterOps.location} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label htmlFor="price">Price:</label>
          <select name="price" id="price" value={filterOps.price} onChange={handleChange}>
            <option value="">Select</option>
            <option value="10-20">$10-20 per hour</option>
            <option value="20-30">$20-30 per hour</option>
            <option value="30-40">$30-40 per hour</option>
            <option value="all">All</option>
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="openTime">Open Time:</label>
          <select name="openTime" id="openTime" value={filterOps.openTime} onChange={handleChange}>
            <option value="">Select</option>
            <option value="9am-9pm">9am-9pm</option>
            <option value="10am-10pm">10am-10pm</option>
            <option value="11am-11pm">11am-11pm</option>
            <option value="all">All</option>
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="distanceRadius">Distance Radius:</label>
          <select name="distanceRadius" id="distanceRadius" value={filterOps.distanceRadius} onChange={handleChange}>
            <option value="">Select</option>
            <option value="50">50 miles</option>
            <option value="100">100 miles</option>
            <option value="300">300 miles</option>
          </select>
        </div>
        <div className="submit-btn-container">
          <button type="submit">Submit</button>
        </div>
      </form>
    </div>
  );
};

export default FilterBar;
