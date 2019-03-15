from django.conf.urls import url, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'bebidas', views.BebidasViewSet)
router.register(r'estabelecimento', views.EstabelecimentoViewSet)
router.register(r'cestas', views.CestaViewSet)
router.register(r'item', views.ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

