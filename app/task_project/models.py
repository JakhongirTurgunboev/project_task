from django.db import models


class Project(models.Model):
    customer_id = models.PositiveIntegerField()
    address = models.TextField()
    customer_inn = models.CharField(max_length=20)
    project_sum = models.FloatField(default=0)
    paid_sum = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def status(self):
        if (self.paid_sum / self.project_sum)*100 == 100:
            return "To'landi"
        elif (self.paid_sum / self.project_sum)*100 < 50:
            return "Boshlanmagan"
        elif (self.paid_sum / self.project_sum)*100 > 50:
            return "Yopilish arafasida"


class Task(models.Model):
    task_name = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_id = models.OneToOneField(Project, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.task_name}'

