from django.conf.urls.static import static
from django.conf.urls import url,include
from .views import PostListView,PostDetailView
from . import views


urlpatterns = [
    url('',  PostListView.as_view(), name='projects-index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^api/projects/$', views.ProjectsList.as_view()),
]