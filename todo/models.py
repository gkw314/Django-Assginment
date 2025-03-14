from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('제목',max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField('작성일자',auto_now_add=True)
    updated_at = models.DateTimeField('수정일자',auto_now=True)

    def __str__(self):
        return self.title