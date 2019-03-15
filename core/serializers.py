# implementar o serializer
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Bebidas, Estabelecimento, Cesta, Item

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'id')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class BebidasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bebidas
        fields = ('id', 'fabricante', 'mililitros', 'estabelecimento', 'preco')

class EstabelecimentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ('id', 'nome', 'endereco')

class CestaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cesta
        fields = ('id', 'nome')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'id_cesta', 'id_bebida')