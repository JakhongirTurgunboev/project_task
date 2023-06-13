from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet.as_view(), basename="task")
router.register(r'project', ProjectViewSet.as_view(), basename="task")

urlpatterns = router.urls
