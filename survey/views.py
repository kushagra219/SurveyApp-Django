from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def thankyou(request):
    return render(request, 'survey/thankyou.html')


