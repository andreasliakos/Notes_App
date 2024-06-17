# serializers.py

from rest_framework import serializers
from .models import DefaultNoteType, ImageNoteType, CheckboxNoteType

class DefaultNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultNoteType
        fields = '__all__'

class CreateDefaultNoteSerializer(serializers.ModelSerializer):
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
        fields = '__all__'
        
class CreateImageNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNoteType
        fields = '__all__'

class UpdateImageNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNoteType
        fields = '__all__'
        
class DeleteImageNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageNoteType
        fields = []

class CheckboxNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckboxNoteType
        fields = '__all__'

class CreateCheckboxNoteSerializer(serializers.ModelSerializer):
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
