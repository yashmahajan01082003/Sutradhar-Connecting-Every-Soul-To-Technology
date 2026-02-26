from django.urls import path
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('openParti', views.openParti, name='openParti'),
    path('openPartiSpec/<str:fName>', views.openPartiSpec, name='openPartiSpec'),
    path('openPartiSpec2/<str:fName0>/<str:fName1>/', views.openPartiSpec2, name='openPartiSpec2'),
    path('newD', views.newD, name='newD'),
    path('newD2/<str:fName0>/', views.newD2, name='newD2'),
    path('gesturePage', views.gesturePage, name='gesturePage'),
    path('pres', views.pres, name='pres'),
    path('execPresentation/<str:Fname>/',views.execPresentation,name='execPresentation'),
    path('activateVM', views.activateVM, name='activateVM'),
    path('activateRM', views.activateRM, name='activateRM'),
    path('speciallyabled', views.speciallyabled, name='speciallyabled'),
    path('execHandTab', views.execHandTab, name='execHandTab'),
    path('execBrightnessControl', views.execBrightnessControl, name='execBrightnessControl'),
    path('execFaceDistance', views.execFaceDistance, name='execFaceDistance'),
    path('eyeBasedFeat', views.eyeBasedFeat, name='eyeBasedFeat'),
    path('assis', views.frontEndForJarvis, name='assis'),
    path('voiceFeat', views.voiceFeat, name='voiceFeat'),
    path('runJarvis', views.runJarvis, name='runJarvis'),
    path("chatbot", views.chatbot, name="chatbot"),
    path("chat/", views.chat_with_gemini, name="chat"),
    path('faceFeat', views.faceFeat, name='faceFeat'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)