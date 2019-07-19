from django import forms
from .models import Answer, Question, Category
from django.core.files.images import get_image_dimensions


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('answer',)
        
class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'description', 'category',)

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name',)
