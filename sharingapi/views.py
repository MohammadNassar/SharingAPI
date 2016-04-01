# Importing the different models that I created in the 'models.py' file
from sharingapi.models import SharedItem, Item, Location, User
# Importing 'viewsets' fromm the 'rest_framework'
from rest_framework import viewsets
# Importing the serializers of the different models that I created in the 'serializers.py' file
from sharingapi.serializers import SharedItemSerializer, ItemSerializer, LocationSerializer, UserSerializer

# Below I created the views of my API, which are: SharedItemSet, ItemSet, LocationSet and UserSet

class SharedItemSet(viewsets.ModelViewSet):

    queryset = SharedItem.objects.all()
    serializer_class = SharedItemSerializer

class ItemSet(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class LocationSet(viewsets.ModelViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class UserSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    

    
