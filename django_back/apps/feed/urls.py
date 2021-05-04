from django.urls import path
from .views import return_feed_view, retrieve_news_view

urlpatterns = [
    path('', return_feed_view, name='ReturnFeedView'),
    path('/news', retrieve_news_view, name = 'RetrieveNewsView')
]
