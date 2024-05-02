from django.urls import path
from posts import views


urlpatterns = [
    path("",views.HomePageView.as_view(),name="home"),
    path("about/",views.AboutPageView.as_view(),name="about"),
    path("posts/list/",views.PostListView.as_view(),name="list"),
    path("posts/<int:pk>/",views.PostDetailView.as_view(),name="detail"),
    path('posts/new/',views.PostCreateView.as_view(),name='new'),
]