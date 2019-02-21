from django.conf.urls import url
from . import views

app_name = "blog"
urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail, name='post_detail'),
    url(r'^(?P<tag_id>[-\w]+)/$', views.post_list_by_tag,
        name='post_list_by_tag'),
    url(r'^$', views.post_list, name='post_list'),
]
