from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name='index'),
]


urlpatterns += [
    path('questions/', views.QuestionListView.as_view(), name='question-list'),
    path('questions/<int:pk>', views.QuestionDetailListView.as_view(), name='question-detail'),
]

urlpatterns += [
    path('otter/<int:pk>', views.OtterProfileDetailView.as_view(), name='otter-profile'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(),name='category-detail'),
    path('favorites/', views.user_favorites, name='user-favorites'),
    path('favorite_added/<int:pk>', views.add_to_favorites, name='favorites'),
    path('answer/<int:pk>/answer/', views.add_answer_to_question, name='add_answer_to_question'),
    path('question/', views.add_new_question, name='add_new_question'),
]

urlpatterns += [
    path('otter/<int:pk>/profile/', views.create_profile, name='create-profile'),
]