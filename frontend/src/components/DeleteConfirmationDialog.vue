<template>
  <div class="delete-dialog">
    <div class="delete-dialog-content">
      <p class="delete-dialog-message">Are you sure you want to delete this note?</p>
      <div class="delete-dialog-buttons">
        <button @click="confirmDelete" class="delete-dialog-confirm">Delete</button>
        <button @click="cancelDelete" class="delete-dialog-cancel">Cancel</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    note: Object,
  },
  methods: {
    confirmDelete() {
      this.$emit('confirm', this.note);
    },
    cancelDelete() {
      this.$emit('cancel');
    },
  },
};
</script>

<style scoped>
.delete-dialog {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  background-color: rgba(0, 0, 0, 0.5);
  overflow: hidden;
}

.delete-dialog-content {
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 30px;
  width: 80%;
  max-width: 600px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  position: relative;
  text-align: center;
  color: #fff;
}

.delete-dialog-message {
  margin-bottom: 20px;
}

.delete-dialog-buttons {
  display: flex;
  justify-content: center;
}

.delete-dialog-buttons button {
  margin: 0 10px;
}

.delete-dialog-confirm,
.delete-dialog-cancel {
  padding: 12px 24px;
  border: none;
  border-radius: 24px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.delete-dialog-confirm {
  background-color: #d32f2f;
  color: white;
}

.delete-dialog-cancel {
  background-color: #333;
  color: white;
}

.delete-dialog-confirm:hover {
  background-color: #cf2114;
}

.delete-dialog-cancel:hover {
  background-color: #555;
}
</style>
