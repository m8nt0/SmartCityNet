import axios from 'axios';

const getNetworks = () => {
  return axios.get('/api/networks/')
    .then(response => response.data)
    .catch(error => console.error("There was an error fetching the networks!", error));
};

export default {
  getNetworks
};
