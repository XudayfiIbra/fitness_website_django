from django.shortcuts import render
from . models import Category
# Home page
def homePage(request):
    return render(request, 'blog/index.html')


# Category view
def CategoryViewList(request):
    cat = Category.objects.order_by('-id')
    context = {
        'categories': cat
    }
    return render(request, 'blog/category.html', context)
