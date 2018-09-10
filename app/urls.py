from django.conf.urls import url
from . import views

urlpatterns = [
    #/archive/                                      INDEX
    url(r'^$', views.IndexView.as_view(), name='index'),

    ################################################ Patient Urls ####################################
    #/archive/Patient/229/                          DETAIL
    url(r'^Patient/(?P<pk>[0-9]+)/$', views.PatientDetailView.as_view(), name="detail-Patient"),
    #/archive/Patient/add/                          ADD
    url(r'^Patient/add/$', views.PatientCreateView.as_view(), name='Patient-add'),
    #/archive/Patient/update/229/                   UPDATE
    url(r'^Patient/update/(?P<pk>[0-9]+)/$', views.PatientUpdateView.as_view(), name="update-Patient"),
    #/archive/Patient/229/delete                    DELETE
    url(r'^Patient/(?P<pk>[0-9]+)/delete/$', views.PatientDeleteView.as_view(), name="delete-Patient"),
    ################################################ Dossier Urls ####################################
    #/archive/Dossier/229                           DETAIL
    url(r'^Dossier/(?P<pk>[0-9]+)/$', views.DossierDetailView.as_view(), name="detail-dossier"),
    #/archive/Dossier/add/                          ADD
    url(r'^Dossier/add/$', views.DossierCreateView.as_view(), name='Dossier-add'),
    #/archive/Dossier/229                           UPDATE
    url(r'^Dossier/update/(?P<pk>[0-9]+)/$', views.DossierUpdateView.as_view(), name="update-dossier"),
    #/archive/Dossier/229                           DELETE
    url(r'^Dossier/(?P<pk>[0-9]+)/delete/$', views.DossierDeleteView.as_view(), name="delete-dossier"),

    ###############################################  Document Urls ###################################
    url(r'^Dossier/Document/add/$', views.DossierDocumentAddView.as_view(), name='Document-add'),
    url(r'^Dossier/Document/(?P<pk>[0-9]+)/$', views.DossierDocumentDetailView.as_view(), name="detail-document"),
    ################################################ Service Urls ####################################
    #/archive/Service/add/
    url(r'^Service/add/$', views.ServiceCreateView.as_view(), name='Service-add'),
    #/archive/service/325
    url(r'^Service/(?P<pk>[\d]+)/$', views.ServiceDetailView.as_view(), name="detail-service"),
]
