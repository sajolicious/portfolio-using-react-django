from django.shortcuts import render
from rest_framework import viewsets
from .models import blog,contact
from .serializers import BlogSerializers,ContactSerializers
# Create your views here.
class blogView(viewsets.ModelViewSet):
    queryset=blog.objects.all()
    serializer_class=BlogSerializers

class ContactView(viewsets.ModelViewSet):
    queryset=contact.objects.all()
    serializer_class=ContactSerializers