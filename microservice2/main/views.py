from http.client import HTTPResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def bd_list(request):
    if request.method == 'GET':
        return HTTPResponse('Ты пидорас')
