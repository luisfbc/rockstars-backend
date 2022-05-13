from django.db import models
from music_store.genre.models import Genre
from music_store.songs.models import Song

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length = 256)
    price = models.DecimalField(max_digits = 6, decimal_places = 2, default=0)
    release_year = models.SmallIntegerField(default = 0)
    cover = models.TextField()
    genre = models.ManyToManyField(Genre, through="AlbumGenre")
    songs = models.ManyToManyField(Song, through="AlbumSongs")

    def __str__(self):
        return f'{self.name}'


class AlbumGenre(models.Model):
    album = models.ForeignKey(Album, related_name='AlbumWithGenre', on_delete=models.DO_NOTHING)
    genre = models.ForeignKey(Genre, related_name='GenreWithAlbum', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name}'

class AlbumSongs(models.Model):
    album = models.ForeignKey(Album, related_name='AlbumWithSong', on_delete=models.DO_NOTHING)
    songs = models.ForeignKey(Song, related_name='SongWithAlbum', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name}'