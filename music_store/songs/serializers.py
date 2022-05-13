from rest_framework import serializers
from music_store.genre.serializers import GenreSerializer
from .models import *

class SongSerializer(serializers.ModelSerializer):
	#genre = serializers.StringRelatedField(many=True, read_only=True)
	genre = GenreSerializer(many=True, read_only=True)
	class Meta:
		model = Song
		fields = ['name', 'duration', 'audio', 'genre']
		#depth = 1;

class SongsGenreSerializer(serializers.ModelSerializer):

	#song = serializers.StringRelatedField()
	#genre = serializers.StringRelatedField()

	class Meta:
		model = SongsGenre
		fields = ['id', 'song', 'genre']