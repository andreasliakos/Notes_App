<template>
  <div class="modal" @click.self="$emit('cancel')">
    <div class="modal-content">
      <span class="close" @click="$emit('cancel')">&times;</span>
      <h2>Edit Note</h2>
      <form @submit.prevent="save">
        <div class="form-group">
          <label>Title:</label>
          <input type="text" v-model="editedNote.title" required>
        </div>
        <div class="form-group">
          <label>Description:</label>
          <textarea v-model="editedNote.description"></textarea>
        </div>
        <div class="button-group">
          <button type="submit" class="button primary">Save</button>
          <button type="button" class="button secondary" @click="$emit('cancel')">Cancel</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: ['note'],
  data() {
    return {
      editedNote: {
        id: '',
        title: '',
        description: '',
        note_type: ''
      }
    };
  },
  watch: {
    note: {
      handler: function(newNote) {
        this.editedNote.id = newNote.id;
        this.editedNote.title = newNote.title;
        this.editedNote.description = newNote.description;
        this.editedNote.note_type = newNote.note_type;
      },
      immediate: true
    }
  },
  methods: {
    save() {
      this.$emit('save', this.editedNote);
      this.editedNote = { id: '', title: '', description: '', note_type: '' };
    }
  }
};
</script>

<style scoped>
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
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
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

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}

.close:hover {
  color: #fff;
}

.form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

label {
  font-weight: bold;
}

input[type="text"],
textarea,
select {
  width: 100%;
  padding: 8px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.select {
  width: 100%;
}

.button-group {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 20px;
}

.button {
  padding: 10px 20px;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  font-size: 14px;
}

.button.primary {
  background-color: #0dce17;
  color: white;
}

.button.secondary {
  background-color: #333;
  color: white;
}

.button:hover {
  opacity: 0.8;
}
</style>
