from rest_framework import serializers
from watchlist_app.models import Watchlist, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('watchlist',)
    
    def validate_rating(self, value):
        if value > 5 or value < 0:
            raise serializers.ValidationError('Rating must be between 0 and 5')
        else:
            return value


class WatchlistSerializer(serializers.ModelSerializer):
    
    review = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')
    
    class Meta:
        model = Watchlist
        fields = "__all__"
    
    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name must be more than 2 characters long.')
        else:
            return value
    
    def validate(self, data):
        if data['title'] == data['storyline']:
            raise serializers.ValidationError('title and storyline cannot be the same.')
        else:
            return data

class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="movie-detail"
    )
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        

        def validate_website(self, value):
            if "www." not in value:
                raise serializers.ValidationError('Website must start with "www."')
            else:
                return value
        
        def validate(self, data):
            if data['name'] == data['about']:
                raise serializers.ValidationError('name and about sections cannot be the same.')
            else:
                return data

            
# class MovieSerializer(serializers.ModelSerializer):

#     len_of_name = serializers.SerializerMethodField()

#     def get_len_of_name(self, object):
#         return len(object.name)

#     class Meta:
#         model = Movie
#         fields = "__all__"
    
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name must be more than 2 characters long.')
#         else:
#             return value
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and description cannot be the same.')
#         else:
#             return data 
        



"""this is the function based view of the serializer"""

# def description_len(value):
#     if len(value) > 100:
#         raise serializers.ValidationError('Description must be less than 100 characters long.')
#     else:
#         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[description_len])
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
        
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name must be more than 2 characters long.')
#         else:
#             return value
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and description cannot be the same.')
#         else:
#             return data