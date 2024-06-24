<template>
  <div class="modal" @click.self="$emit('cancel')">
    <div class="modal-content">
      <span class="close" @click="$emit('cancel')">&times;</span>
      <h2 class="text-2xl font-bold mb-4">Edit Note</h2>
      <form @submit.prevent="save" class="form">
        <div class="form-group">
          <label>Title:</label>
          <input type="text" v-model="editedNote.title" required>
        </div>
        <div class="form-group">
          <label>Description:</label>
          <textarea v-model="editedNote.description"></textarea>
        </div>
        <div class="form-group" v-if="editedNote.note_type === 1">
          <label>New Image:</label>
          <input type="file" @change="handleImageChange">
        </div>
        <div class="form-group" v-if="editedNote.note_type === 2">
          <label>Checkbox Tick:</label>
          <input type="checkbox" v-model="editedNote.checkbox_tick">
        </div>
        <div class="image-preview-container" v-if="imagePreviewUrl">
          <img :src="imagePreviewUrl" class="image-preview">
        </div>
        <div v-if="editedNote.image" class="show-image-button-container">
          <button type="button" class="button secondary" @click="showImage">Show Image</button>
        </div>
        <div class="button-group">
          <button type="submit" class="button primary" :disabled="loading">Save</button>
          <button type="button" class="button secondary" @click="$emit('cancel')" :disabled="loading">Cancel</button>
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
    const editedNote = ref({
      id: '',
      title: '',
      description: '',
      note_type: '',
      image: null,
      checkbox_tick: false
    });

    const imageFile = ref(null);
    const imagePreviewUrl = ref(null);
    const loading = ref(false);

    const initializeNote = () => {
      const { id, title, description, note_type, image, checkbox_tick } = props.note;
      editedNote.value = {
        id,
        title,
        description,
        note_type,
        image,
        checkbox_tick: checkbox_tick || false
      };
    };

    const save = () => {
      loading.value = true;

      if (editedNote.value.note_type === 1 && imageFile.value) {
        editedNote.value.image = imageFile.value;
      }

      emit('save', editedNote.value);

      setTimeout(() => {
        loading.value = false;
        resetForm();
      }, 1000);
    };

    const handleImageChange = (event) => {
      imageFile.value = event.target.files[0];
      imagePreviewUrl.value = URL.createObjectURL(imageFile.value);
    };

    const showImage = () => {
      if (editedNote.value.image) {
        window.open(editedNote.value.image);
      }
    };

    const resetForm = () => {
      editedNote.value = {
        id: '',
        title: '',
        description: '',
        note_type: '',
        image: null,
        checkbox_tick: false
      };
      imageFile.value = null;
      imagePreviewUrl.value = null;
    };

    initializeNote();
    return {
      editedNote,
      imageFile,
      imagePreviewUrl,
      loading,
      save,
      handleImageChange,
      showImage,
      resetForm
    };
  }
});
</script>

<style scoped>
@import '../assets/styles/editmodal.css';
</style>
