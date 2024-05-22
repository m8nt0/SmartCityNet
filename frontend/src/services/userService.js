import axios from 'axios';

const getUsers = () => {
  return axios.get('/api/users/')
    .then(response => response.data)
    .catch(error => console.error("There was an error fetching the users!", error));
};

export default {
  getUsers
};
