from rest_framework.routers import DefaultRouter
from .views import NutricionistaViewSet

router = DefaultRouter()
router.register(r'clientes', NutricionistaViewSet)# Registra a viewset NutricionistaViewSet com a rota 'clientes'

urlpatterns = router.urls