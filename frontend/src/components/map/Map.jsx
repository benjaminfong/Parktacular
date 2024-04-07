import React, { useState, useEffect } from "react";
import { GoogleMap, useJsApiLoader, MarkerF, InfoWindowF } from '@react-google-maps/api';
import axios from 'axios';
import "./map.css";
import parkingLots from "./maps-data.json"


// const sfBounds = {
//   north: 37.812,
//   south: 37.708,
//   east: -122.324,
//   west: -122.524,
// }

const createNumberIcon = (number) => {
  const svg = encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 50 50">
    <path fill="#ff3025" d="M45 1H5v40h15.093l5.439 8.05l5.44-8.05H45z"/>
    <text x="50%" y="50%" alignment-baseline="middle" text-anchor="middle" fill="white" font-size="15" font-family="Helvetica">${number}</text>
  </svg>`);

  return `data:image/svg+xml,${svg}`;
};

const getLatLong = async (address) => {
  try {
    const response = await axios.get(`https://maps.googleapis.com/maps/api/geocode/json`, {
      params: {
        address: address,
        key: "AIzaSyB6rIDQSME3Qqstx1x4WDRUvBGMSSVJuNY"
      }
    });

    const locationData = response.data.results[0];
    const { lat, lng } = locationData.geometry.location;
    return { lat, lng };
  } catch (error) {
    console.error('Error fetching location data in getLatLong:', error);
  }

};

const Map = ({ address, submitTrigger }) => {
  const { isLoaded } = useJsApiLoader({
    id: 'google-map-script',
    googleMapsApiKey: "AIzaSyB6rIDQSME3Qqstx1x4WDRUvBGMSSVJuNY"
  })

  const [map, setMap] = useState(null)

  const [activeMarker, setActiveMarker] = useState(null)

  const [places, setPlaces] = useState([]);

  const [center, setCenter] = useState({lat: 37.784, lng: -122.407})


  const handleMarkerClick = (parkingLot) => {
    setActiveMarker(parkingLot.id);
    setCenter({lat: parseFloat(parkingLot.lat), lng: parseFloat(parkingLot.long)});
  }

  useEffect(() => {
    setPlaces(parkingLots);
    if (address) {
      const fetchData = async () => {
        try {
          const { lat, lng } = await getLatLong(address); 
          setCenter({ lat, lng });
        } catch (error) {
          console.error('Error fetching lat and lng:', error);
        }
      };
  
    // Call the fetchData function
      fetchData();
    }
  }, [address, submitTrigger]); // Run only once when the component mounts

  if (!isLoaded) {
    return <h1>Loading Map</h1>
  }

  return (
    <div className="map">
      <GoogleMap
        center={center}
        zoom={13}
        mapContainerStyle={{
          width: '100%',
          height: '100%'
        }}
        onLoad={map => setMap(map)}
        options={{
            streetViewControl: false,
            mapTypeControl: false,
            fullscreenControl: false,
            clickableIcons: false,
            minZoom: 12,
          }}>
            { 
              places.map((parkingLot) => (
                <MarkerF 
                  key={parkingLot.id}
                  position={{lat: parseFloat(parkingLot.lat), lng: parseFloat(parkingLot.long)}}
                  onClick={() => setActiveMarker(parkingLot.id)}
                  icon={
                    {  url: createNumberIcon(parkingLot.id),
                      scaledSize: new window.google.maps.Size(40, 35) }}
                >
                  { activeMarker === parkingLot.id ? 
                    <InfoWindowF onCloseClick={() => setActiveMarker(null)}>
                      <div>{parkingLot.facility_name}, {parkingLot.street_address}</div>
                    </InfoWindowF> : <></>
                  }
                </MarkerF>
            ))}
      </GoogleMap>
      <div style={{ position: 'absolute', top: '10px', left: '10px', zIndex: 9999 }}>
        <button className='center-btn' onClick={() => map.panTo(center)}>Center</button>
      </div>
    </div>
  );
};

export default Map;