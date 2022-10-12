from rest_framework import serializers
from .models import URLs


class URLsSerializerAuth(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = URLs
        fields = '__all__'
        read_only_fields = ('views',)


# class URLsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = URLs
#         fields = ('author', 'orig_url', 'short_url',)
