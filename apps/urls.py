from django.conf.urls import url, include


urlpatterns = [
    url(r'', include('apps.post.urls', namespace='post')),
]