from rest_framework import serializers
from .models import Artiste, Song, Lyric

class ArtisteSerializer(serializers.ModelSerializer):
    def __str__(self):
        #return self.first_name == first_name
        #return self.last_name == last_name   
        return f'{self.first_name}   {self.last_name}'
    
    class Meta:
        model = Artiste
        fields = ['id','first_name', 'last_name', 'age']
    
    
    
    
        
class SongSerializer(serializers.ModelSerializer):
    def __str__(self):
        # return f'{self.title}  {self.first_name}  {self.Artiste.{last_name}}'
        #return self.title
        return f'{self.title}  by    {self.artiste_id}'
        # return str(self.song_id)
    
    class Meta:
        model = Song
        fields = ['id', 'artiste_id', 'title', 'date_released', 'likes']  
    
    

class LyricSerializer(serializers.ModelSerializer):
    
    def __str__(self):
        # return HttpResponse({song_id})        
        #return str(self.song_id)
        return f' {self.song_id} song lyric'
    
    
    class Meta:
        model = Lyric
        fields = ['id', 'song_id', 'content']      
    