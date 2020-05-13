from rest_framework import serializers
from .models import Movies, Reviews, Rating


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['title', 'country', 'year']



class ReviewSerialazaerCreate(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = '__all__'



class MoviesSerializerDetail(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    reviews = ReviewSerialazaerCreate (many=True)


    class Meta:
        model = Movies
        exclude = ['url', 'posts']




class ReviewSerialazerView(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['email', 'name', 'title']


class RatingSerialazerCreate(serializers.ModelSerializer):


    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            ip = validated_data.get('ip', None),
            movie = validated_data.get('movie', None),
            defaults=('star',validated_data.get('star'))
        )
