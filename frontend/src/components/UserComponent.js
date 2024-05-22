import React, { useState, useEffect } from 'react';
import userService from '../services/userService';

const UserComponent = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    userService.getUsers().then(data => setUsers(data));
  }, []);

  return (
    <div>
      <h2>Users</h2>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.username}</li>
        ))}
      </ul>
    </div>
  );
};

export default UserComponent;
