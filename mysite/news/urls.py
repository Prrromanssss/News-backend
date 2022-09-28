from django.urls import path
from .views import index, get_category, views_news

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', views_news, name='views_news')

    ]
