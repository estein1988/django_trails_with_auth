from rest_framework import serializers
from .models import User, Trail, Review
from django.contrib.auth.hashers import make_password

class TrailObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trail
        fields = ('id', 'trail_name', 'location', 'difficulty', 'length', 'elevation')

class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'full_name', 'age', 'experience', 'reviews')

class ReviewObjectSerializer(serializers.ModelSerializer):
    trail = TrailObjectSerializer(many=False)
    class Meta:
        model = Review
        fields = ('id', 'trail', 'rating', 'review')

class UserSerializer(serializers.ModelSerializer):
    reviews = ReviewObjectSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'full_name', 'age', 'experience', 'reviews')

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
        )

        user.save()

        return user

class TrailSerializer(serializers.ModelSerializer):
    users = UserObjectSerializer(many=True)
    reviews = ReviewObjectSerializer(many=True)

    class Meta:
        model = Trail
        fields = ('id', 'trail_name', 'location', 'difficulty', 'length', 'elevation', 'users', 'reviews')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'trail', 'user')