// src/api/pexels.js (facultatif si tu veux centraliser)
import axios from 'axios';

const instance = axios.create({
  baseURL: 'https://api.pexels.com/v1',
  headers: {
    Authorization: 'Y'
  }
});

export default instance;
