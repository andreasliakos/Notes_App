<template>
  <div class="modal" @click.self="$emit('cancel')">
    <div class="modal-content">
      <span class="close" @click="$emit('cancel')">&times;</span>
      <h2 class="text-2xl font-bold mb-4">Add Note</h2>
      <form @submit.prevent="save">
        <label class="block text-sm font-medium text-gray-700">Title:</label>
        <input type="text" v-model="newNote.title" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
        
        <label class="block text-sm font-medium text-gray-700 mt-4">Description:</label>
        <textarea v-model="newNote.description" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"></textarea>
        
        <label class="block text-sm font-medium text-gray-700 mt-4">Note Type:</label>
        <select v-model="newNote.note_type" @change="handleNoteTypeChange" required class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm">
          <option value="0">Default</option>
          <option value="1">Image</option>
          <option value="2">Checkbox</option>
        </select>

        <div v-if="newNote.note_type === '1'" class="mt-4 text-center">
          <label class="block text-sm font-medium text-gray-700">Image:</label>
          <input type="file" @change="handleImageUpload" class="mt-1 block w-full text-sm text-gray-900 border-gray-300 rounded-lg cursor-pointer focus:border-indigo-500 focus:ring-indigo-500">
          <div class="image-preview-container mt-2" v-if="newNote.imagePreviewUrl">
            <img :src="newNote.imagePreviewUrl" class="image-preview">
          </div>
        </div>

        <div v-if="newNote.note_type === '2'" class="mt-4">
          <label class="block text-sm font-medium text-gray-700">Checkbox Tick:</label>
          <input type="checkbox" v-model="newNote.checkbox_tick" class="h-4 w-4 text-indigo-600 border-gray-300 rounded focus:ring-indigo-500">
        </div>
    
        <div class="button-group">
          <button class="button primary" type="submit" :disabled="loading">Save</button>
          <button class="button danger" type="button" @click="$emit('cancel')" :disabled="loading">Cancel</button>
        </div>

        <div v-if="loading" class="loading-spinner-container">
          <div class="loading-spinner"></div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';

export default defineComponent({
  props: ['note'],
  setup(props, { emit }) {
    const newNote = ref({
      id: '',
      title: '',
      description: '',
      note_type: '0',
      checkbox_tick: false,
      image: null,
      imagePreviewUrl: ''
    });

    const loading = ref(false);

    const save = () => {
      loading.value = true;
      newNote.value.note_type = parseInt(newNote.value.note_type);

      setTimeout(() => {
        emit('save', newNote.value);
        resetNewNote();
        loading.value = false;
      }, 1000);
    };

    const handleNoteTypeChange = () => {
      if (newNote.value.note_type !== '1') {
        newNote.value.image = null;
        newNote.value.imagePreviewUrl = '';
      }
    };

    const handleImageUpload = (event) => {
      let selectedFile = event.target.files[0];
      if (!selectedFile) return;

      let reader = new FileReader();
      reader.onload = () => {
        newNote.value.image = selectedFile;
        newNote.value.imagePreviewUrl = reader.result;
      };
      reader.readAsDataURL(selectedFile);
    };

    const resetNewNote = () => {
      newNote.value = {
        id: '',
        title: '',
        description: '',
        note_type: '0',
        checkbox_tick: false,
        image: null,
        imagePreviewUrl: ''
      };
    };

    return {
      newNote,
      loading,
      save,
      handleNoteTypeChange,
      handleImageUpload,
      resetNewNote
    };
  }
});
</script>

<style scoped>
@import '../assets/styles/addmodal.css';
</style>