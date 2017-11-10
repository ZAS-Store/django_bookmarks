from django.shortcuts import render

# Create your views here.
from django http import HttpResponse
def main_page(request):
    output= '''
    <html>
    <head><tittle>%s</tittle></head>
    <body>
    <h1>%s,/h1><p>%s</p>
    </body>
    </html>
    '''%(
        'Django bookmarks'
        'Welcome to quickmark',
        ' Here you can store and share bookmarks!'
        )
    return HttpResponse (output)
