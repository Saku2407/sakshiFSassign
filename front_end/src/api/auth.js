import axios from 'axios';

export const login = (data) =>
  axios.post('http://localhost:8000/api/users/login/', data);

export const getProfile = (token) =>
  axios.get('http://localhost:8000/api/users/profile/', {
    headers: { Authorization: `Bearer ${token}` }
  });
