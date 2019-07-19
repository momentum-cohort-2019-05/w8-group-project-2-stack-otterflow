from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views import generic
from core.models import Question, Category, Favorite, Answer, OtterProfile
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import OtterProfileForm
from django.views.generic import CreateView


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_questions = Question.objects.all().count()
    recent_questions_list = Question.objects.all()[0:5]
    all_cats = Category.objects.all()

    context = {
        'num_questions': num_questions,
        'recent_questions_list': recent_questions_list,
        'all_cats': all_cats,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class QuestionListView(generic.ListView):
    model = Question


class QuestionDetailListView(generic.DetailView):
    model = Question


class CategoryListView(generic.ListView):
    model = Category


class CategoryDetailView(generic.DetailView):
    model = Category


class OtterProfileDetailView(generic.DetailView):
    model = OtterProfile
    


@login_required
def user_favorites(request):
    favorites = Favorite.objects.filter(favorited_by=request.user)

    favorites_list = []

    for favorite in favorites:
        favorites_list.append(favorite.question)

    context = {
        'favorites': favorites,
        'favorites_list': favorites_list,
    }

    return render(request, 'core/added_favorites.html', context)


@login_required
def add_to_favorites(request, pk):
    question = get_object_or_404(Question, pk=pk)

    new_favorite, created = Favorite.objects.get_or_create(
        question=question, favorited_by=request.user)
    if not created:
        new_favorite.delete()

    context = {
        'question': question,
        'new_favorite': new_favorite,
        'created': created,
    }

    return render(request, 'core/favorite_added.html', context)
    
# class CreateProfileView(CreateView):
#     model = OtterProfile
#     form_class = OtterProfileForm
#     template_name = 'core/profile.html'
#     success_url = reverse_lazy('otter-profile')

@login_required 
def add_answer_to_question(request, pk):
    from core.forms import AnswerForm
    from django.views.generic.edit import CreateView
    answer = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.target_question = get_object_or_404(Question, pk=pk)
            form.save()
            return redirect('question-detail', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'core/answer_form.html', {'form': form})

from django.contrib import messages

@login_required
def create_profile(request, pk):
    otterprofile = get_object_or_404(OtterProfile, id=pk)

    if otterprofile.user != request.user:
        messages.warning(
            request, "You cannot edit this profile! This is not your profile!")
        return redirect('/')

    if request.method == 'POST':
        form = OtterProfileForm(request.POST)
        if form.is_valid():
            otterprofile.user = request.user
            otterprofile.bio = form.cleaned_data['bio']
            # otterprofile.avatar = form.cleaned_data['avatar']
            otterprofile.save()
            return redirect('index')
    else:
        form = OtterProfileForm()
    return render(request, 'core/profile.html', {'form': form})
