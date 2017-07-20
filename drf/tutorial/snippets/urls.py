from django.conf.urls import url, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view(actions={
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view(actions={
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view(actions={
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view(actions={
    'get': 'list'
})

user_detail = UserViewSet.as_view(actions={
    'get': 'retrieve'
})



urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^all/', snippet_list, name='snippet-list'),
    url(r'^(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    url(r'^(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
])

#urlpatterns = format_suffix_patterns(urlpatterns)