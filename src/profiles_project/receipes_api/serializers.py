from rest_framework import serializers

from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)
    another_name = serializers.CharField(max_length=10)


class ReceipeList(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    title = serializers.CharField(max_length=255)
    image = serializers.CharField(max_length=255)
    instructions = serializers.CharField(max_length=255)


class ReceipeSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    title = serializers.CharField(max_length=255)
    ingredient_list = serializers.CharField(max_length=255)
    instruction_list = serializers.CharField(max_length=255)
    image = serializers.CharField(max_length=255)
    # what = serializers.JSONField(False)


class IngredientSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=255)
    image = serializers.CharField(max_length=255)
    portion = serializers.IntegerField()


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        print(validated_data['name'])

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
