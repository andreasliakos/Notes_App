from django.db import models
class BaseNote(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    NOTE_TYPES = [
        (0, 'default'),
        (1, 'image'),
        (2, 'checkbox'),
    ]
    note_type = models.IntegerField(choices=NOTE_TYPES)
    
    def __str__(self):
        return self.title
    
    class Meta:
        abstract = True
        
class DefaultNoteType(BaseNote):
    note_type = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
          
class ImageNoteType(models.Model):
    note_type= models.IntegerField(default=1)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

class CheckboxNoteType(BaseNote):
    note_type= models.IntegerField(default=2)
    checkbox_list = models.JSONField(blank=True, null=True)    
    

    
        


