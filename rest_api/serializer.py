from rest_framework import serializers
from album.models import Album, Size, Binding, Template


class AlbumSerializer(serializers.ModelSerializer):
    
     class Meta:
        model = Album
        fields = ['id', 'title', 'size', 'binding', 'template', 'description', 'pages', ]


class SizeSerializer(serializers.ModelSerializer):

     class Meta:
         model = Size
         fields = ['id', 'size']


class BindingSerializer(serializers.ModelSerializer):

      class Meta:
        model = Binding
        fields = ['id', 'binding']
    

class TemplateSerializer(serializers.ModelSerializer):
     class Meta:
         model = Template
         fields = ['id', 'template']
       