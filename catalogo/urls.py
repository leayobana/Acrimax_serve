
from django.conf.urls import url, include
from rest_framework import routers
from .views import ProductoViewSet, VentaViewSet, CategoriaViewSet, UnidadMedViewSet, ClienteViewSet, ShoppingCartViewSet

router = routers.DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'unidadMed', UnidadMedViewSet)
router.register(r'producto', ProductoViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'venta', VentaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
