from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Bebidas, Estabelecimento, Cesta, Item
from core.serializers import BebidasSerializer, EstabelecimentoSerializer, CestaSerializer, ItemSerializer, UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BebidasViewSet(viewsets.ModelViewSet):
    queryset = Bebidas.objects.all()
    serializer_class = BebidasSerializer

class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer

class CestaViewSet(viewsets.ModelViewSet):
    queryset = Cesta.objects.all()
    serializer_class = CestaSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

