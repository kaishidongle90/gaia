from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import GaiaUser
def index(request):
    user = request.POST.get('user')
    passwd = request.POST.get('passwd')
    print(user,passwd)
    gu = GaiaUser.objects.create(name=user,ip=passwd)
    gu.save()
    return  render(request, 'index.html')