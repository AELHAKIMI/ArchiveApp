from django.conf.urls import url
from . import views

urlpatterns = [
    #/archive/
    url(r'^$', views.IndexView.as_view(), name='index'),
    #/archive/Patient/229/
    url(r'^Patient/(?P<pk>[0-9]+)/$', views.PatientDetailView.as_view(), name="detail-Patient"),
    #/archive/Patient/add/
    url(r'^Patient/add/$', views.PatientCreateView.as_view(), name='Patient-add'),
    #/archive/Dossier/add/
    url(r'^Dossier/add/$', views.DossierCreateView.as_view(), name='Dossier-add'),
    #/archive/Dossier/229
    url(r'^Dossier/(?P<pk>[0-9]+)/$', views.DossierDetailView.as_view(), name="detail-dossier"),
    #/archive/service/325
    url(r'^Service/(?P<pk>[\d]+)/$', views.ServiceDetailView.as_view(), name="detail-service"),
    #/archive/Service/add/
    url(r'^Service/add/$', views.ServiceCreateView.as_view(), name='Service-add'),

]
