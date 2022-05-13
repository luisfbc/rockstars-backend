from django.db import models
from music_store.genre.models import Genre

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length = 256)
    duration = models.CharField(max_length = 256)
    audio = models.TextField()
    genre = models.ManyToManyField(Genre, through="SongsGenre")

    def __str__(self):
        return f'{self.name}'


class SongsGenre(models.Model):
    song = models.ForeignKey(Song, related_name='SongWithGenre', on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre, related_name='GenreWithSong', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name}'