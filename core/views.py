from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views import generic
from core.models import Question, Category, Favorite, Answer
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User  # Blog author or commenter
from django.core.mail import send_mail
from django.http import HttpResponse


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
            send_mail(
                'A user answered your question',
                'A user posted an answer to your question on http://www.stack-otterflow.herokuapp.com/',
                'answers@stack-otterflow.com',
                [f'{request.user.email}'],
                fail_silently=False,
            )
            return redirect('question-detail', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'core/answer_form.html', {'form': form})


@login_required
def add_new_question(request):
    from core.forms import QuestionForm
    from django.views.generic.edit import CreateView
    # question = get_object_or_404(Question)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.owner = request.user
            question.post = Question
            form.save()
            return redirect('question-list')
    else:
        form = QuestionForm()
    return render(request, 'core/question_form.html', {'form': form})


@login_required
def add_new_category(request):
    from core.forms import CategoryForm
    from django.views.generic.edit import CreateView
    # question = get_object_or_404(Question)
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            form.save()
            return redirect('add_new_question')
    else:
        form = CategoryForm()
    return render(request, 'core/category_form.html', {'form': form})


class UserProfileView(generic.ListView):
    model = Question
    template_name = 'core/profile.html'

    def get_queryset(self):
        """
        Return list of Question objects created by User (owner id specified in URL)
        """
        id = self.kwargs['pk']
        target_owner = get_object_or_404(User, pk=id)
        return Question.objects.filter(owner=target_owner)

    def get_context_data(self, **kwargs):
        """
        Add question owner to context so they can be displayed in the template
        """
        # Call the base implementation first to get a context
        context = super(UserProfileView, self).get_context_data(**kwargs)
        # Get the owner object from the "pk" URL parameter and add it to the context
        context['user'] = get_object_or_404(User, pk=self.kwargs['pk'])
        return context


def sendmail(request):
    send_mail(
        'A user answered your question',
        'A user posted an answer to your question on http://www.stack-otterflow.herokuapp.com/',
        'answers@stack-otterflow.com',
        ['kyle.heidelberger@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse('Mail successfully sent')
