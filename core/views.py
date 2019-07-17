from django.shortcuts import render
from django.views import generic
from core.models import Question, Category, Favorite, Answer, OtterProfile

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_questions = Question.objects.all().count()
    recent_questions_list = Question.objects.all()[0:5]

    context = {
        'num_questions': num_questions,
        'recent_questions_list': recent_questions_list,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class CategoryListView(generic.ListView):
    model = Category

class CategoryDetailView(generic.DetailView):
    model = Category
    
class OtterProfileDetailView(generic.DetailView):
    model = OtterProfile
