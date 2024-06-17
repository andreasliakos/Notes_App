import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/api/';

export default {
  fetchNotes() {
    return axios.get(`${BASE_URL}notes/all/`)
      .then(response => {
        console.log('Notes fetched successfully:', response.data);
        return response.data;
      })
      .catch(error => {
        console.error('Error fetching notes:', error);
        throw error;
      });
  },
};
