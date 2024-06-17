<template>
  <div id="app" class="container">
    <!-- Header and Add button -->
    <header class="header">
      <h1>Note Taking App</h1>
      <button class="add-note-button" @click="openAddModal">
        <span>Add</span>
      </button>
    </header>

    <!-- Note table -->
    <div class="content">
      <table class="notes-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Title</th>
            <th>Description</th>
            <th>Note Type</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="note in notes" :key="note.id" @click="openNoteModal(note)">
            <td class="note-id">{{ note.id }}</td>
            <td>{{ note.title }}</td>
            <td>{{ note.description }}</td>
            <td>{{ getNoteTypeName(note.note_type) }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modal for Note Details -->
    <div class="modal" v-if="selectedNote !== null">
      <div class="modal-content">
        <span class="close" @click="closeNoteModal">&times;</span>
        <h2>Note Details</h2>
        <div class="note-detail">
          <div><strong>ID:</strong> {{ selectedNote.id }}</div>
          <div><strong>Title:</strong> {{ selectedNote.title }}</div>
          <div><strong>Description:</strong> {{ selectedNote.description }}</div>
          <div><strong>Note Type:</strong> {{ getNoteTypeName(selectedNote.note_type) }}</div>
        </div>
        <!-- Buttons section -->
        <div class="button-group">
          <button class="button primary" @click="openEditModal">Edit</button>
          <button class="button danger" @click="openDeleteModal">Delete</button>
        </div>
      </div>
    </div>

    <!-- AddModal component -->
    <AddModal v-if="isAdding" @save="saveNewNote" @cancel="cancelAdding" />

    <!-- EditModal component -->
    <EditModal v-if="isEditing" :note="selectedNote" @save="saveEditedNote" @cancel="cancelEditing" />

    <!-- DeleteConfirmationDialog component -->
    <DeleteConfirmationDialog v-if="isDeleting" @confirm="deleteNote" @cancel="cancelDeleting" />

    <!-- Footer -->
    <footer class="footer">
      <p>&copy; 2024 Note Taking App</p>
    </footer>
  </div>
</template>

<script>
import AddModal from './components/AddModal.vue';
import EditModal from './components/EditModal.vue';
import DeleteConfirmationDialog from './components/DeleteConfirmationDialog.vue';
import api from './api';

export default {
  name: 'App',
  components: {
    AddModal,
    EditModal,
    DeleteConfirmationDialog
  },
  data() {
    return {
      notes: [],
      isAdding: false,
      isEditing: false,
      isDeleting: false,
      selectedNote: null
    };
  },
  methods: {
    fetchNotes() {
      api.getNotes()
        .then(response => {
          this.notes = response.data;
        })
        .catch(error => {
          console.error('Error fetching notes:', error);
        });
    },
    getNoteTypeName(noteType) {
      switch (noteType) {
        case 0:
          return 'Default';
        case 1:
          return 'Image';
        case 2:
          return 'Checkbox';
        default:
          return 'Default';
      }
    },
    openAddModal() {
      this.isAdding = true;
    },
    saveNewNote(newNote) {
      switch (newNote.note_type) {
        case 0:
          api.createDefaultNote(newNote)
            .then(response => {
              this.notes.push(response.data);
            })
            .catch(error => {
              console.error('Error saving note:', error);
            })
            .finally(() => {
              this.isAdding = false;
            });
          break;
        case 1:
          api.createImageNote(newNote)
            .then(response => {
              this.notes.push(response.data);
            })
            .catch(error => {
              console.error('Error saving note:', error);
            })
            .finally(() => {
              this.isAdding = false;
            });
          break;
        case 2:
          api.createCheckboxNote(newNote)
            .then(response => {
              this.notes.push(response.data);
            })
            .catch(error => {
              console.error('Error saving note:', error);
            })
            .finally(() => {
              this.isAdding = false;
            });
          break;
        default:
          console.error('Invalid note type:', newNote.note_type);
          this.isAdding = false;
          break;
      }
    },
    cancelAdding() {
      this.isAdding = false;
    },
    openNoteModal(note) {
      this.selectedNote = note;
    },
    closeNoteModal() {
      this.selectedNote = null;
    },
    openEditModal() {
      this.isEditing = true;
    },
    saveEditedNote(editedNote) {
      switch (editedNote.note_type) {
        case 0:
          api.updateDefaultNote(editedNote)
            .then(response => {
              const index = this.notes.findIndex(note => note.id === editedNote.id);
              this.notes.splice(index, 1, response.data);
            })
            .catch(error => {
              console.error('Error updating note:', error);
            })
            .finally(() => {
              this.isEditing = false;
              this.selectedNote = null;
            });
          break;
        case 1:
          api.updateImageNote(editedNote)
            .then(response => {
              const index = this.notes.findIndex(note => note.id === editedNote.id);
              this.notes.splice(index, 1, response.data);
            })
            .catch(error => {
              console.error('Error updating note:', error);
            })
            .finally(() => {
              this.isEditing = false;
              this.selectedNote = null;
            });
          break;
        case 2:
          api.updateCheckboxNote(editedNote)
            .then(response => {
              const index = this.notes.findIndex(note => note.id === editedNote.id);
              this.notes.splice(index, 1, response.data);
            })
            .catch(error => {
              console.error('Error updating note:', error);
            })
            .finally(() => {
              this.isEditing = false;
              this.selectedNote = null;
            });
          break;
        default:
          console.error('Invalid note type:', editedNote.note_type);
          this.isEditing = false;
          this.selectedNote = null;
          break;
      }
    },
    cancelEditing() {
      this.isEditing = false;
      this.selectedNote = null;
    },
    openDeleteModal() {
      this.isDeleting = true;
    },
    deleteNote() {
      if (this.selectedNote) {
        switch (this.selectedNote.note_type) {
          case 0:
            api.deleteDefaultNote(this.selectedNote.id)
              .then(() => {
                this.notes = this.notes.filter(note => note.id !== this.selectedNote.id);
              })
              .catch(error => {
                console.error('Error deleting note:', error);
              })
              .finally(() => {
                this.isDeleting = false;
                this.selectedNote = null;
              });
            break;
          case 1:
            api.deleteImageNote(this.selectedNote.id)
              .then(() => {
                this.notes = this.notes.filter(note => note.id !== this.selectedNote.id);
              })
              .catch(error => {
                console.error('Error deleting note:', error);
              })
              .finally(() => {
                this.isDeleting = false;
                this.selectedNote = null;
              });
            break;
          case 2:
            api.deleteCheckboxNote(this.selectedNote.id)
              .then(() => {
                this.notes = this.notes.filter(note => note.id !== this.selectedNote.id);
              })
              .catch(error => {
                console.error('Error deleting note:', error);
              })
              .finally(() => {
                this.isDeleting = false;
                this.selectedNote = null;
              });
            break;
          default:
            console.error('Invalid note type:', this.selectedNote.note_type);
            this.isDeleting = false;
            this.selectedNote = null;
            break;
        }
      }
    },
    cancelDeleting() {
      this.isDeleting = false;
      this.selectedNote = null;
    }
  },
  created() {
    this.fetchNotes();
  }
};
</script>

<style>
html,
body {
  height: 100%;
  margin: 0;
}

body {
  background: linear-gradient(45deg, #49a09d, #5f2c82);
  font-family: 'Roboto', sans-serif;
  font-weight: 100;
  display: flex;
  align-items: center;
  justify-content: center;
}

.container {
  text-align: center;
  color: #fff;
}

.header {
  margin-bottom: 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h1 {
  font-size: 28px;
  color: #fff;
  margin: 0;
}

.add-note-button {
  background: #55608f;
  color: #ffffff;
  border: none;
  padding: 12px 30px;
  border-radius: 10px;
  cursor: pointer;
  font-size: 16px;
  transition: background 0.3s ease;
}

.add-note-button:hover {
  background: #55608f;
}

.notes-table {
  width: 800px;
  border-collapse: collapse;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.notes-table th,
.notes-table td {
  padding: 15px;
  background-color: rgba(255, 255, 255, 0.2);
  color: #fff;
}

.notes-table th {
  text-align: left;
}

.notes-table thead th {
  background-color: #55608f;
}

.notes-table tbody tr:hover {
  background-color: rgba(255, 255, 255, 0.3);
}

.notes-table tbody td {
  position: relative;
}


.footer {
  text-align: center;
  padding: 15px;
  color: #fff;
  border-top: 2px solid #ddd;
  margin-top: 30px;
}

.modal {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  background-color: rgba(0, 0, 0, 0.7);
}

.modal-content {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 30px;
  width: 80%;
  max-width: 600px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  position: relative;
  text-align: left;
  color: #fff;
}

.close {
  position: absolute;
  top: 15px;
  right: 15px;
  color: #aaa;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}

.close:hover,
.close:focus {
  color: #fff;
}

.note-detail {
  text-align: left;
  margin-bottom: 30px;
}

.note-detail div {
  margin-bottom: 12px;
}

.button-group {
  display: flex;
  justify-content: center;
  margin-top: 25px;
  gap: 10px;
}

.button {
  padding: 12px 24px;
  border: none;
  border-radius: 24px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.button.primary {
  background-color: #55608f;
  color: white;
}

.button.danger {
  background-color: #cf2114;
  color: white;
}

.button:hover {
  opacity: 0.9;
}
</style>

