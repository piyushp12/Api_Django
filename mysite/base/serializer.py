from rest_framework import serializers


class studentserializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    cls = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    avatar = serializers.ImageField()
