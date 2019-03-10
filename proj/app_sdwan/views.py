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


def routerping(request):

    # router_ip = '45.251.109.168'
    # username = 'azhe'
    # password = 'sdlnet'
    router_port = 8728

    form = forms.ClassForm_Router_pingresult()

    if request.method == 'POST':
        form = forms.ClassForm_Router_pingresult(request.POST)

        if form.is_valid():
            #do something here
            ping_result = routeros_func.RouterPing( router_ip = form.cleaned_data["mgtIP"],
                                                    router_user = form.cleaned_data["username"],
                                                    router_pass = form.cleaned_data["password"],
                                                    dst_ip = form.cleaned_data["destinationIP"],
                                                    router_port = router_port,
                                                    )
            pingsourceIP = form.cleaned_data["mgtIP"]
            pingdestinationIP = form.cleaned_data["destinationIP"]
            ping_avg_rtd = ping_result['success']['rtt_avg']

            return render(request,'app_sdwan/routerping.html',{'pingsourceIP':pingsourceIP,
                                                               'pingdestinationIP':pingdestinationIP,
                                                               'ping_avg_rtd':ping_avg_rtd,
                                                               'form':form})
        else:
            print("the router ping form is not valid")

    return render(request,'app_sdwan/routerping.html',{'form':form})

def routerinterface(request):

    # router_ip = '45.251.109.168'
    # username = 'azhe'
    # password = 'sdlnet'
    router_port = 8728

    form = forms.ClassForm_Router_Interface()

    if request.method == 'POST':
        form = forms.ClassForm_Router_Interface(request.POST)

        if form.is_valid():
            #do something here
            Interface_result = routeros_func.RouterOs_Query( cmd = 'interface',
                                                    router_ip = form.cleaned_data["mgtIP"],
                                                    username = form.cleaned_data["username"],
                                                    password = form.cleaned_data["password"],
                                                    )
            print(Interface_result)

            # for interface in Interface_result:
            #     ClassModel_Router_Interface.objects.get_or_create(interface_id = interface['id'],
            #                                                     name=interface['name'],
            #                                                     type = interface['type'],
            #                                                     rx_byte = interface['rx-byte'],
            #                                                     tx_byte = interface['tx-byte'],
            #                                                     )
            # interfacelist = ClassModel_Router_Interface.objects.order_by('name')
            for interface in Interface_result:
                interface['rx_byte'] = interface.pop('rx-byte')
                interface['tx_byte'] = interface.pop('tx-byte')

            interfacelist_dict = {'interfacelist':Interface_result}
            return render(request,'app_sdwan/routerinterface.html',interfacelist_dict)
        else:
            print("the router ping form is not valid")

    return render(request,'app_sdwan/routerinterface.html',{'form':form})
