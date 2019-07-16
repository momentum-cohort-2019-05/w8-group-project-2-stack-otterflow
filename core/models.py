from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a question here')
    description = models.TextField(max_length=5000, help_text='Type your question description here')
    date_posted = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 
    times_favorited = models.PositiveIntegerField(default=0, help_text='Enter the number of times this question has been favorited')
    category = models.ManyToManyField("Category", help_text='Enter the category for this question')

    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        pass

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Chose a category for your question.")

    def get_absolute_url(self):
        pass

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']

    def __str__(self):
        """ Returns the category name as a string. """
        return self.name
        
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    date_favorited = models.DateField(
        auto_now_add=True, verbose_name="Date Favorited")

    class Meta:
        ordering = ['-date_favorited']

    def __str__(self):
        return f"{self.user} | {self.question}"

class Answer(models.Model):
    """Model representing an answer."""
    answer = models.TextField(max_length=200, help_text='Enter a comment here')
    date_posted = models.DateTimeField(auto_now_add=True)
    target_question = models.ForeignKey('', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    approved_answer = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_posted']

    def approve(self):
        self.approved_comment = True
        self.save()


    def __str__(self):
        """String for representing the Model object."""
        return self.answer
