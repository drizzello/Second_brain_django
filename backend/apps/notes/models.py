from django.db import models
from backend.apps.common.models import BaseModel
from backend.apps.accounts.models import User

class Tags(models.TextChoices):
    STUDY = "STUDY", "Study"
    PERSONAL = "PERSONAL", "Personal"
    WORK = "WORK", "Work"

class Note(BaseModel):
    title = models.CharField()
    content = models.TextField(blank=True)
    tag = models.CharField(max_length=20, choices=Tags.choices)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    def __str__(self):
        return self.title