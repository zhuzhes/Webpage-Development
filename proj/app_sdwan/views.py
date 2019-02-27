from django.shortcuts import render
from app_sdwan.models import Class_Model_Model1
from app_sdwan import forms
from app_sdwan import routeros_func


# Create your views here.
def index(request):
    return render(request,'app_sdwan/index.html')

def routeradding(request):
    # routeros_func.Router1()
    form = forms.ClassForm_Router_Register()
    if request.method == 'POST':
        form = forms.ClassForm_Router_Register(request.POST)

        if form.is_valid():
            #do something here
            print ("validation success")
            print("routerIP: " + form.cleaned_data["routerip"])
            print("Username: " + form.cleaned_data["username"])
            print("Password: " + form.cleaned_data["password"])
            routeros_func.Router1(router_ip=form.cleaned_data["routerip"],
                                  username=form.cleaned_data["username"],
                                  password=form.cleaned_data["password"])
            print("Router informanation fetched")
            return render(request,'app_sdwan/devicestatus.html')

    return render(request,'app_sdwan/routeradding.html',{'form':form})



def devicestatus(request):
    devicestatus = Class_Model_Model1.objects.order_by('router_name')
    devicestatus_dict = {'device_status':devicestatus}
    return render(request,'app_sdwan/devicestatus.html',devicestatus_dict)
