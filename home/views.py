from django.shortcuts import render, HttpResponse
from .models import home,abou


# Create your views here.
def index(request):
    data = home.objects.all()
    hom= {
    "home_number": data
}
    return render(request, 'index.html',hom)
    # return HttpResponse("this is homepage")

def about(request):
    data = abou.objects.all()
    abo={
        "abou_number":data
    }
    return render(request, 'about.html',abo)


 