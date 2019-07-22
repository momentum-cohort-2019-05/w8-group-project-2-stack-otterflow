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
    path('user/<int:pk>', views.UserProfileView.as_view(), name='user-profile'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(),name='category-detail'),
    path('favorites/', views.user_favorites, name='user-favorites'),
    path('favorite_added/<int:pk>', views.add_to_favorites, name='favorites'),
    path('answer/<int:pk>/answer/', views.add_answer_to_question, name='add_answer_to_question'),
    path('question/', views.add_new_question, name='add_new_question'),
    path('category/', views.add_new_category, name='add_new_category'),
    path('favorite/', views.add_favorite, name='add_new_favorite'),
    # path('answer/add/', views.add_answer, name='add_answer'),
    # path('ajax_is_favorite/', views.ajax_is_favorite, name='ajax_is_favorite'),
]

urlpatterns += [
        path('sendmail', views.sendmail, name='sendmail'),
]