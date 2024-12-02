from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        
    return render(request,'index.html')
# Create your views here.
