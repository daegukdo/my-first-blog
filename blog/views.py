from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def COVID19_map_data(request):
    return render(request, 'blog/COVID19/COVID_19_in_South_Korea_200317.html', {})