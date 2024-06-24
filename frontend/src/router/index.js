import { createRouter, createWebHistory } from 'vue-router';
import DeleteConfirmationDialog from '../components/DeleteConfirmationDialog.vue';
import AddModal from '../components/AddModal.vue';
import EditModal from '../components/EditModal.vue';
import UploadedImages from '../components/UploadedImages.vue';

const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/delete/:id',
    name: 'DeleteConfirmation',
    component: DeleteConfirmationDialog,
    props: true
  },
  {
    path: '/add',
    name: 'Add',
    component: AddModal
  },
  {
    path: '/edit/:id',
    name: 'Edit',
    component: EditModal,
    props: true
  },
  {
    path: '/images',
    name: 'UploadedImages',
    component: UploadedImages
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
