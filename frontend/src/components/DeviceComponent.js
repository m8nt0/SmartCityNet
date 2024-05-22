import React, { useState } from 'react';

function DeviceComponent() {
  const [devices, setDevices] = useState([]);

  // Function to fetch devices from API
  const fetchDevices = async () => {
    try {
      const response = await fetch('api/devices');
      if (response.ok) {
        const data = await response.json();
        setDevices(data.devices);
      } else {
        throw new Error('Failed to fetch devices');
      }
    } catch (error) {
      console.error('Error fetching devices:', error.message);
    }
  };

  return (
    <div className="DeviceComponent">
      <h2>Devices</h2>
      <button onClick={fetchDevices}>Fetch Devices</button>
      <ul>
        {devices.map((device, index) => (
            <li key={index}>{
                `Device ID: ${device.id}, Type: ${device.type}, Location: ${device.location}`
            }</li>
        ))}
      </ul>
    </div>
  );
}

export default DeviceComponent;
