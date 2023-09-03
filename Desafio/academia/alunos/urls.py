from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet

router = DefaultRouter()

# Registra a viewset AlunoViewSet com a rota 'alunos'
router.register(r'alunos', AlunoViewSet)

urlpatterns = router.urls