from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
