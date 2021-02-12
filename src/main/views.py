from django.shortcuts import render
from django.http import JsonResponse # this allows you to return the data instead of text

# third party imports
from rest_framework.response import Response
#this inherits from the jsonResponse built in with python 
from rest_framework.views import APIView 
# this is a wrapper in django rest framework that allows users to accept get or post request

class TestView(APIView):
    def get(self, request, *args, **kwargs): #args and kwargs are used for passing multiple parameters 
        data = {
            'name': 'john',
            'age': 23,
        } #json payload 
        return Response(data)




# Create your views here.
# def test_view(request):
#     data = {
#         'name': 'isaac',
#         'age': 23,
#     } # json payload 
#     return JsonResponse(data)
