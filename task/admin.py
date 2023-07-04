from django.contrib import admin
from .models import Board, Card, Task, Activity

# Register your models here.
admin.site.register(Board)
admin.site.register(Card)
admin.site.register(Task)
admin.site.register(Activity)

