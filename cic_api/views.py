from rest_framework import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({'message': 'Welcome to my Django Rest Framework cic API!!'})
