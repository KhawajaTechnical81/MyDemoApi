from django.shortcuts import render
from rest_framework import viewsets
from myapi.models import DocAttach, Document
from myapi.serializers import DocAttachSerializer, DocumentSerializer

# Create your views here.
class DocumentViewSet(viewsets.ModelViewSet):
    
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
class DocAttachViewSet(viewsets.ModelViewSet):
    
    queryset = DocAttach.objects.all()
    serializer_class = DocAttachSerializer