from rest_framework import serializers
from .models import *
from music_store.songs.serializers import SongSerializer

class AlbumSerializer(serializers.ModelSerializer):
	songs = serializers.StringRelatedField(many=True, read_only=True)
	#songs = SongSerializer(many=True, read_only=True)
	genre = serializers.StringRelatedField(many=True, read_only=True)
	class Meta:
		model = Album
		fields = ['name', 'cover', 'genre', 'songs']
		#depth = 1

class AlbumGenreSerializer(serializers.ModelSerializer):
	#song = serializers.StringRelatedField()
	#genre = serializers.StringRelatedField()
	class Meta:
		model = AlbumGenre
		fields = ['id', 'album', 'genre']

class AlbumSongsSerializer(serializers.ModelSerializer):
	#song = serializers.StringRelatedField()
	#genre = serializers.StringRelatedField()
	class Meta:
		model = AlbumSongs
		fields = ['id', 'album', 'songs']