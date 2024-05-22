import React, { useState, useEffect } from 'react';
import networkService from '../services/networkService';

const NetworkComponent = () => {
  const [networks, setNetworks] = useState([]);

  useEffect(() => {
    networkService.getNetworks().then(data => setNetworks(data));
  }, []);

  return (
    <div>
      <h2>Networks</h2>
      <ul>
        {networks.map(network => (
          <li key={network.id}>{network.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default NetworkComponent;
