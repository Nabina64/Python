from django.db import models

# Create your models here.
# TABLE: NOTE
# FIELDS: Id,Title,Content,Program(Science,Commerce,Arts),Created_At,Updated_At

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    program = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# models.py file create models -> migration file: contains the state of models.py file(python manage.py makemigrations) -> database reflect(python manage.py migrate)