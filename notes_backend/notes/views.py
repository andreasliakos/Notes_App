from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED
from .models import DefaultNoteType, ImageNoteType, CheckboxNoteType
from .serializers import (
    DefaultNoteSerializer, 
    ImageNoteSerializer, 
    CheckboxNoteSerializer, 
    UpdateDefaultNoteSerializer,  
    UpdateImageNoteSerializer,  
    UpdateCheckboxNoteSerializer,
    DeleteDefaultNoteSerializer,  
    DeleteImageNoteSerializer,    
    DeleteCheckboxNoteSerializer, 
)
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

class UnifiedNoteView(APIView):
    def get(self, request):
        note_type = request.query_params.get('note_type')
        if note_type == 'default':
            notes = DefaultNoteType.objects.all()
            serializer = DefaultNoteSerializer(notes, many=True)
        elif note_type == 'image':
            notes = ImageNoteType.objects.all()
            serializer = ImageNoteSerializer(notes, many=True)
        elif note_type == 'checkbox':
            notes = CheckboxNoteType.objects.all()
            serializer = CheckboxNoteSerializer(notes, many=True)
        else:
            default_notes = DefaultNoteType.objects.all()
            image_notes = ImageNoteType.objects.all()
            checkbox_notes = CheckboxNoteType.objects.all()

            default_serializer = DefaultNoteSerializer(default_notes, many=True)
            image_serializer = ImageNoteSerializer(image_notes, many=True)
            checkbox_serializer = CheckboxNoteSerializer(checkbox_notes, many=True)

            data = default_serializer.data + image_serializer.data + checkbox_serializer.data
            return Response(data)

        return Response(serializer.data)

class CreateDefaultNoteAPIView(generics.CreateAPIView):
    queryset = DefaultNoteType.objects.all()
    serializer_class = DefaultNoteSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)

class CreateImageNoteAPIView(generics.CreateAPIView):
    queryset = ImageNoteType.objects.all()
    serializer_class = ImageNoteSerializer
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateCheckboxNoteAPIView(generics.CreateAPIView):
    queryset = CheckboxNoteType.objects.all()
    serializer_class = CheckboxNoteSerializer

class UpdateDefaultNoteAPIView(generics.RetrieveUpdateAPIView):
    queryset = DefaultNoteType.objects.all()
    serializer_class = UpdateDefaultNoteSerializer

class UpdateImageNoteAPIView(generics.UpdateAPIView):
    queryset = ImageNoteType.objects.all()
    serializer_class = UpdateImageNoteSerializer
    parser_classes = (MultiPartParser, FormParser)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)
   
class UpdateCheckboxNoteAPIView(generics.RetrieveUpdateAPIView):
    queryset = CheckboxNoteType.objects.all()
    serializer_class = UpdateCheckboxNoteSerializer

class DeleteDefaultNoteAPIView(generics.DestroyAPIView):
    queryset = DefaultNoteType.objects.all()
    serializer_class = DeleteDefaultNoteSerializer

class DeleteImageNoteAPIView(generics.DestroyAPIView):
    queryset = ImageNoteType.objects.all()
    serializer_class = DeleteImageNoteSerializer

class DeleteCheckboxNoteAPIView(generics.DestroyAPIView):
    queryset = CheckboxNoteType.objects.all()
    serializer_class = DeleteCheckboxNoteSerializer
    
