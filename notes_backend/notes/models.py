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
    def save(self, *args, **kwargs):
        self.note_type = 0
        super().save(*args, **kwargs)

class ImageNoteType(BaseNote):
    image = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        self.note_type = 1
        super().save(*args, **kwargs)

class CheckboxNoteType(BaseNote):
    title = models.CharField(max_length=255)
    description = models.TextField()  
    checkbox_tick = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.note_type = 2
        super().save(*args, **kwargs)
