from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    path('otter/<int:pk>', views.OtterProfileDetailView.as_view(), name='otter-profile'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(),
         name='category-detail'),
]