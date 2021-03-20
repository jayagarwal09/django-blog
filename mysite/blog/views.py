from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):
	posts = Post.objects.all().order_by('title')
	return render(request, 'blog/post_list.html',{'posts':posts})