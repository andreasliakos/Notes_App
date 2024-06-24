from django.urls import path
from .views import (
    UnifiedNoteView,
    CreateDefaultNoteAPIView,
    CreateImageNoteAPIView,
    CreateCheckboxNoteAPIView,
    UpdateDefaultNoteAPIView,
    UpdateImageNoteAPIView,
    UpdateCheckboxNoteAPIView,
    DeleteDefaultNoteAPIView,
    DeleteImageNoteAPIView,
    DeleteCheckboxNoteAPIView,
)

urlpatterns = [
    path('notes/all/', UnifiedNoteView.as_view(), name='note-list'),
    path('notes/create/default/', CreateDefaultNoteAPIView.as_view(), name='create-default-note'),
    path('notes/create/image/', CreateImageNoteAPIView.as_view(), name='create-image-note'),
    path('notes/create/checkbox/', CreateCheckboxNoteAPIView.as_view(), name='create-checkbox-note'),
    path('notes/update/default/<int:pk>/', UpdateDefaultNoteAPIView.as_view(), name='update-default-note'),
    path('notes/update/image/<int:pk>/', UpdateImageNoteAPIView.as_view(), name='update-image-note'),
    path('notes/update/checkbox/<int:pk>/', UpdateCheckboxNoteAPIView.as_view(), name='update-checkbox-note'),
    path('notes/delete/default/<int:pk>/', DeleteDefaultNoteAPIView.as_view(), name='delete-default-note'),
    path('notes/delete/image/<int:pk>/', DeleteImageNoteAPIView.as_view(), name='delete-image-note'),
    path('notes/delete/checkbox/<int:pk>/', DeleteCheckboxNoteAPIView.as_view(), name='delete-checkbox-note'),
    
]

