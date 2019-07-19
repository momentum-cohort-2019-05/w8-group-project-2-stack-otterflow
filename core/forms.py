from django import forms
from .models import OtterProfile, Answer
from django.core.files.images import get_image_dimensions


class OtterProfileForm(forms.ModelForm):
    class Meta:
        model = OtterProfile
        fields = ['bio']

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('answer',)

