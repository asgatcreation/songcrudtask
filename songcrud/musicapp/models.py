from email.policy import default
# from __future__ import unicode_literals
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
from datetime import date
from django.http import HttpResponse
# from musicapp.models import Artiste, Song, Lyric 

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 400)
    last_name = models.CharField(max_length = 400)
    age = models.IntegerField()
    
    def __str__(self):
        #return self.first_name == first_name
        #return self.last_name == last_name   
        return f'{self.first_name}   {self.last_name}'
    
    class Meta:
        ordering = ('first_name','last_name')
     
        

class Song(models.Model):
    #artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length = 400)
    date_released = models.DateField(default = datetime.today)
    likes = models.IntegerField()
    #artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    
    def __str__(self):
        # return f'{self.title}  {self.first_name}  {self.Artiste.{last_name}}'
        #return self.title
        return f'{self.title}  by    {self.artiste_id}'
        # return str(self.song_id)
        # return "%s the waiter at %s" % (self.artiste.first_name, self.title)
        #reurn self.from_db.artiste_id
        
    class Meta:
        ordering = ('title',)

class Lyric(models.Model):
    song_id  = models.ForeignKey(Song, on_delete=models.CASCADE)
    # artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    #song = models.ForeignKey(Song, on_delete=models.CASCADE)
    # title = models.CharField(max_length = 40)
    content = models.TextField()
    
    
    def __str__(self):
        # return HttpResponse({song_id})        
        return str(self.song_id)
    
    class Meta:
        ordering = ('song_id',)
    # # def lyric():
    #     return song_id    
