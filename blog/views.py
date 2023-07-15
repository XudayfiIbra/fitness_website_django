from django.shortcuts import render


# Home page
def homePage(request):
    return render(request, 'blog/index.html')