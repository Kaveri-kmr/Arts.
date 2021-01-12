"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from arts.views import eventdetails
from arts.views import registration_details,list_of_participants
from django.conf.urls.static import static
from .settings import STATIC_ROOT, STATIC_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('eventdetails/',eventdetails,name="eventdetails"),
    path('',registration_details,name='registration_details'),
    path('list/', list_of_participants,name='list_of_participants')
    # path('list/ind',individual,name='individual')
] + static(STATIC_URL, document_root=STATIC_ROOT)
