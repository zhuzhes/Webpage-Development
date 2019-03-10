from django.conf.urls import url
from app_sdwan import views

# SET THE NAMESPACE!
app_name = 'app_sdwan'

urlpatterns=[
    url(r'^routeradding/$',views.routeradding,name='routeradding'),
    url(r'^devicelist/$',views.devicelist,name='devicelist'),
    url(r'^routerdeleting/$',views.routerdeleting,name='routerdeleting'),
    url(r'^routerping/$',views.routerping,name='routerping'),
    url(r'^routerinterface/$',views.routerinterface,name='routerinterface'),

]
