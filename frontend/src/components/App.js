import React from 'react';
import UserComponent from './components/UserComponent';
import DeviceComponent from './components/DeviceComponent';
import NetworkComponent from './components/NetworkComponent';

function App() {
  return (
    <div className="App">
      <UserComponent />
      <DeviceComponent />
      <NetworkComponent />
    </div>
  );
}

export default App;
