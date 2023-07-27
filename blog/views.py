from django.shortcuts import render
from . models import Category, Post
# Home page
def homePage(request):
    featuredPosts = Post.objects.order_by('-id')[:3]
    context = {
        'featuredPosts': featuredPosts
    }
    return render(request, 'blog/index.html', context)


# Category view
def CategoryViewList(request):
    cat = Category.objects.order_by('-id')
    context = {
        'categories': cat
    }
    return render(request, 'blog/category.html', context)
