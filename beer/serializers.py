from builtins import object
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User

class BeerSerializer(object):
    def __init__(self, body):
        self.body = body
    
    @property
    def all_beers(self):
        output = {'beers': []}

        for beer in self.body:
            beer_details = {
                'beer_name': beer.beer_name,
                'brewery': beer.brewery,
                'abv': beer.abv
            }
            output['beers'].append(beer_details)

        return output
    
    @property
    def beer_detail(self):
        return {
            'beer_name': self.body.beer_name,
            'brewery': self.body.brewery,
            'abv': self.body.abv
        }

# USER SERIALIZER

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')