from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def bd_list(request):
    if request.method == 'GET':
        return HttpResponse('Привет! Это ПЕРВЫЙ микросервис!')
