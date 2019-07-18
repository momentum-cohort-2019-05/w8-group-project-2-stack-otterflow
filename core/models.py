from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver




class Question(models.Model):
    title = models.CharField(max_length=200, help_text='Enter a question here')
    description = models.TextField(
        max_length=5000, help_text='Type your question description here')
    date_posted = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('OtterProfile', on_delete=models.CASCADE)
    times_favorited = models.PositiveIntegerField(
        default=0, help_text='Enter the number of times this question has been favorited')
    category = models.ManyToManyField(
        "Category", help_text='Enter the category for this question')

    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Category(models.Model):
    name = models.CharField(
        max_length=100, help_text="Chose a category for your question.")

    def get_absolute_url(self):
        """
        A function to return a link to category's unique page.
        """
        return reverse('category-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']

    def __str__(self):
        """ Returns the category name as a string. """
        return self.name


class Favorite(models.Model):
    favorited_by = models.ForeignKey(User, default=1, unique=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    date_favorited = models.DateField(auto_now_add=True, verbose_name="Date Favorited")

    class Meta:
        ordering = ['-date_favorited']

    def __str__(self):
        return f"{self.favorited_by} | {self.question}"


class Answer(models.Model):
    """Model representing an answer."""
    answer = models.TextField(max_length=200, help_text='Enter a comment here')
    date_posted = models.DateTimeField(auto_now_add=True)
    target_question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             default=1, on_delete=models.CASCADE)
    approved_answer = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_posted']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        """String for representing the Model object."""
        return self.answer


class OtterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True,
                           help_text='Tell us a bit about yourself!')
    avatar = models.ImageField(upload_to='images/')

    def __str__(self):
        """
        String for representing the user.
        """
        return self.user.username

    def get_absolute_url(self):
        """
        Returns the url to access a particular user's profile.
        """
        return reverse('otter-profile', args=[str(self.id)])

    class Meta:
        ordering = ['user', 'bio']

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        OtterProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.otterprofile.save()