"""jym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,re_path
from base_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.SuperAdmin_index, name='SuperAdmin_index'),
    re_path(r'^SuperAdmin_personal_trainer/$', views.SuperAdmin_personal_trainer, name='SuperAdmin_personal_trainer'),
    re_path(r'^SuperAdmin_active_trainers/$', views.SuperAdmin_active_trainers, name='SuperAdmin_active_trainers'),
    re_path(r'^SuperAdmin_resigned_trainers/$', views.SuperAdmin_resigned_trainers, name='SuperAdmin_resigned_trainers'),
    re_path(r'^SuperAdmin_activetrainer_update/$', views.SuperAdmin_activetrainer_update, name='SuperAdmin_activetrainer_update'),
    re_path(r'^SuperAdmin_resignedtrainer_update/$', views.SuperAdmin_resignedtrainer_update, name='SuperAdmin_resignedtrainer_update'),



    re_path(r'^User_index/$', views.User_index, name='User_index'),
    re_path(r'^User_payment_history/$', views.User_payment_history, name='User_payment_history'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
