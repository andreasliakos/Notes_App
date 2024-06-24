<template>
  <div id="app" class="min-h-screen bg-gradient-to-br from-teal-400 to-purple-600 flex items-center justify-center font-roboto font-thin">
    <header class="container text-center text-white">
      <h1 class="header mb-8 flex justify-between items-center text-2xl font-bold">
        Note Taking App
        <button class="add-note-button bg-blue-600 text-white px-6 py-2 rounded transition duration-300 ease-in-out hover:bg-blue-700" @click="openAddModal">
          <span>Add</span>
        </button>
      </h1>
    </header>

    <div class="content">
      <router-view></router-view>
    </div>

    <div class="content">
      <table class="notes-table w-800 border-collapse overflow-hidden shadow-md">
        <thead>
          <tr class="bg-blue-700">
            <th class="p-4 text-left text-white">ID</th>
            <th class="p-4 text-left text-white">Title</th>
            <th class="p-4 text-left text-white">Description</th>
            <th class="p-4 text-left text-white">Note Type</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="note in notes" :key="note.id" @click="openNoteModal(note)" class="transition duration-300 ease-in-out hover:bg-opacity-30 cursor-pointer">
            <td class="p-4">{{ note.id }}</td>
            <td class="p-4">{{ note.title }}</td>
            <td class="p-4">{{ note.description }}</td>
            <td class="p-4">{{ getNoteTypeName(note.note_type) }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="modal fixed left-0 top-0 w-full h-full backdrop-filter backdrop-blur bg-black bg-opacity-70" v-if="selectedNote !== null">
      <div class="modal-content bg-opacity-20 rounded-lg p-8 w-4/5 max-w-2xl shadow-lg text-white">
        <span class="close absolute top-5 right-5 text-gray-300 text-2xl font-bold cursor-pointer" @click="closeNoteModal">&times;</span>
        <h2 class="text-2xl font-bold mb-4">Note Details</h2>
        <div class="note-detail">
          <div><strong>ID:</strong> {{ selectedNote.id }}</div>
          <div><strong>Title:</strong> {{ selectedNote.title }}</div>
          <div><strong>Description:</strong> {{ selectedNote.description }}</div>
          <div><strong>Note Type:</strong> {{ getNoteTypeName(selectedNote.note_type) }}</div>
          <div v-if="selectedNote.note_type === 2">
            <strong>Checkbox Tick:</strong>
            <span v-if="selectedNote.checkbox_tick"> Checked</span>
            <span v-else> Unchecked</span>
          </div>
          <div v-if="selectedNote.note_type === 1">
            <strong>Image:</strong>
            <div class="image-container">
              <img :src="getImageUrl(selectedNote.image)" class="note-image max-w-50 h-auto rounded-lg block transition-opacity duration-300 ease-in-out opacity-100 mx-auto my-0" v-if="selectedNote.imageVisible">
              <button class="button small bg-blue-600 text-white px-2 py-1 rounded-lg text-xs transition duration-300 ease-in-out hover:opacity-90" @click="toggleImageVisibility(selectedNote)">
                {{ selectedNote.imageVisible ? 'Hide Image' : 'Show Image' }}
              </button>
            </div>
          </div>
        </div>
        <div class="button-group flex justify-center mt-6 gap-4">
          <button class="button primary bg-blue-600 text-white rounded-lg px-6 py-3 transition duration-300 ease-in-out hover:bg-blue-700" @click="openEditModal">Edit</button>
          <button class="button danger bg-red-600 text-white rounded-lg px-6 py-3 transition duration-300 ease-in-out hover:bg-red-700" @click="openDeleteModal">Delete</button>
        </div>
      </div>
    </div>

    <AddModal v-if="isAdding" @save="saveNewNote" @cancel="cancelAdding" />

    <EditModal v-if="isEditing" :note="selectedNote" @save="saveEditedNote" @cancel="cancelEditing" />

    <DeleteConfirmationDialog v-if="isDeleting" @confirm="deleteNote" @cancel="cancelDeleting" />

    <footer class="footer text-center py-4 text-white border-t-2 border-gray-300 mt-6">
      <p>&copy; 2024 Note Taking App</p>
    </footer>

  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import AddModal from './components/AddModal.vue';
import EditModal from './components/EditModal.vue';
import DeleteConfirmationDialog from './components/DeleteConfirmationDialog.vue';
import api from './api';

export default {
  name: 'App',
  components: {
    AddModal,
    EditModal,
    DeleteConfirmationDialog,
  },
  setup() {
    const notes = ref([]);
    const isAdding = ref(false);
    const isEditing = ref(false);
    const isDeleting = ref(false);
    const selectedNote = ref(null);
    const baseUrl = 'http://127.0.0.1:8000';

    const fetchNotes = () => {
      api.getNotes()
        .then(response => {
          notes.value = response.data;
        })
        .catch(error => {
          console.error('Error fetching notes:', error);
        });
    };

    const getNoteTypeName = (noteType) => {
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
    };

    const openAddModal = () => {
      isAdding.value = true;
    };

    const saveNewNote = (newNote) => {
      switch (newNote.note_type) {
        case 0:
          api.createDefaultNote(newNote)
            .then(response => {
              notes.value.push(response.data);
            })
            .catch(error => {
              console.error('Error saving note:', error);
            })
            .finally(() => {
              isAdding.value = false;
            });
          break;
        case 1:
          api.createImageNote(newNote)
            .then(response => {
              notes.value.push(response.data);
            })
            .catch(error => {
              console.error('Error saving note:', error);
            })
            .finally(() => {
              isAdding.value = false;
            });
          break;
        case 2:
          api.createCheckboxNote(newNote)
            .then(response => {
              notes.value.push(response.data);
            })
            .catch(error => {
              console.error('Error saving note:', error);
            })
            .finally(() => {
              isAdding.value = false;
            });
          break;
        default:
          console.error('Invalid note type:', newNote.note_type);
          isAdding.value = false;
          break;
      }
    };

    const cancelAdding = () => {
      isAdding.value = false;
    };

    const openNoteModal = (note) => {
      selectedNote.value = note;
    };

    const closeNoteModal = () => {
      selectedNote.value = null;
    };

    const openEditModal = () => {
      isEditing.value = true;
    };

    const saveEditedNote = (editedNote) => {
      switch (editedNote.note_type) {
        case 0:
          api.updateDefaultNote(editedNote)
            .then(() => {
              const index = notes.value.findIndex(note => note.id === editedNote.id);
              if (index !== -1) {
                notes.value.splice(index, 1, editedNote);
              }
            })
            .catch(error => {
              console.error('Error updating note:', error);
            })
            .finally(() => {
              isEditing.value = false;
              selectedNote.value = null;
            });
          break;
        case 1:
          api.updateImageNote(editedNote)
            .then(() => {
              const index = notes.value.findIndex(note => note.id === editedNote.id);
              if (index !== -1) {
                notes.value.splice(index, 1, editedNote);
              }
            })
            .catch(error => {
              console.error('Error updating note:', error);
            })
            .finally(() => {
              isEditing.value = false;
              selectedNote.value = null;
            });
          break;
        case 2:
          api.updateCheckboxNote(editedNote)
            .then(() => {
              const index = notes.value.findIndex(note => note.id === editedNote.id);
              if (index !== -1) {
                notes.value.splice(index, 1, editedNote);
              }
            })
            .catch(error => {
              console.error('Error updating note:', error);
            })
            .finally(() => {
              isEditing.value = false;
              selectedNote.value = null;
            });
          break;
        default:
          console.error('Invalid note type:', editedNote.note_type);
          isEditing.value = false;
          selectedNote.value = null;
          break;
      }
    };

    const cancelEditing = () => {
      isEditing.value = false;
      selectedNote.value = null;
    };

    const openDeleteModal = () => {
      isDeleting.value = true;
    };

    const deleteNote = () => {
      if (selectedNote.value) {
        switch (selectedNote.value.note_type) {
          case 0:
            api.deleteDefaultNote(selectedNote.value.id)
              .then(() => {
                notes.value = notes.value.filter(note => note.id !== selectedNote.value.id);
              })
              .catch(error => {
                console.error('Error deleting note:', error);
              })
              .finally(() => {
                isDeleting.value = false;
                selectedNote.value = null;
              });
            break;
          case 1:
            api.deleteImageNote(selectedNote.value.id)
              .then(() => {
                notes.value = notes.value.filter(note => note.id !== selectedNote.value.id);
              })
              .catch(error => {
                console.error('Error deleting note:', error);
              })
              .finally(() => {
                isDeleting.value = false;
                selectedNote.value = null;
              });
            break;
          case 2:
            api.deleteCheckboxNote(selectedNote.value.id)
              .then(() => {
                notes.value = notes.value.filter(note => note.id !== selectedNote.value.id);
              })
              .catch(error => {
                console.error('Error deleting note:', error);
              })
              .finally(() => {
                isDeleting.value = false;
                selectedNote.value = null;
              });
            break;
          default:
            console.error('Invalid note type:', selectedNote.value.note_type);
            isDeleting.value = false;
            selectedNote.value = null;
            break;
        }
      }
    };

    const cancelDeleting = () => {
      isDeleting.value = false;
      selectedNote.value = null;
    };

    const toggleImageVisibility = (note) => {
      note.imageVisible = !note.imageVisible;
    };

    const getImageUrl = (image) => {
      return image ? `${baseUrl}${image}` : '';
    };

    onMounted(fetchNotes);

    return {
      notes,
      isAdding,
      isEditing,
      isDeleting,
      selectedNote,
      baseUrl,
      fetchNotes,
      getNoteTypeName,
      openAddModal,
      saveNewNote,
      cancelAdding,
      openNoteModal,
      closeNoteModal,
      openEditModal,
      saveEditedNote,
      cancelEditing,
      openDeleteModal,
      deleteNote,
      cancelDeleting,
      toggleImageVisibility,
      getImageUrl,
    };
  },
};
</script>

<style>
@import './assets/styles/app.css';
</style>
