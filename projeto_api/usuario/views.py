from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from .models import Modalidade, Usuario
from .serializers import ModalidadeSerializer, UsuarioSerializer
class ModalidadeList(generics.ListCreateAPIView):
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer

class ModalidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer
class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    parser_classes = (MultiPartParser, FormParser)
class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    parser_classes = (MultiPartParser, FormParser)