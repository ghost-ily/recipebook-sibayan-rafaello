from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('test')
    
def recipe_list(request):
    return render(request, 'recipe_list.html', {'name': "Leo"})
    