from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

@api_view(['POST'])
def getBillAmount(request):
    data={'status':'OK'}
    return Response(status=status.HTTP_200_OK, data=data)
