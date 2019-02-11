from django.contrib.auth.models import User
from rest_framework import serializers
from MovieRaterApi.api.models import Movie, Rating


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description','image', 'avg_rating', 'no_of_ratings','image','fantasy','romance','action','director')


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('stars', 'user', 'movie')
