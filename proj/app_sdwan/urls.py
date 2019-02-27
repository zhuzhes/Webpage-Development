from django.conf.urls import url
from app_sdwan import views

# SET THE NAMESPACE!
app_name = 'app_sdwan'

urlpatterns=[
    url(r'^routeradding/$',views.routeradding,name='routeradding'),
    url(r'^devicestatus/$',views.devicestatus,name='devicestatus'),
]
