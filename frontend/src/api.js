import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json'
  }
});


export default {
  getNotes() {
    return api.get('/notes/all/');
  },

  getNoteById(id) {
    return api.get(`/notes/${id}/`);
  },

  createDefaultNote(note) {
    return api.post('/notes/create/default/', note);
  },

  createImageNote(note) {
    const formData = new FormData();
    formData.append('id', note.id);
    formData.append('title', note.title);
    formData.append('description', note.description);
    formData.append('note_type', note.note_type);
    formData.append('image', note.image); 

    return api.post('/notes/create/image/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data' 
      }
    });
  },

  createCheckboxNote(note) {
    return api.post('/notes/create/checkbox/', note);
  },

  updateDefaultNote(note) {
    const { id, ...data } = note;
    return api.put(`/notes/update/default/${id}/`, data);
  },

  updateImageNote(note) {
  const { id, ...data } = note;
  const formData = new FormData();
  formData.append('id', id);
  formData.append('title', data.title);
  formData.append('description', data.description);
  formData.append('note_type', data.note_type);
  formData.append('image', data.image); 

  return api.put(`/notes/update/image/${id}/`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });
},

  updateCheckboxNote(note) {
    const { id, ...data } = note;
    return api.put(`/notes/update/checkbox/${id}/`, data);
  },

  deleteDefaultNote(id) {
    return api.delete(`/notes/delete/default/${id}/`);
  },

  deleteImageNote(id) {
    return api.delete(`/notes/delete/image/${id}/`);
  },

  deleteCheckboxNote(id) {
    return api.delete(`/notes/delete/checkbox/${id}/`);
  },
  updateNote(note) {
    const { id, ...data } = note;
    switch (note.note_type) {
      case 0:
        return api.put(`/notes/update/default/${id}/`, data);
      case 1:
        return api.put(`/notes/update/image/${id}/`, data);
      case 2:
        return api.put(`/notes/update/checkbox/${id}/`, data);
      default:
        throw new Error(`Invalid note type: ${note.note_type}`);
    }
  },

  deleteNoteById(id, noteType) {
    switch (noteType) {
      case 0:
        return api.delete(`/notes/delete/default/${id}/`);
      case 1:
        return api.delete(`/notes/delete/image/${id}/`);
      case 2:
        return api.delete(`/notes/delete/checkbox/${id}/`);
      default:
        throw new Error(`Invalid note type: ${noteType}`);
    }
  }
};