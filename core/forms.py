from django import forms
from .models import Answer, Question
from django.core.files.images import get_image_dimensions


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('answer',)
        
class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'description', 'category',)

