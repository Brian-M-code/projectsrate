from django.conf.urls.static import static
from django.conf.urls import url,include
from .views import PostListView,PostDetailView, PostCreateView,PostUpdateView,PostDeleteView,ReviewCreateView
from . import views


urlpatterns = [
    url('',  PostListView.as_view(), name='projects-index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^api/projects/$', views.ProjectsList.as_view()),
    url(r'^post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url(r'^profile/details/<str:username>/',views.display_profile, name = 'profile-detail'),
    url(r'^post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    url(r'^post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
    url(r'^review/new/<int:pk>/', ReviewCreateView.as_view(), name='review-create'),
]