from rest_framework import serializers
from myapi.models import DocAttach, Document

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        
class DocAttachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DocAttach
        fields = '__all__'