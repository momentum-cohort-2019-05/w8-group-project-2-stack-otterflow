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
]

urlpatterns += [
    path('profile/', login_required(views.CreateProfileView.as_view()), name='create-profile'),
]