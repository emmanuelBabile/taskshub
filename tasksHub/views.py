# taskhub/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to TaskHub API </h1>"
                        "<p>To access the projects section, <a href='/api/projects/'> click here </a></p>"
                        "<p>To access the tasks section, <a href='/api/tasks/'> click here </a></p>"
                        "<p>To access the comments section, <a href='/api/comments/'> click here </a></p>"
    )
