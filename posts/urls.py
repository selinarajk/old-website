'''Defines url patterns for posts'''

from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    # All blog posts
    path('blog/', views.blog, name='blog'),
    # Detail page for a single blog post
    path('blog/<int:post_id>/', views.post, name='post'),
    # Now page
    path('now/', views.now, name='now'),
    # Colophon
    path('colophon/', views.colophon, name='colophon'),
    # discover page
    path('discover/', views.discover, name='discover'),
    # depths page
    path('depths/', views.depths, name='depths'),
    # lands page
    path('lands/', views.lands, name='lands'),
    # skies page
    path('skies/', views.skies, name='skies'),
    # About page
    path('about/', views.about, name='about'),
    # Projects page
    path('projects/', views.projects, name='projects'),
    # Favourites page
    path('favourites/', views.favourites, name='favourites'),
    # Others' Work page
    path('otherswork/', views.otherswork, name='otherswork'),
    # Code page
    path('code/', views.code, name='code'),
    # Treat page
    path('treat/', views.treat, name='treat'),
]
