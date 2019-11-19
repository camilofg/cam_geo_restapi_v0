from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ItemSerializer, ElementSerializer
from .models import Item, Element
from rest_framework.response import Response
from rest_framework import status


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all().order_by('description')
    serializer_class = ItemSerializer

    def put(self, request):
        data = request.data
        Item.objects.filter(pk=data['id']).update(description=data['description'])
        return Response(status=status.HTTP_200_OK)


class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all().order_by('description')
    serializer_class = ElementSerializer

    def put(self, request):
        data = request.data
        Element.objects.filter(pk=data['id']).update(description=data['description'], serial=data['serial'])
        return Response(status=status.HTTP_200_OK)
