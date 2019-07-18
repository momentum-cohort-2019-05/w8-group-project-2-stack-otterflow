from django.shortcuts import render

# Create your views here.
from core.models import Question, Category, Favorite, Answer

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_questions = Question.objects.all().count()

    
    context = {
        'num_questions': num_questions,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)




from django.views import generic

class QuestionListView(generic.ListView):
    model = Question

class QuestionDetailListView(generic.DetailView):
    model = Question
