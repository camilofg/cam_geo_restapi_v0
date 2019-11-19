from rest_framework import serializers
from .models import Item, Element


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('description', 'creation_date')


class ElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Element
        fields = ('description', 'serial')
