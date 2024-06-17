<template>
  <div class="modal" @click.self="$emit('cancel')">
    <div class="modal-content">
      <span class="close" @click="$emit('cancel')">&times;</span>
      <h2>Add Note</h2>
      <form @submit.prevent="save">
        <label>Title:</label>
        <input type="text" v-model="newNote.title" required>
        
        <label>Description:</label>
        <textarea v-model="newNote.description"></textarea>
        
        <label>Note Type:</label>
        <select v-model="newNote.note_type" required>
          <option value="0">Default</option>
          <option value="1">Image</option>
          <option value="2">Checkbox</option>
        </select>
        
        <div class="button-group">
          <button class="button primary" type="submit">Save</button>
          <button class="button danger" type="button" @click="$emit('cancel')">Cancel</button>
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
      newNote: {
        id: '',
        title: '',
        description: '',
        note_type: '0'
      }
    };
  },
  methods: {
    save() {
      this.newNote.note_type = parseInt(this.newNote.note_type);
      this.$emit('save', this.newNote);
      this.newNote = { id: '', title: '', description: '', note_type: '0' };
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

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 10px;
  color: #fff;
}

input,
textarea,
select {
  margin-top: 5px;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
  color: #333;
}

.button-group {
  display: flex;
  justify-content: center;
  margin-top: 25px;
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
  background-color: #0dce17;
  color: white;
}

.button.danger {
  background-color: #da2518;
  color: white;
}

.button:hover {
  opacity: 0.9;
}
</style>
