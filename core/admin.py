from django.contrib import admin
from .models import Question, Category, Favorite, Answer, OtterProfile

# Register your models here.
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Answer)
admin.site.register(OtterProfile)