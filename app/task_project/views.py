from rest_framework import viewsets, mixins
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework.response import Response


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Update the associated Task here
        task_instance = instance.task
        if task_instance:
            if instance.status == "To'landi":
                task_instance.status = True
                task_instance.save()

        return Response(serializer.data)

