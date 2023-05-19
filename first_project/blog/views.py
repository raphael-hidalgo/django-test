from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        'author':'Raphaël',
        'title':'Django trial',
        'content':'first post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author':'Guilhem',
        'title':'JS Specialist',
        'content':'second post content',
        'date_posted': 'August 28, 2018'
    },
    {
        'author':'Stephanie',
        'title':'Architectural goodess',
        'content':'third post content',
        'date_posted': 'August 29, 2018'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title': "home"
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title': "about us <3"
    }
    return render(request, 'blog/about.html', context)
