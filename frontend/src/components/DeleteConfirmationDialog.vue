<template>
  <div class="delete-dialog" @click.self="cancelDelete">
    <div class="delete-dialog-content">
      <p class="delete-dialog-message text-lg text-gray-700 mb-4">Are you sure you want to delete this note?</p>
      <div class="delete-dialog-buttons flex justify-end space-x-4">
        <button @click="confirmDelete" class="delete-dialog-confirm">Delete</button>
        <button @click="cancelDelete" class="delete-dialog-cancel">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'DeleteConfirmationDialog',
  props: {
    note: Object,
  },
  setup(props, { emit }) {
    const confirmDelete = () => {
      emit('confirm', props.note);
    };

    const cancelDelete = () => {
      emit('cancel');
    };

    return {
      confirmDelete,
      cancelDelete,
    };
  },
});
</script>

<style scoped>
@import '../assets/styles/delete.css';
</style>
