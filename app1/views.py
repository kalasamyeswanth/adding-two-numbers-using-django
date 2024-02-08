from django.shortcuts import render

# Create your views here.
def happy(request):
    s={'a':'nenu','b':'after','c':'nenu'}
    return render(request,'honey.html',s)
def add(request):
    n1=int(request.GET["num1"])
    n2=int(request.GET['num2'])
    n3=n1+n2
    return render(request,'happy.html',{"result":n3})
