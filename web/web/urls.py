"""GYM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from gym import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('adreg/', views.adminreg, name='adminreg'),
    path('adlog/', views.adminlog, name='adminlog'),
    path('class/', views.classy, name='class'),
    path('contact/', views.contact, name='contact'),
    path('detail/', views.detail, name='detail'),
    path('', views.index, name='index'),
    path('team/', views.team, name='team'),
    path('about/', views.about, name='about'),
    path('memlog/', views.memlog, name='memlog'),
    path('memreg/', views.memreg, name='memregs'),
    path('dashboard/', views.dashboard, name='dash'),
    path('logout/', views.logout, name='logout'),
    path('mdash/', views.mdash, name='mdash'),
    path('mlogout/', views.mlogout, name='mlogout'),
    path('tlogout/', views.tlogout, name='tlogout'),
    path('update/<int:id>', views.update, name='update'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.destroy),
    path('tlog/', views.tlog,name="tlog"),
    path('tdash/', views.tdash,name="tdash"),
    path('treg/', views.treg,name="treg"),
    path('memreg2/', views.memreg2, name="memreg2"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
