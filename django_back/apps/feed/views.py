from apps.feed.models import Site
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
import feedparser


class ReturnFeedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        queryset = Site.objects.filter(
            user_site_relation=request.user.id).values()
        return Response(data=queryset, status=200)

    def post(self, request, *args, **kwargs):
        if Site.objects.filter(name=request.data['name']).exists():
            return Response(status=400)
        else:
            if take_feed_from_url(request.data['site_url']):
            
                site = Site.objects.create(name=request.data['name'],site_url=request.data['site_url'],
                category=request.data['category'],)
                site.user_site_relation.add(request.user)
                return Response(status=201)
            else:
                return Response(status=404)



class RetrieveNewsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        feed_name = request.query_params.get('feed_name')
        obj = get_object_or_404(Site, name = feed_name)
        feed = take_feed_from_url(obj.site_url)
        return Response(data=feed, status=200)


def take_feed_from_url(feed_url):
    feed_list = []
    feed = feedparser.parse(
        feed_url)
    for article in feed['entries']:
        feed_list.append({
            "title": article['title'],
            "summary": article['summary'],
            "published": article['published'],
            "link": article['link'],
        })
    return feed_list


return_feed_view = ReturnFeedView.as_view()
retrieve_news_view = RetrieveNewsView.as_view()
