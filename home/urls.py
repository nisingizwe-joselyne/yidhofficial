from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
                                                         
urlpatterns=[
    path('',views.welcome, name='smart'),
    path('about-us',views.about, name='about'),
    # path('home',views.home, name='home'),
    # path('digital-ikigega',views.Ikigega, name='ikigega'),
    # path('digitalapp',views.digitalapp, name='digital'),
    # path('registration/', views.registration, name='register'),
    # path('<int:id>deleteInfos', views.delreg, name='deleteInfos'),
    # path('<int:id>updateInfos', views.updatereg, name='updateInfos'),
    path('reg/endpoint', views.registerEndpoint, name='farmendpoint'),
    path('coop/endpoint', views.CooperativeEndpoint, name='endpoint'),
    path('rec/endpoint', views.RecordEndpoint, name='recordendpoint'),
    # path('deleteEndpoints/<int:id>', views.deleteEndpoint, name='deleteEndpoints'),
    # path('user-creation/', CustomAuthToken.as_view())
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)