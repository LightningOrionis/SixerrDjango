from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def gig_detail_page(request, pk):
    return render(request, 'gig_detail.html')
