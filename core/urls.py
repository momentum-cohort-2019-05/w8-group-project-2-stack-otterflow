from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]


urlpatterns += [
    path('questions/', views.QuestionListView.as_view(), name='question-list'),
    path('questions/<int:pk>', views.QuestionDetailListView.as_view(), name='question-detail'),
]