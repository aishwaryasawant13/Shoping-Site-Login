from django.shortcuts import render

# Create your views here.
def w1(request):
    return render(request,'html/page.html')
def success_views(request):
    return render(request,'html/success.html')
def reg_views(request):
    return render(request,'html/register.html')
def final_views(request):
    return render(request,'html/final.html')
def login_views(request):
    return render(request,'html/page.html')
def save_views(request):
    print("...................................heloooo")
    name=request.GET['fname']
    age=request.GET['fage']
    no=request.GET['fno']
    email=request.GET['fid']
    dict= {
        'name':name,'age':age,'no':no,'mail':email
    }
    return render(request,'html/success.html',context=dict)
