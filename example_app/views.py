from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response



# Create your views here.

def hello(request):
    return HttpResponse("Hello Django World!")

@api_view(['GET'])
@permission_classes([AllowAny])
def hello_rest_api(request):
    data = {'message':'Hello, REST Api'}
    return Response(data)

