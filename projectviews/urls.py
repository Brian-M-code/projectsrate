from django.conf.urls.static import static
from django.conf.urls import url,include
from .views import PostListView,PostDetailView, PostCreateView,PostUpdateView
from . import views


urlpatterns = [
    url('',  PostListView.as_view(), name='projects-index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^api/projects/$', views.ProjectsList.as_view()),
    url(r'^post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url(r'^profile/details/<str:username>/',views.display_profile, name = 'profile-detail'),
    url(r'^post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
]