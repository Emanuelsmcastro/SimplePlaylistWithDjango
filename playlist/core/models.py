from django.db import models
from imagekit.processors import ResizeToFit
from imagekit.models import ProcessedImageField

# Create your models here.
class Music(models.Model):
    image = ProcessedImageField(verbose_name='Imagem', upload_to='img/thumbs/', default='img/thumbs/default/default.jpg', processors=[ResizeToFit(600, 600)])
    title = models.CharField(verbose_name='Nome da Música', max_length=30, unique=True, primary_key=True)
    music = models.FileField(verbose_name='selecione a música', upload_to='audio/')
    
    def __str__(self) -> str:
        return f'title: {self.title}'