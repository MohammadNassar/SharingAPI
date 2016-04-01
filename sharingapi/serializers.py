
# Underneath I am importing the models/classes that I have created in the 'models.py' file, as well as importing 'serializers' from the 'rest_framework'
from sharingapi.models import SharedItem, Item, Location, User
from rest_framework import serializers

# Defining the fields in the SharedItem model
class SharedItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SharedItem
        fields = ('id', 'trade_type', 'trade_status', 'timestamp', 'item_id', 'location_id', 'user_id')

# Defining the fields in the ItemSerializer model
class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'category', 'description')

# Defining the fields in the LocationSerializer model
class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'address', 'lat', 'lng')

# Defining the fields in the UserSerializer model
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'firstname', 'surname', 'email', 'phone', 'password')
