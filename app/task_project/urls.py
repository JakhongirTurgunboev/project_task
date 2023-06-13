from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, basename="task")
router.register(r'project', ProjectViewSet, basename="task")

urlpatterns = router.urls
