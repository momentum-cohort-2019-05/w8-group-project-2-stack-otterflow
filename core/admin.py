from django.contrib import admin
from .models import Question, Category, Favorite, Answer

# Register your models here.
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Answer)