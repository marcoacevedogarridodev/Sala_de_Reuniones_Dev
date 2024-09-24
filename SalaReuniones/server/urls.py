from django.urls import path, include
from rest_framework.routers import DefaultRouter
from server.api.sala import SalaViewSet
from server.api.reuniones import ReunionesViewSet
from server.api.asignacion import AsignacionViewSet

router = DefaultRouter()
router.register(r'salas', SalaViewSet)
router.register(r'reuniones', ReunionesViewSet)
router.register(r'asignaciones', AsignacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]