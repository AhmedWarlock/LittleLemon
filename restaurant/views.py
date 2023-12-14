from django.shortcuts import render
from rest_framework import generics
from .serializers import *

def index(request):
    return render(request, 'index.html', {})

class MenuItemView (generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()