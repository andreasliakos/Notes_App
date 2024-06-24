from rest_framework import serializers
from .models import DefaultNoteType, ImageNoteType, CheckboxNoteType

class DefaultNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultNoteType
        fields = '__all__'

class UpdateDefaultNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultNoteType
        fields = '__all__'
        
class DeleteDefaultNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultNoteType
        fields = []

class ImageNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNoteType
        fields = ['id', 'title', 'note_type', 'description', 'image']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['image'] = instance.image.url
        return representation
        

class UpdateImageNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNoteType
        fields = ['id', 'title', 'note_type', 'description', 'image']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image:
            representation['image'] = instance.image.url
        return representation
        
class DeleteImageNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNoteType
        fields = []

class CheckboxNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckboxNoteType
        fields = '__all__'

class UpdateCheckboxNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckboxNoteType
        fields = '__all__'
        
class DeleteCheckboxNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckboxNoteType
        fields = []

