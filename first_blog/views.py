from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'Josh',
        'title': 'Blog Post 1',
        'content': 'First Blog post',
        'date_posted': 'January 18, 2018'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second Blog post',
        'date_posted': 'January 22, 2018'
    },
    {
        'author': 'Sophie',
        'title': 'Blog Post 3',
        'content': 'How to make spicy food!',
        'date_posted': 'January 22, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'first_blog/home.html', context)

def about(request):
    return render(request, 'first_blog/about.html', {'title': 'About'})