import axios from 'axios';

const getDevices = () => {
  return axios.get('/api/devices/')
    .then(response => response.data)
    .catch(error => console.error("There was an error fetching the devices!", error));
};

export default {
  getDevices
};
