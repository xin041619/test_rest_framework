from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Set, Card


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('question', 'answer')


class SetSerializer(serializers.Serializer):
    set_id = serializers.ModelField(model_field=Set._meta.get_field('set_id'))
    pub_date = serializers.DateTimeField()
    cards = CardSerializer(many=True)
    pass
