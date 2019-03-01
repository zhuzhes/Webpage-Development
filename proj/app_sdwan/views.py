from django.shortcuts import render
from app_sdwan.models import *
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
            form.save(commit=True)
            routeros_func.RouterBasicinfo(router_ip = form.cleaned_data["routerip"],
                                username = form.cleaned_data["username"],
                                password = form.cleaned_data["password"],
                                )
            return devicelist(request)
        else:
            print("the router register form is not valid")
            # original coding regarding update to database
            # print ("validation success")
            # print("routerIP: " + form.cleaned_data["routerip"])
            # print("Username: " + form.cleaned_data["username"])
            # print("Password: " + form.cleaned_data["password"])
            # routeros_func.Router1(router_ip=form.cleaned_data["routerip"],
            #                       username=form.cleaned_data["username"],
            #                       password=form.cleaned_data["password"])
            # print("Router informanation fetched")
            # return render(request,'app_sdwan/devicelist.html')

    return render(request,'app_sdwan/routeradding.html',{'form':form})

def routerdeleting(request):
    form = forms.ClassForm_Router_Delete()

    if request.method == 'POST':
        form = forms.ClassForm_Router_Delete(request.POST)

        if form.is_valid():
            print("routerIP: " + form.cleaned_data["routerip"])
            #do something here#
            ClassModel_Router_Register.objects.filter(routerip=form.cleaned_data["routerip"]).delete()
            ClassModel_Router_Basicinfo.objects.filter(mgtIP=form.cleaned_data["routerip"]).delete()
            #######
            return devicelist(request)
        else:
            print("the router register form is not valid")


    return render(request,'app_sdwan/routerdeleting.html',{'form':form})


def devicelist(request):
    devicelist = ClassModel_Router_Basicinfo.objects.order_by('router_name')
    devicelist_dict = {'device_status':devicelist}
    return render(request,'app_sdwan/devicelist.html',devicelist_dict)
