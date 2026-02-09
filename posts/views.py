from django.shortcuts import render

from .models import Post

# Create your views here.

def home(request):
    '''Home page'''
    return render(request, 'posts/home.html')

def blog(request):
    '''All blog posts'''
    posts = Post.objects.all()#.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'posts/blog.html', context)

def post(request, post_id):
    '''A single post'''
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'posts/post.html', context)

def now(request):
    '''Now page'''
    return render(request, 'posts/now.html')

def colophon(request):
    '''Colophon page'''
    return render(request, 'posts/colophon.html')

def discover(request):
    '''discover page'''
    return render(request, 'posts/discover.html')

def depths(request):
    '''depths page'''
    return render(request, 'posts/depths.html')

def lands(request):
    '''lands page'''
    return render(request, 'posts/lands.html')

def skies(request):
    '''skies page'''
    return render(request, 'posts/skies.html')

def about(request):
    '''about page'''
    return render(request, 'posts/about.html')

def projects(request):
    '''projects page'''
    return render(request, 'posts/projects.html')

def favourites(request):
    '''favourites page'''
    return render(request, 'posts/favourites.html')

def otherswork(request):
    '''others' work page'''
    return render(request, 'posts/otherswork.html')

def code(request):
    '''code page'''
    return render(request, 'posts/code.html')

def treat(request):
    '''treat page'''
    return render(request, 'posts/treat.html')
