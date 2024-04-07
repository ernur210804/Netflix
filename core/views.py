from django.shortcuts import render
from django.http import JsonResponse

def add_to_list(request):
    # Your view logic to add the item to the list goes here
    # For example, you can process the POST data and add the item to the database

    # Dummy response for demonstration
    response_data = {'message': 'Item added to list successfully.'}
    return JsonResponse(response_data)

def index(request):
    return render(request, 'index.html')
