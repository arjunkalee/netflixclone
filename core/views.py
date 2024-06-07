from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return  render(request, 'index.html')

def add_to_list(request):
    # Your implementation for adding the movie to the user's list
    # This view should handle the AJAX request and return a JSON response
    return JsonResponse({'message': 'Movie added to list.'})